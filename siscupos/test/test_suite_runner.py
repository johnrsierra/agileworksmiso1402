"""Django test runner that invokes nose.
You can use... ::
NOSE_ARGS = ['list', 'of', 'args']
in settings.py for arguments that you want always passed to nose.
"""

from __future__ import print_function
from django.test.runner import dependency_ordered
import os
import sys
from optparse import make_option
from types import MethodType
import django
from django.conf import settings
from django.core import exceptions
from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.core.management.commands.loaddata import Command
from django.db import connections, transaction, DEFAULT_DB_ALIAS, models
from django.db.backends.creation import BaseDatabaseCreation
from django.utils.importlib import import_module
import nose.core
from django_nose.plugin import DjangoSetUpPlugin, ResultPlugin, TestReorderer
from django_nose.utils import uses_mysql


from django_nose.runner import BasicNoseRunner, _should_create_database, _mysql_reset_sequences, \
    _foreign_key_ignoring_handle, _skip_create_test_db, _reusing_db


class NoseTestSuiteRunner(BasicNoseRunner):
    """A runner that optionally skips DB creation
    Monkeypatches connection.creation to let you skip creating databases if
    they already exist. Your tests will start up much faster.
    To opt into this behavior, set the environment variable ``REUSE_DB`` to
    something that isn't "0" or "false" (case insensitive).
    """

    def _get_models_for_connection(self, connection):
        """Return a list of models for a connection."""
        tables = connection.introspection.get_table_list(connection.cursor())
        return [m for m in models.loading.cache.get_models() if
               m._meta.db_table in tables]

    def setup_databases(self):
        for alias in connections:
            connection = connections[alias]
            creation = connection.creation
            test_db_name = connection.settings_dict['NAME']  #creation._get_test_db_name()
            orig_db_name = connection.settings_dict['NAME']
            connection.settings_dict['NAME'] = test_db_name
            if _should_create_database(connection):
                connection.settings_dict['NAME'] = orig_db_name
                connection.close()
            else:
                cursor = connection.cursor()
                style = no_style()
                if uses_mysql(connection):
                    reset_statements = _mysql_reset_sequences(
                    style, connection)
                else:
                    reset_statements = connection.ops.sequence_reset_sql(
                    style, self._get_models_for_connection(connection))
                for reset_statement in reset_statements:
                    cursor.execute(reset_statement)

#                transaction.commit_unless_managed(using=connection.alias)
#                creation.create_test_db = MethodType(
#                        _skip_create_test_db, creation, creation.__class__)
        Command.handle = _foreign_key_ignoring_handle
#        return super(NoseTestSuiteRunner, self).setup_databases()
        return self.setup_databases2(test_db_name)


    def teardown_databases(self, *args, **kwargs):
        """Leave those poor, reusable databases alone if REUSE_DB is true."""
        if not _reusing_db():
            return super(NoseTestSuiteRunner, self).teardown_databases(
            *args, **kwargs)
        # else skip tearing down the DB so we can reuse it next time


    def setup_databases2(self, test_db_name2):
        from django.db import connections, DEFAULT_DB_ALIAS

        # First pass -- work out which databases actually need to be created,
        # and which ones are test mirrors or duplicate entries in DATABASES
        mirrored_aliases = {}
        test_databases = {}
        dependencies = {}
        default_sig = connections[DEFAULT_DB_ALIAS].creation.test_db_signature()
        for alias in connections:
            connection = connections[alias]
            if connection.settings_dict['TEST_MIRROR']:
                # If the database is marked as a test mirror, save
                # the alias.
                mirrored_aliases[alias] = (
                    connection.settings_dict['TEST_MIRROR'])
            else:
                # Store a tuple with DB parameters that uniquely identify it.
                # If we have two aliases with the same values for that tuple,
                # we only need to create the test database once.
                item = test_databases.setdefault(
                    connection.creation.test_db_signature(),
                    (connection.settings_dict['NAME'], set())
                )
                item[1].add(alias)

                if 'TEST_DEPENDENCIES' in connection.settings_dict:
                    dependencies[alias] = (
                        connection.settings_dict['TEST_DEPENDENCIES'])
                else:
                    if alias != DEFAULT_DB_ALIAS and connection.creation.test_db_signature() != default_sig:
                        dependencies[alias] = connection.settings_dict.get(
                            'TEST_DEPENDENCIES', [DEFAULT_DB_ALIAS])

        # Second pass -- actually create the databases.
        old_names = []
        mirrors = []

        for signature, (db_name, aliases) in dependency_ordered(test_databases.items(), dependencies):
            test_db_name = test_db_name2
            # Actually create the database for the first connection
            for alias in aliases:
                connection = connections[alias]
                connection.settings_dict['NAME'] = test_db_name
                destroy = False
                old_names.append((connection, db_name, destroy))

        for alias, mirror_alias in mirrored_aliases.items():
            mirrors.append((alias, connections[alias].settings_dict['NAME']))
            connections[alias].settings_dict['NAME'] = (
                connections[mirror_alias].settings_dict['NAME'])

        return old_names, mirrors

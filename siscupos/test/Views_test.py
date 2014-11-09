#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import unittest
from django.test import Client
from django.test import TestCase
import json

class Views_test(TestCase):

    def setUp(self):
        self.client = Client()
        self.corrida75porciento = '85'

    def test_indicador_ocupacion_nivel_1(self):
        resultadoEsperado =[]
        p1 = {'name': 'MISO', 'porc_ocupacion':75, 'drilldown':'miso_ocup'}
        p2 = {'name': 'MATI', 'porc_ocupacion':100, 'drilldown':'mati_ocup'}
        p3 = {'name': 'MESI', 'porc_ocupacion':100, 'drilldown':'mesi_ocup'}
        p4 = {'name': 'MBIT', 'porc_ocupacion':100, 'drilldown':'mbit_ocup'}

        resultadoEsperado.append(p1)
        resultadoEsperado.append(p2)
        resultadoEsperado.append(p3)
        resultadoEsperado.append(p4)

        response = self.client.get('asignaciones_maestria/' + self.corrida75porciento)

        json_string = response.content
        data = json.loads(json_string)


        self.assertEqual(data[0]['name'], resultadoEsperado[0]['name'])
        self.assertEqual(data[0]['porc_ocupacion'], resultadoEsperado[0]['porc_ocupacion'])

    def test_indicador_ocupacion_nivel_2(self):
        resultadoEsperado =[]
        # por cada secciòn se observa, cuantos son de la misma maestria y cuantos de otras.
        p1 = {'name': '4101-1',
              'data': [10, 5]
             }
        p2 = {'name': '4101-2',
              'data': [2, 0]
             }
        p3 = {'name': '4103-1',
              'data': [2, 0]
             }
        p4 = {'name': '4104-1',
              'data': [2, 0]
             }

        resultadoEsperado.append(p1)
        resultadoEsperado.append(p2)
        resultadoEsperado.append(p3)
        resultadoEsperado.append(p4)

        response = self.client.get('asignaciones_seccion/' + self.corrida75porciento)

        json_string = response.content
        data = json.loads(json_string)


        self.assertEqual(data[0]['name'], resultadoEsperado[0]['name'])
        self.assertEqual(data[0]['data'][0], resultadoEsperado[0]['data'][0])
        self.assertEqual(data[0]['data'][1], resultadoEsperado[0]['data'][1])




#if __name__ == '__main__':
#    unittest.main()

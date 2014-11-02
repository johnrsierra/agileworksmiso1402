'use strict';

$('#stack .materia').hover(function() {
 $(this).css('cursor','move');
 }, function() {
 $(this).css('cursor','auto');
});


$( "#stack .materia" ).draggable({
    revert:true,
    clone:true,
    stack:'#stack .materia'
});

$( "div[id^='periodo']" ).droppable({
activeClass: "ui-state-default",
hoverClass: "ui-state-hover",
accept: ":not(.ui-sortable-helper)",
drop: function( event, ui ) {
    console.log(ui.draggable[0]);
    var tmp = ui.draggable[0]
    $(tmp).clone().removeAttr('style').appendTo(this);
}
});


$('table.table').DataTable();

var seleccionarPlan = function(programa){
    console.log(window.corrida);
    $.get( "asignacionr/"+programa+"/"+window.corrida+"/", function( data ) {
        console.log(data);
        setResults(data);
    });
}
var setResults = function(datos){
$('#morris-bar-chart').empty();
Morris.Bar({
        element: 'morris-bar-chart',
        data: datos,
        xkey: 'asignatura',
        ykeys: ['cupos','estudiantes'],
        labels: ['cupos','estudiantes'],
        hideHover: 'auto',
        resize: true,
        xLabelAngle: 60
    });
}

var seleccionarCorrida = function(corridaConsulta){
    console.log(corridaConsulta);

    $.get( "asignacions/"+corridaConsulta+"/", function( data ) {
        console.log(data);
        setResultsCorrida(data);
    });
}

var setResultsCorrida = function(datos){
    var chart = new Highcharts.Chart({
        chart: {
            renderTo: 'morris-bar-chart2',
            type: 'column'
        },

        title: {
            text: 'Total fruit consumtion, grouped by gender'
        },

        xAxis: {
            categories: ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
        },

        yAxis: {
            allowDecimals: false,
            min: 0,
            title: {
                text: 'Number of fruits'
            }
        },

        tooltip: {
            formatter: function () {
                return '<b>' + this.x + '</b><br/>' +
                    this.series.name + ': ' + this.y + '<br/>' +
                    'Total: ' + this.point.stackTotal;
            }
        },

        plotOptions: {
            column: {
                stacking: 'normal'
            }
        },

        series: [{
            name: 'John',
            data: [5, 3, 4, 7, 2],
            stack: 'male'
        }, {
            name: 'Joe',
            data: [3, 4, 4, 2, 5],
            stack: 'male'
        }, {
            name: 'Jane',
            data: [2, 5, 6, 2, 1],
            stack: 'male'
        }, {
            name: 'Janet',
            data: [3, 0, 4, 4, 3],
            stack: 'male'
        }]
    });

}

var setResultsCorridaOld = function(datos){
$('#morris-bar-chart2').empty();
Morris.Bar({
        element: 'morris-bar-chart2',
        data: datos,
        xkey: 'tipo',
        ykeys: ['porcentaje'],
        labels: ['porcentaje'],
        hideHover: 'auto',
        resize: true,
        xLabelAngle: 60
    });
}

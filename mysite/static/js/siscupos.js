'use strict';

$('[data-toggle="popover"]').popover({
    trigger: 'hover',
        'placement': 'top'
});
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
    if($(this).find('.empty').length == 1){
        $(this).find('.empty').remove('.empty');
    }
    var tmp = ui.draggable[0]
    $(tmp).clone().removeAttr('style').appendTo(this).wrap("<div class='col-sm-12 col-lg-12'></div>");
}
});


$('table.table').DataTable();

var resetModal = function(ejec){
    window.corrida = ejec;

}
var seleccionarPlan = function(programa){
    $.get( "asignacionr/"+programa+"/"+window.corrida+"/", function( data ) {

        if(data){
        console.log("data " + data);
            setResults(data);
        }else{
            console.log("do something else");
            Morris.bar = {};
            $('#morris-bar-chart').empty();
        }
    });
}
var setResults = function(datos){
$('#morris-bar-chart').empty();
Morris.bar ={};
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

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
    $("#myModalLabel").text("Resultados ejecución " + ejec);
}

var cerrarModal = function(){
    delete Morris.Bar.data;
    $('#morris-bar-chart').empty();
    $("option:selected").removeAttr("selected");
}
var seleccionarPlan = function(programa){
    $.get( "asignacionr/"+programa+"/"+window.corrida+"/", function( data ) {
        if(data.length != 0){
            setResults(data);
        }else{
            $('#morris-bar-chart').html("<div class='row empty'><div class='col-xs-12 text-center'><i class='fa fa-book fa-3x'></i><div>No hay resultados para este programa</div></div></div>");
        }
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
    delete Morris.Bar.data;
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

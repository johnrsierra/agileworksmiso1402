'use strict';

$('#stack .materia').hover(function() {
 $(this).css('cursor','move');
 }, function() {
 $(this).css('cursor','auto');
});


$( "#stack .materia" ).draggable({
    revert:false,
    clone:false,
    stack:'#stack .materia'
});

$( "div[id^='periodo']" ).droppable({
activeClass: "ui-state-default",
hoverClass: "ui-state-hover",
accept: ":not(.ui-sortable-helper)",
drop: function( event, ui ) {
    alert('aa');
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

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

        var tmp = ui.draggable[0];
        var matExiste = false;

        //Busca todos los paneles de periodos
        $( "div[id^='periodo']" ).each(function(){
            var periodoMat = $(this);

            // Busca todas las materias de un periodo y evalua si es visible y si ya existe
            $(this).find(".materia").each(function(){
                if($(this).css('display') != 'none' && $(this).parent().hasClass('nuevaMateria') == false){
                    if($(this).text().trim() == $(tmp).text().trim()){
                        matExiste = true;
                        $('#alertPanel').text('Materia previamente asignada ' + $(tmp).text().trim());
                        $("#alertPanel").show();
                        setTimeout(function() { $("#alertPanel").hide(); }, 5000);
                    }
                }
            });
        });

        // Si la materia no esta asignada actualmente se procede a su asignación
        if(matExiste == false) {

            if ($(this).find('.empty').length == 1) {
                $(this).find('.empty').remove('.empty');
            }

            $(tmp).clone().removeAttr('style').draggable({
                revert: true,
                clone: true,
                stack: '#stack .materia'
            }).appendTo(this).wrap("<div class='col-sm-12 col-lg-12 nuevaMateria'></div>");
            $(tmp).css('display', 'none');
        }
    }
});

$( "button[id^='drop---']" ).on('click', function(e) {
    // Oculta la materia
    $(this).parent().parent().parent().parent().css('display','none');
});

// Ejecuta el reset de todas las materias a como estaban
$('#resetMaterias').on('click', function(e) {
    // Borra las materias que fueron arrastradas
    $(".nuevaMateria").each(function () {
        $(this).remove();
    });
    // Muestra las materias que se encuentran ocultas
    $("#stack .materia").each(function () {
        if($(this).css('display') == 'none'){
           $(this).css('display','');
        }
    });

    // Muestra las materias que se encuentran ocultas
    $(".asignadaManual").each(function () {
        if($(this).css('display') == 'none'){
           $(this).css('display','');
        }
    });
});

$('#sendMaterias').on('click', function(e) {

    // Obtiene el listado de las materias que son nuevas y se van a guardar
    var objMaterias = [];
    $(".nuevaMateria").each(function () {
        var parentPeriodo = $(this).parent().attr('id');
        var matPeriodo = $(this).text().trim() + "---" + (parentPeriodo.substring("periodo".length));
        objMaterias.push(matPeriodo);
    });

    // Obtiene el listado de las materias que se van a borrar (las que habian sido preasignadas manulamente)
    var objMateriasABorrar = [];
    $(".asignadaManual").each(function () {
        if($(this).css('display') == 'none'){
            var parentPeriodoBorrar = $(this).parent().parent().attr('id');
            var matPeriodoBorrar = $(this).text().trim() + "---" + (parentPeriodoBorrar.substring("periodo".length));
            objMateriasABorrar.push(matPeriodoBorrar);
        }
    });

    var pathname = window.location.pathname;

    var lngStrPath_1 = "/siscupos/estudiante/".length;
    var idxStrCarpet = pathname.indexOf("/carpetaestudiante/");

    var idEstudiante = pathname.substring(lngStrPath_1, idxStrCarpet);

    $.ajax({
        url : "/siscupos/estudiante/"+ idEstudiante +"/nuevacarpeta/",
        type : "POST",
        dataType: "json",
        data:
        {
            idEstudiante: idEstudiante,
            nuevaMaterias: objMaterias,
            borraMaterias: objMateriasABorrar
        },
        success : function(json) {
            $('#result').append( 'Server Response: ' + json.server_response);
            location.reload();
        },
        error : function(xhr,errmsg,err) {
            location.reload();
        }
    });
});

$('table.table').DataTable();

// Gráfica 1

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



//Gráfica 2

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

//Gráfica 3

var cerrarModalDemanda = function(){
    delete Morris.Bar.data;
    $('#morris-bar-chart3').empty();
    $("option:selected").removeAttr("selected");
}
var seleccionarPlan3 = function(corrida){
    $("#modalDemandaAsigLbl").text("Resultados ejecución " + corrida);
    $.get( "demanda/"+corrida+"/", function( datos ) {
        if(datos.length != 0){
           $('#morris-bar-chart3').empty();
            Morris.Bar({
                element: 'morris-bar-chart3',
                data: datos,
                xkey: 'asignatura',
                ykeys: ['demanda','asignadas'],
                labels: ['demanda','asignadas'],
                hideHover: 'auto',
                resize: true,
                xLabelAngle: 60
            });
            delete Morris.Bar.data;
        }else{
            $('#morris-bar-chart3').html("<div class='row empty'><div class='col-xs-12 text-center'><i class='fa fa-book fa-3x'></i><div>No hay resultados para esta corrida</div></div></div>");
        }
    });
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

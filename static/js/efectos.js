$(document).ready(function(){
//efecto menu
    $('.menu a').each(function(index, elemento){
        $(this).css({
            'top' : '-200px'
        });
        $(this).animate({
            top: '0'
        }, 1200 + (index * 500));
    });
    
//efecto header
    if( $(window).width() > 800 ){
        $('header .textos').css({
            opacity: 0,
            marginTop: 0
        });
        
        $('header .textos').animate({
            opacity: 1,
            marginTop: '-52px'
        }, 1500);
       }
    
// Scroll Elemento Menu
    var productos = $('#productos').offset().top,
        ubicacion = $('#ubicacion').offset().top;
    
    $('#btn-productos').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: productos
        }, 500);
    });
    $('#btn-contactanos').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: ubicacion + 30
        }, 500);
        
    });
});
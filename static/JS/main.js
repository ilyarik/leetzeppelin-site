$(document).ready(function(){

    var FLIP_HEADER_VALUE = 60;

    var flipMenu = function () {
        $("#header").css("height", 150);
        $(".menu-area").css("height", "35%");
        $(".sitemap").hide();
    }

    var expandMenu = function () {
        $("#header").removeAttr("style");
        $(".menu-area").removeAttr("style");
        $(".sitemap").show();
    }

    $(document).scroll(function() {
        if ($(this).scrollTop() > FLIP_HEADER_VALUE){
            flipMenu();
        } else if($(this).scrollTop() <= FLIP_HEADER_VALUE) {
            expandMenu();
        }
    });

    if ($(window).scrollTop() > FLIP_HEADER_VALUE) {
        flipMenu();
    }

    $('#contacts-button').hover(
        function () {
            $('#contacts-panel').show();
            $(this).addClass('active-button');
        }, function () {
            $('#contacts-panel').hide();
            $(this).removeClass('active-button');
        }
    )

    $('#contacts-panel').hover(
        function () {
            $(this).show();
            $('#contacts-button').addClass('active-button');
        }, function () {
            $(this).hide();
            $('#contacts-button').removeClass('active-button');
        }
    )
    
    $('#map-button').hover(
        function () {
            $('#map-panel').show();
            $(this).addClass('active-button');
        }, function () {
            $('#map-panel').hide();
            $(this).removeClass('active-button');
        }
    )

    $('#map-panel').hover(
        function () {
            $(this).show();
            $('#map-button').addClass('active-button');
        }, function () {
            $(this).hide();
            $('#map-button').removeClass('active-button');
        }
    )

    $('#about-button').hover(
        function () {
            $('#about-panel').show();
            $(this).addClass('active-button');
        }, function () {
            $('#about-panel').hide();
            $(this).removeClass('active-button');
        }
    )

    $('#about-panel').hover(
        function () {
            $(this).show();
            $('#about-button').addClass('active-button');
        }, function () {
            $(this).hide();
            $('#about-button').removeClass('active-button');
        }
    )
        
        

});
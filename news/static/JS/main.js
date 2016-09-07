$(document).ready(function(){

        var flipMenu = function () {
            $("#header").css("height", 90);
            $(".search-field").css("margin-top", 12);
            $(".logo-area").css("margin-top", 2);
            $(".logo-area h5").hide();
            $(".menu-area").css("height", "35%");
            $(".sitemap").hide();
        }

        var expandMenu = function () {
            $("#header").css("height", 230);
            $(".search-field").css("margin-top", 55);
            $(".logo-area").css("margin-top", 18);
            $(".logo-area h5").show();
            $(".menu-area").css("height", "20%");
            $(".sitemap").show();
        }

        $(window).scroll(function(){

            if ( $(this).scrollTop() > 60){
                flipMenu();
            } else if($(this).scrollTop() <= 60) {
                expandMenu();
            }
        });//scroll
    });
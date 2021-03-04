$(document).ready(function(){
    $(window).on('load resize', function () {
        if ($(this).width() < 1100) {
            $('#towns_slider').owlCarousel({
                nav: false,
                dots: false,
                margin: -20,
                responsive: {
                    0: {items: 1},
                    600: {items: 2},
                    900: {items: 3},
                    1000: {
                        items: 4,
                        margin: 0,
                        rewind: false,
                        callback: false,
                    },
                },
                responsiveRefreshRate: 10,
            });
        } else {
            $('#towns_slider').trigger('destroy.owl.carousel');
        }
    })
});

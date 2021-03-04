let settings = {
    loop: true,
    nav: false,
    dots: true,
    margin: 0,
    items: 1,
}

$(document).ready(function(){
    $(window).on('load resize', function () {
        if ($(this).width() < 768) {
            $('#tour-gallery').owlCarousel(settings);
        } else {
            $('#tour-gallery').trigger('destroy.owl.carousel');
        }
    })
});
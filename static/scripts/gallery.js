let settings = {
    loop: false,
    nav: false,
    dots: true,
    margin: 0,
    items: 1,
    mouseDrag: false,
}

$(document).ready(function(){
    $(window).on('load resize', function () {
        console.log($(this).width())
        if ($(this).width() < 768) {
            $('#tour-gallery').owlCarousel(settings);
        } else {
            $('#tour-gallery').trigger('destroy.owl.carousel');
        }
    })
});
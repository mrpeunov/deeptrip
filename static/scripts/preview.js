$(document).ready(function(){
    let preview_gallery_settings = {
        items: 1,
        slideSpeed: 200,
        nav: true,
        lazyLoad:true,
        loop:true,
        margin:0,
        dots: true,
    }

    function css_setting(){
        console.log("Поправить стиль кода");
        if($('.tours_item').length % 3 === 0){
            $('.tours_items').addClass("zero");
            $('.tours_items').removeClass("not_zero");
        } else {
            $('.tours_items').addClass("not_zero");
            $('.tours_items').removeClass("zero");
        }
    }

    function preview_galley_create(){
       $('.preview_gallery').owlCarousel(preview_gallery_settings);
    }

    preview_galley_create();

    $('#tours_more').on('click', function (e){
        let $tours = $('#tours');

        let current_page = parseInt($tours.data('page'), 10);
        let next_page = 0; //current_page + 1;
        let city_slug = $tours.data('city');

        e.preventDefault();

        $.ajax({
            url: '/api/v1/get_more_tours/',
            method: 'GET',
            data: {
                'page': next_page,
                'city_slug': city_slug
            },
            success: function(data) {
                $tours.append(data);
                $('.preview_gallery').owlCarousel(preview_gallery_settings);
                css_setting();
                console.log("Нужно доделать обновление номера страницы")
            },
            error: function(data) {
                console.log("Error");
            }
        });
    });

    css_setting();

});


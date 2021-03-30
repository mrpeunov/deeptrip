$(document).ready(function(){

    //настройки owl gallery
    let preview_gallery_settings = {
        items: 1,
        mouseDrag: false,
        slideSpeed: 200,
        nav: true,
        lazyLoad:true,
        loop:true,
        margin:0,
        dots: true,
    }

    //обновление css отображения экскурсий
    //из-за кривой реализации justify-content space-between
    function css_setting(){
        let $tours_items = $('.tours_items');
        if($('.tours_item').length % 3 === 0){
            $tours_items.addClass("tours_zero");
            $tours_items.removeClass("tours_not_zero");
        } else {
            $tours_items.addClass("tours_not_zero");
            $tours_items.removeClass("tours_zero");
        }
    }

    //запуск owl gallery
    function preview_galley_create(){
       $('.preview_gallery_item').owlCarousel(preview_gallery_settings);
    }

    //запуск при загрузке
    preview_galley_create();
    css_setting();

    //обработка клика по "показать ещё"
    $('#tours_more').on('click', function (e){
        //отмена дефолтного действия
        e.preventDefault();

        let $tours = $('#tours');

        //получаем данные для ajax запроса
        let current_page = parseInt($tours.attr('data-page'), 10);
        let next_page = current_page + 1; // = 0
        let city_slug = $tours.data('city');

        $.ajax({
            url: '/api/v1/get_more_tours/',
            method: 'GET',
            data: {
                'page': next_page,
                'city_slug': city_slug
            },
            success: function(data) {
                //если больше нет экскурсий, то убираем кнопку
                if(getCookie("more") === "True"){
                    console.log(getCookie("more"));
                } else {
                    $('.tours_more').addClass("none");
                }

                //добавляем данные на страницу
                $tours.append(data);

                //обновляем новые данные
                preview_galley_create();
                css_setting();

                //устанавливаем новый атрибут текущей страницы
                $tours.attr('data-page', next_page)
            },
            error: function(data) {
                console.log("Error");
            }
        });
    });

    //отменяем переход по ссылке
    $('.owl-nav button').attr("onclick", "return false;")

    $('#update_none_button').on('click', function () {
        preview_galley_create();
        css_setting();
    })
});


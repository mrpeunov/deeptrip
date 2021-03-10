$(document).ready(function(){
    //настроки для mobile
    let settings = {
        loop: false,
        nav: false,
        dots: true,
        margin: 0,
        items: 1,
        mouseDrag: false,
    }

    //настройки для desktop open
    let open_settings = {
        loop: false,
        nav: true,
        dots: false,
        margin: 0,
        items: 1,
        mouseDrag: false,
        onChanged: callback,
    }

    //переиспользуемые элементы
    let $information_about_number = $('#gallery_open_info');
    let $tour_gallery_item = $('.tour_gallery_item');
    let $tour_gallery = $('#tour-gallery');
    let $tour_gallery_wrap = $('#tour-gallery-wrap');
    let $all_photo = $('#all_photo');

    //callback on change slide
    function callback(event){
        let number = event.item.index + 1;
        let count = event.item.count;
        update_information(number, count);
    }

    let mobile = true;

    $(window).on('load', function () {
        if ($(this).width() < 768) {
            mobile_gallery();
            mobile = true;
        } else {
            mobile = false;
        }
    })

    $(window).on('resize', function () {
        if ($(this).width() < 768) {
            if (!mobile){
                desktop_open_gallery_destroy();
                mobile_gallery();
                mobile = true;
            }
        } else {
            if (mobile){
                mobile_gallery_destroy();
                mobile = false;
            }

        }
    })

    //клик по кнопке все фото
    $all_photo.click(function (){
        desktop_open_gallery(1);
    })

    //клик по отдельному элементу
    $tour_gallery_item.click(function (){
        let number = $tour_gallery_item.index(this) + 1;
        desktop_open_gallery(number)
    })

    $('#gallery_button_close').click(function (){
        desktop_open_gallery_destroy();
    })

    //инициализация мобильной галереи
    function mobile_gallery(){
        $tour_gallery.owlCarousel(settings);
    }

    function mobile_gallery_destroy(){
        $tour_gallery.trigger('destroy.owl.carousel');
    }

    //открытие галареи по номеру фотки
    function desktop_open_gallery(number){
        //добавляем класс задающий все стили
        $tour_gallery_wrap.addClass('tour_gallery_open');

        //инициализируем
        $tour_gallery.owlCarousel(open_settings);

        //устанавливаем номер открытой фотки
        $tour_gallery.trigger("to.owl.carousel", [number-1, 0]);

        //убираем прокрутку
        $("body").css("overflow","hidden");

        //высчитываем размеры блока и окна
        let height_block = $tour_gallery_item.height();
        let height_window = $(window).height();

        //отступ основного блока
        let margin_block = (height_window - height_block)/2;
        let margin_information = height_block + margin_block + 10;

        //установка отступов
        $tour_gallery.css("margin-top", margin_block)
        $information_about_number.css("top", margin_information);

        //количество элементов на странице
        let count = $tour_gallery_item.length;

        update_information(number, count)
    }

    //дестрой галереи
    function desktop_open_gallery_destroy(){
        $tour_gallery.trigger('destroy.owl.carousel');
        $tour_gallery_wrap.removeClass('tour_gallery_open');
        $("body").css("overflow","auto");
        $tour_gallery.removeAttr('style');
    }

    //обновление номера фотки
    function update_information(number, count){
        $information_about_number.html(number + " из " + count);
    }
});













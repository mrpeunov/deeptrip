//старье


$(function(){
    let currentClass = "tour_gallery_list_item_current";
    let $item = $('.tour_gallery_list_item');

    //открывает изображение переданное в блок
    function open_photo(block){
        $item.removeClass(currentClass);
        $(block).addClass(currentClass);
        let src = $('.tour_gallery_list_item_current img').attr("src");
        $("#main_photo").attr("src", src);
        $(block).scrollLeft(10);
    }

    //устанавливает для главного фото размер 16 к 9
    function set_size_main_photo(){
        let $main_photo = $('.tour_gallery_main');
        let ratio = 0.56;
        $main_photo.height($main_photo.width() * ratio);
    }

    //при загрузке и обновлении
    set_size_main_photo();
    $(window).resize(function(){
        set_size_main_photo();
    });

    //меняет главное фото при клике на него
    $item.click(function (){
        open_photo(this);
    });

    //меняет главное фото при клике по кнопке влево или вправо
    $('.tour_gallery_main_button').click(function (){
        //выбираем следующее или прыдудщее фото
        let photo;
        if($(this).is('#prev')) photo = $('.tour_gallery_list_item_current').prev();
        if($(this).is('#next')) photo = $('.tour_gallery_list_item_current').next();

        //если фото не конечное, то меняем главное
        if(photo.is('.tour_gallery_list_item')) open_photo(photo);

    })
});


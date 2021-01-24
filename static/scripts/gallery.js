$(function(){
    let $main_photo = $('.tour_gallery_main');
    let ratio = 0.56;

    $main_photo.height($main_photo.width() * ratio);

    $(window).resize(function(){
        $main_photo.height($main_photo.width() * ratio);
    });
});
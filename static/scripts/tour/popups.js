
let $comment_popup = $('#comment_popup');

$('#send_comment').on('click', function () {
    open_popup_comment();
})

$comment_popup.on('click', function () {
    close_popup_comment();
})

$('#comment_popup_form').on('click', function (event){
    event.stopPropagation();
})

$('#tour_popup_close').on('click', function (){
    close_popup_comment();
})

function open_popup_comment(){
    $comment_popup.css("display", "flex");
    $('body').css("overflow", "hidden");
}

function close_popup_comment(){
    $comment_popup.css("display", "none");
    $('body').removeAttr("style");
}

$('.tour_popup_comment_rating_items_item').on('click', function (){
    $('.tour_popup_comment_rating_items_item').removeClass('active');
    $(this).addClass('active');
})


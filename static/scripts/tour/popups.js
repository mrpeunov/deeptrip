$('#send_comment').on('click', function () {
    $('#comment_popup').css("display", "flex");
})

$('#comment_popup').on('click', function () {
    $('#comment_popup').css("display", "none");
})

$('#comment_popup_form').on('click', function (event){
    event.stopPropagation();
})

$('.tour_popup_comment_rating_items_item').on('click', function (){
    $('.tour_popup_comment_rating_items_item').removeClass('active');
    $(this).addClass('active');
})


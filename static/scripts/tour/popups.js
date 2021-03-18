
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

$('#popup_comment_button').on('click', function (){
    //собираем данные
    let content = $("#comment_content").val()
    let name = $("#comment_name").val()

    //дефолтная оценка - 5
    let rating = 5

    $(".tour_popup_comment_rating_items_item").each(function (index) {
        if ($(this).hasClass("active")) rating = index;
    })


    //отправляем на сервер
    $.ajax({
        url:  document.location.href + '/comment/',
        method: 'GET',
        data: {
            'content': content,
            'name': name,
            'rating': rating,
        },
        success: function(data) {
            console.log(data);
        },
        error: function(data) {
            console.log("Ошибка при добавлении отзыва");
        }
    });
})


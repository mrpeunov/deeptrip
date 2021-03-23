
let $comment_popup = $('#comment_popup');
let $popup_comment_button = $('#popup_comment_button');
let $comment_name = $("#comment_name");
let $comment_content = $('#comment_content');

$comment_name.on('input', function () {
    update_button();
})

$comment_content.on('input', function () {
    update_button();
})

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

function update_button(){
    if ($comment_content.val() && $comment_name.val()){
        $popup_comment_button.removeClass('not_active');
    } else {
        $popup_comment_button.addClass('not_active');
    }
}

$('.tour_popup_comment_rating_items_item').on('click', function (){
    $('.tour_popup_comment_rating_items_item').removeClass('active');
    $(this).addClass('active');
})

$popup_comment_button.on('click', function (){
    //если данные пустые
    if($popup_comment_button.hasClass('not_active')) return 0;

    //собираем данные
    let content = $comment_content.val();
    let name = $comment_name.val();

    //дефолтная оценка - 5
    let rating = 5;

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


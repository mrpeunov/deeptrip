
let $comment_popup = $('#comment_popup');
let $popup_comment_button = $('#popup_comment_button');
let $comment_name = $("#comment_name");
let $comment_content = $('#comment_content');
let $comment_popup_form = $('#comment_popup_form');
let $comment_popup_ok = $("#comment_popup_ok")

//обновление кнопки при вводе комментария
$comment_name.on('input', function () { update_button(); })
$comment_content.on('input', function () { update_button(); })

//открытие окна при клике по кнопке
$('#send_comment').on('click', function () {
    open_popup_comment();
})

//закрытие окна при клике рандомной областит
$comment_popup.on('click', function () {
    close_popup_comment();
})

//не вырубать окно при клике не по нему (мб переделать)
console.log("Переделать на нормальную обботку одного ")
$('.tour_popup_wrap').on('click', function (event){ event.stopPropagation() })

//клик по крестику
$('#tour_popup_close').on('click', function (){
    close_popup_comment();
})

//клик по кнопке закрыть
$('.tour_popup_comment_completed_close').on('click', function (){
    close_popup_comment();
})

//открытие попапа
function open_popup_comment(){
    $comment_popup.css("display", "flex");
    $('body').css("overflow", "hidden");
}

//функция закрытия попапа
function close_popup_comment(){
    $comment_popup.css("display", "none");
    $('body').removeAttr("style");
    $comment_popup_ok.addClass("none");
    $comment_popup_form.removeClass("none");
}

//обновление кнопки в зависмости от пустоты инпутов
function update_button(){
    if ($comment_content.val() && $comment_name.val()){
        $popup_comment_button.removeClass('not_active');
    } else {
        $popup_comment_button.addClass('not_active');
    }
}

//обработка выбора оценки
$('.tour_popup_comment_rating_items_item').on('click', function (){
    $('.tour_popup_comment_rating_items_item').removeClass('active');
    $(this).addClass('active');
})

//отправка коммента
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
        method: 'POST',
        data: {
            'content': content,
            'name': name,
            'rating': rating,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function(data) {
            console.log(data);
            $comment_popup_ok.removeClass("none");
            $comment_popup_form.addClass("none");
            $comment_content.val("")
            $comment_name.val("");
        },
        error: function(data) {
            console.log("Ошибка при добавлении отзыва");
        }
    });
})


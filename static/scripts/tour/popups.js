
let $comment_popup = $('#comment_popup');
let $popup_comment_button = $('#popup_comment_button');
let $comment_name = $("#comment_name");
let $comment_content = $('#comment_content');
let $comment_popup_form = $('#comment_popup_form');
let $question_popup_form = $('#question_popup_form');
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

$('.tour_popup_wrap').on('click', function (event){ event.stopPropagation() })

//клик по крестику
$('#tour_popup_close').on('click', function (){
    close_popup_comment();
    close_popup_question();
})

//клик по кнопке закрыть
$('.tour_popup_comment_completed_close').on('click', function (){
    close_popup_comment();
    close_popup_question();
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

$("#question").on("click", function () {
    open_popup_question();
})

function open_popup_question() {
    $comment_popup.css("display", "flex");
    $comment_popup_form.addClass("none");
    $question_popup_form.removeClass("none");
    $('body').css("overflow", "hidden");
}

function close_popup_question(){
    $comment_popup_form.removeClass("none");
    $question_popup_form.addClass("none");
}

let $question_connection_item = $(".tour_popup_question_connection_item");

$question_connection_item.on("click", function () {
    $question_connection_item.removeClass("active");
    $(this).addClass("active");

    if($(this).html() === "Телефон"){
        $("#question_email").addClass("none");
        $("#question_phone").removeClass("none");
    }
    else{
        $("#question_email").removeClass("none");
        $("#question_phone").addClass("none");
    }

    update_button_question();
})

let inp = document.querySelector('#question_phone');
let $question_name = $("#question_name");
let $question_phone = $("#question_phone");
let $question_email = $("#question_email");
let $question_button = $("#question_button");
let $question_content = $("#question_content");

$question_name.on('input', function () { update_button_question(); })
$question_phone.on('input', function () { update_button_question(); })
$question_email.on('input', function () { update_button_question(); })
$question_content.on('input', function () { update_button_question(); })

// Проверяем фокус
inp.addEventListener('focus', _ => {
  // Если там ничего нет или есть, но левое
  if(!/^\+\d*$/.test(inp.value))
    // То вставляем знак плюса как значение
    inp.value = '+';
});

inp.addEventListener('keypress', e => {
  // Отменяем ввод не цифр
  if(/[^0-9+()-]/.test(e.key))
    e.preventDefault();
});

function update_button_question(){
    let phone = true;

    $question_connection_item.each(function () {
        if($(this).hasClass("active")){
            phone = $(this).html() === "Телефон";
        }
    })

    let active = false;

    if(phone){
        active = $question_name.val() && $question_content.val()
            && $question_phone.val()
    } else {
        active = $question_name.val() && $question_content.val()
            && $question_email.val()
    }
    if (active){
        $question_button.removeClass('not_active');
    } else {
        $question_button.addClass('not_active');
    }
}
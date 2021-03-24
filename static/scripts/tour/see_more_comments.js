
let $see_more_comments = $("#see_more_comments")

//обработка клика по "показать ещё"
$see_more_comments.on('click', function (){

    //получаем данные для ajax запроса
    let current_page = parseInt($see_more_comments.attr('data-page'), 10);
    let next_page = current_page + 1;
    let tour_slug = $see_more_comments.data('tour');

    $.ajax({
        url: '/api/v1/get_more_comments/',
        method: 'GET',
        data: {
            'page': next_page,
            'tour_slug': tour_slug
        },
        success: function(data) {
            //если больше нет экскурсий, то убираем кнопку
            if(getCookie("more_comments") === "False"){
                $see_more_comments.addClass("none");
                $('#send_comment').css("width", "100%");
            }

            //добавляем данные на страницу
            let $review_items = $('.tour_information_review_items');
            $review_items.append(data);

            $('.tour_information_review_item').each(function () {
                $(this).slideDown(300);
            })

            //устанавливаем новый атрибут текущей страницы
            $see_more_comments.attr('data-page', next_page)
        },
        error: function(data) {
            console.log("Error");
        }
    });
});
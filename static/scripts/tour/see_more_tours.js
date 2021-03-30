let $see_more_tours = $("#see_more_tours");

//обработка клика по "показать ещё"
$see_more_tours.on('click', function (){
    console.log("Покажи сиськи");
    //получаем данные для ajax запроса
    let next_page = parseInt($see_more_tours.attr('data-page'), 10) + 1;
    let tour_slug = $see_more_tours.data('tour');


    $.ajax({
        url: '/api/v1/get_more_recommended/',
        method: 'GET',
        data: {
            'page': next_page,
            'count': 3,
            'tour_slug': tour_slug
        },
        success: function(data) {
            if(getCookie("more_tours") === "False"){
                $see_more_tours.parent().css("display", "none");
            }

            //добавляем данные на страницу
            let $recommended_items = $("#recommended_items");
            $recommended_items.append(data);
            $('.tours_item').each(function () {
                $(this).slideDown(500);
            })

            $('#update_none_button').trigger("click");

            //устанавливаем новый атрибут текущей страницы
            $see_more_tours.attr('data-page', next_page)
        },
        error: function(data) {
            console.log("Error");
        }
    });

});
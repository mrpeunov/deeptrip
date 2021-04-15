$(document).ready(function() {
    let $booking_button = $('#booking_button');


    $booking_button.on("click", function () {
        make_booking();
    })

    function make_booking() {
        let $booking_name = $('#booking_name');
        let $booking_phone = $('#booking_phone');

        let name = $booking_name.val();
        let phone = $booking_phone.val();

        //проверка заполненности данных
        if(name.length === 0){

        }

        if(phone.length === 0){

        }

        //собрать данные
        let $booking_date = $(".booking-date");
        let $booking_time = $('.booking-time');

        let slug = $booking_button.attr("data-slug")

        let day = $booking_date.attr("data-day");
        let month = $booking_date.attr("data-month");
        let year = $booking_date.attr("data-year");
        let time = $booking_time.html();

        let rate = $('.booking-rate').html();
        let group = $('.booking-group').html();
        let children = $('.booking-children').html();

        let amount = $('.calculate_price').html();
        let prepay = $('.prepay_count').html();

        console.log("здесь")

        //отправить ajax
        $.ajax({
                url: '/new_order/',
                method: 'POST',
                data: {
                    'name': name,
                    'phone': phone,
                    'mail': '',
                    'tour_slug': slug,
                    'date_tour': {
                        'day': day,
                        'month': month,
                        'year': year
                    },
                    'start_tour': time,
                    'rate': rate,
                    'group': group,
                    'children': children,
                    'amount': amount,
                    'prepay': prepay,
                    'transfer': '',
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                },
                success: function(data) {
                    console.log(data)

                    //перевести на нужную страницу
                },
                error: function(data) {
                    console.log("Ошибка" + data);
                }
            });

        if($booking_button.data("prepay") === "True"){
            // если предоплата есть
        } else {
            // если предоплаты нет
        }
    }


})


$(function() {
    let $ok = $("#ok");

    let min_price = parseInt($("#min").data("min"));
    let max_price = parseInt($("#max").data("max"));

    //слайдер для выбора цены
    $( "#slider-range" ).slider({
          range: true,
          min: min_price,
          max: max_price,
          step: 10,
          values: [min_price, max_price],
          slide: function( event, ui ) {
              $("#min").html(ui.values[0]);
              $("#max").html(ui.values[1]);

              min_price = ui.values[0];
              max_price = ui.values[1];

              update_count();
          }
    });

    $ok.on("click", function () {
        $(this).toggleClass("active");
        update_count();
    })

    $("#show").on("click", function () {
        update_view();
    })

    $(".filter_item").on("click", function () {
        update_count();
    })

    $("#reset").on("click", function () {
        reset();
    })

    function update_count() {
        let count = get_count_view_tours();
        $("#count").html(count);
    }

    //получить количество видимых экскурсий
    function get_count_view_tours() {
        let choice_category_array = get_choice_category_array();
        let prepay = get_prepay();

        let count = 0; //количество подходящих экскурсий
        //перебираем все эскурсии
        $('.filter_tours_item').each(function () {
            let view = get_view_tour($(this), min_price, max_price, prepay, choice_category_array)

            //если экскурсия видим то увеличим количество
            if(view === true){
                count++;
            }
        })

        return count;
    }

    //обновить видимые
    function update_view() {
        let choice_category_array = get_choice_category_array();
        let prepay = get_prepay();

        //сортировка по количеству совпадений категорий
        if(choice_category_array.length !== 0){
            let items = $('.filter_tours_item');
            let array_items = $.makeArray(items);
            array_items.sort(function(a, b) {
                let rating_a = get_rating_for_tour($(a), choice_category_array);
                let rating_b = get_rating_for_tour($(b), choice_category_array);
                return rating_b - rating_a;
            });

            $(array_items).appendTo("#tours");
        }

        //перебираем все эскурсии
        $('.filter_tours_item').each(function () {
            $(this).removeClass("none");

            let view = get_view_tour($(this), min_price, max_price, prepay, choice_category_array)

            //если экскурсия видимая то
            if(view === false){
                $(this).addClass("none")
            }
        })

    }

    function reset() {
        $(".filter_item").prop('checked', false);
        min_price = parseInt($("#min").data("min"));
        max_price = parseInt($("#max").data("max"));
        console.log(min_price, max_price);
        $("#min").html(min_price);
        $("#max").html(max_price);
        $("#slider-range").slider("values", [min_price, max_price])
        $("ok").removeClass("active");
        update_view();
    }

    function get_prepay(){
        let prepay = true; //изначально предоплата допустима
        if($ok.hasClass("active")){
            prepay = false;
        }

        return prepay;
    }

    //получить колечество категорий в которые попадает экскурсия
    function get_rating_for_tour($tour, categories_choice){
        let rating = 0;
        let categories = $tour.data("categories").split(";");
        categories.forEach(function (category) {
            categories_choice.forEach(function (item) {
                if(category === item){
                    rating++;
                }
            })
        })

        return rating;
    }

    //получим массив с выбранными категориями
    function get_choice_category_array() {
        let checked_array = [];
        $('.filter_item:checked').each(function(){
            checked_array.push($(this).attr('value'));
        });

        return checked_array;
    }

    //получить видимость экскурсии
    function get_view_tour($tour, min_price, max_price, prepay, choice_category_array) {
        //изначально считаем все экскурсии видимыми
        let view = true;

        //если не подходит по цене, делаем невидимой
        let price = parseInt($tour.data("price"));
        if( price < min_price || price > max_price){
            view = false;
        }

        //если ни одной категории не выбрано, то не учитываем этот фильтр
        if(choice_category_array.length !== 0){
            //получаем рейтинг, если 0, то не отображаем
            let rating = get_rating_for_tour($tour, choice_category_array);
            if(rating === 0){
                view = false;
            }
        }

        //если включено без предоплаты, а предоплата есть, то не отображаем
        if(prepay === false && $tour.data("prepay") === "+"){
            view = false;
        }

        return view;
    }
});
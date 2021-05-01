$(function() {
    let $ok = $("#ok"); //блок с предоплатой
    let $slider_range = $( "#slider-range" ); //слайдер
    let $filter_item = $(".filter_item"); //элемент с галочкой

    //максимальные и минимальные блоки
    let $min_block = $("#min");
    let $max_block = $("#max");
    let min_price = parseInt($min_block.data("min"));
    let max_price = parseInt($max_block.data("max"));

    let show_button = false;
    let $show = $("#show");

    //слайдер для выбора цены
    $slider_range.slider({
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

              show_button = true;
              update_view_button();
              update_count();

          }
    });

    //при клике на блок с предоплатой
    $ok.on("click", function () {
        $(this).toggleClass("active");
        show_button = true;
        update_view_button();
        update_count();
    })

    //при клике на показать обновляем отображение экскурсий
    $show.on("click", function () {
        //если кнопка не заблокирована, обновить
        if(!$show.hasClass("blocked")) {
            update_view();
            show_button = false;
            update_view_button();
        }
    })

    $filter_item.on("click", function () {
        show_button = true;
        update_view_button();
        update_count();
    })

    //при клике на сбросить сбрасываем настройки
    $("#reset").on("click", function () {
        reset();
    })

    //при клике на сбросить в меню сбрасываем настройки
    $("#reset_menu").on("click", function () {
        reset();
    })

    //обновление количества экскурсий
    function update_count() {
        let count = get_count_view_tours();
        $("#count").html("Найдено " + count + " экскурсий");

        if (count === 0){
            show_button = false;
            update_view_button();
        }
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
            //изначально видимая
            $(this).removeClass("none");

            //получаем видимость экскурсии
            let view = get_view_tour($(this), min_price, max_price, prepay, choice_category_array)

            //если экскурсия невидимая то, убираем видимость
            if(view === false){
                $(this).addClass("none")
            }
        })

        let count = get_count_view_tours();
        $("#count").html("Отображено " + count + " экскурсий");

        let destination = $("#tours").offset().top - 20;
        $('html, body').animate({
            scrollTop: destination
        }, 300);
    }

    //сбросить настройки
    function reset() {
        //убрать все поставленныегалоки в категориях
        $(".filter_item").prop('checked', false);

        //получить максимальную и минимальную цену
        min_price = parseInt($min_block.data("min"));
        max_price = parseInt($max_block.data("max"));

        //установить максимальную и минимальную цену на странице
        $min_block.html(min_price);
        $max_block.html(max_price);

        //установить максимальную и минимальную цену в слайдере
        $slider_range.slider("values", [min_price, max_price])

        //убрать галочку
        $("#ok").removeClass("active");

        //обновить видимость кнопки
        show_button = false;
        update_view_button();
        //обновить отображение
        update_view();



        $("#count").html("Отображены все экскурсии");

        $('html,body').animate({
            scrollTop: 0
        }, 300);
    }

    //нужна или нет предоплата
    function get_prepay(){
        //return true если предоплата возможно
        //return false если нужны только экскурсии без предоплаты
        let prepay = true;
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

    //обновить видимость кнопки
    function update_view_button() {
        if(show_button === false){
            $show.addClass("blocked");
        } else {
            $show.removeClass("blocked");
        }
    }

    $(".standard_dropdown_list_item").on("click", function () {
        let city = $(this).data("price");
        window.location.href = window.location.origin + "/" + city + "/filter/"
    })

});
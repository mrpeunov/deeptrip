ymaps.ready(init);
let $map = $("#booking_map");
let myMap;

function init() {
    myMap = new ymaps.Map("booking_map", {
        center: [43.585472, 39.723089],
        zoom: 9, // от 0 (весь мир) до 19.
        controls: []
    });

    if ($map.data("transfer") === "yn" || $map.data("transfer") === "y") {
        create_map_y();
    } else {
        create_map_n();
    }
}

$("input[name='transfer']").click(function () {
    let $booking_map = $('#booking_map');

    $(".booking_transfer_text").addClass("none");
    $("#transfer_text_" + $(this).val()).removeClass("none");

    if ($(this).val() === "yes") {
        create_map_y();
        $booking_map.attr("data-bool", "True")
    } else {
        create_map_n();
        $booking_map.attr("data-bool", "False")
    }
})

function create_map_n(){
    // Создание карты для трансфер есть.
    clear_map();

    //нужно очистить существующие точки
    $('.point').each(function () {
        view_point($(this));
    })
}

function create_map_y() {
    clear_map();

    $('.t_point').each(function () {
        view_point($(this));
    })
}

let points = [];

function view_point($elem) {
    let x = parseFloat($elem.data("x").replace(',', '.'));
    let y = parseFloat($elem.data("y").replace(',', '.'));
    let text = $(this).data("title");

    let point = new ymaps.Placemark([x, y], {
        balloonContent: text,
        iconCaption: text,

    }, {
        iconLayout: 'default#imageWithContent',
            // Своё изображение иконки метки.
        iconImageHref: '/static/img/booking/standard.png',
        // Размеры метки.
        iconImageSize: [24, 24],
        // Смещение левого верхнего угла иконки относительно
        // её "ножки" (точки привязки).
        iconImageOffset: [-24, -24],
        // Смещение слоя с содержимым относительно слоя с картинкой.
        iconContentOffset: [15, 15],
        // Макет содержимого.
    })

    myMap.geoObjects.add(point);

    points.push(point)

    point.events.add('click', function (e) {
        // Ссылку на объект, вызвавший событие,
        // можно получить из поля 'target'.
        points.forEach(function(item) {
          item.options.set('iconImageHref', '/static/img/booking/standard.png');
        })

        e.get('target').options.set('iconImageHref', '/static/img/booking/active.png');
    })
}

function clear_map() {
    myMap.geoObjects.removeAll();
}
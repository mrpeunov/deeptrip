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
    $(".booking_transfer_text").addClass("none");
    $("#transfer_text_" + $(this).val()).removeClass("none");

    if ($(this).val() === "yes") {
        create_map_y();
    } else {
        create_map_n();
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

function view_point($elem) {
    let x = parseFloat($elem.data("x").replace(',', '.'));
    let y = parseFloat($elem.data("y").replace(',', '.'));
    let text = $(this).data("title");

    myMap.geoObjects.add(new ymaps.Placemark([x, y], {
        balloonContent: text,
        iconCaption: text
    }, {
        preset: 'islands#greenDotIconWithCaption'
    }))
}

function clear_map() {
    myMap.geoObjects.removeAll();
}
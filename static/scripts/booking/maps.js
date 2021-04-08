ymaps.ready(init);

function init(){
    // Создание карты.
    let myMap = new ymaps.Map("booking_map", {
        // Координаты центра карты.
        // Порядок по умолчанию: «широта, долгота».
        // Чтобы не определять координаты центра карты вручную,
        // воспользуйтесь инструментом Определение координат.
        center: [43.585472, 39.723089],
        // Уровень масштабирования. Допустимые значения:
        // от 0 (весь мир) до 19.
        zoom: 9,
        controls: []
    });

    $('.point').each(function () {
        let x = parseFloat($(this).data("x").replace(',', '.'));
        let y = parseFloat($(this).data("y").replace(',', '.'));
        let text = $(this).data("title");

        console.log(x, y);

        myMap.geoObjects.add(new ymaps.Placemark([x, y], {
            balloonContent: text,
            iconCaption: text
        }, {
            preset: 'islands#greenDotIconWithCaption'
        }))
    })


}
ymaps.ready(init);
let mainMap;
let objectManager;

//инициализация карты
function init() {
    mainMap = new ymaps.Map("map", {
        center: [43.585472, 39.723089],
        zoom: 9, // от 0 (весь мир) до 19.
        controls: []
    }, {
        searchControlProvider: 'yandex#search'
    });

    objectManager = new ymaps.ObjectManager({
        clusterize: true, // Чтобы метки начали кластеризоваться, выставляем опцию.
        gridSize: 32, // ObjectManager принимает те же опции, что и кластеризатор.
        clusterDisableClickZoom: true
    });

    objectManager.objects.options.set('preset', 'islands#nightCircleDotIcon');
    objectManager.clusters.options.set('preset', 'islands#nightClusterIcons');
    mainMap.geoObjects.add(objectManager);

    create_map();
}

//создание точки на карте
function get_point_from_block($elem) {
    let x = parseFloat($elem.data("lat").replace(',', '.'));
    let y = parseFloat($elem.data("lon").replace(',', '.'));
    let id = $elem.data("id");

    return {
        type: 'Feature',
        id: id,
        geometry: {
            type: 'Point',
            coordinates: [x, y]
        }
    };
}

//создание карты
function create_map(){
    //создаим json под точки
    let points = {
        type: 'FeatureCollection',
        features: []
    }

    //получим точки из html
    $('.point').each(function () {
        points.features.push(get_point_from_block($(this)));
    })

    //добавим на карту
    objectManager.add(points);
}

let $wrap = $(".wrap");
$wrap.mouseenter(function() {
    //при наведении на мышку
    let tour_id = $(this).data("tour_id");
    let points_id_array = block_to_points_array($(this));
    set_active_tour(tour_id, points_id_array);
})
$wrap.mouseleave(function(){
    remove_active_tour();
});

let active_tour;

//получает из блока экскурсии массив из id точек на карте
function block_to_points_array($block) {
    let int_array = [];

    let points_str_array = $block.data("points").split(";");
    points_str_array.forEach(function (value) {
        if(value) int_array.push(parseInt(value));
    })

    return int_array;
}

//устанавливаем активный тур
function set_active_tour(tour_id, points_id_array){
    //убираем следы прыдудщего активного тура
    remove_active_tour();

    active_tour = tour_id;

    console.log(points_id_array);
    //подсвечиваем точки, которые соотвествуют активному туру
    points_set_active(points_id_array);
}

function remove_active_tour(){
    clear_all_points();
    //перебиваем все точки и устанавливаем их в дефолтное состояние
}


function points_set_active(points_id_array) {
    points_id_array.forEach(function (point_id) {
        objectManager.objects.setObjectOptions(point_id, {
            preset: 'islands#greenIcon'
        });
    })
}

function clear_point(point) {
    point.options.set('iconImageHref', '/static/img/booking/standard.png');
}

function clear_all_points() {
    /*
    points.forEach(function (point) {
        point.options.set('iconImageHref', '/static/img/booking/standard.png');;
    })*/
}

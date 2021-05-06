/*
* Блок работы с яндекс картами
* Здесь всё что касается API
*/

ymaps.ready(init); //при готовности инициализируем
let mainMap; //сама карта
let objectManager; //менеджер объектов

//инициализация карты
function init() {
    mainMap = new ymaps.Map("map", {
        center: [43.585472, 39.723089],
        zoom: 9, // от 0 (весь мир) до 19.
        controls: ['searchControl']
    }, {
        searchControlProvider: 'yandex#map',
        noPopup: true,
        preset: 'islands#geolocationIcon'
    });

    objectManager = new ymaps.ObjectManager({
        clusterize: true, // Чтобы метки начали кластеризоваться, выставляем опцию.
        gridSize: 32, // ObjectManager принимает те же опции, что и кластеризатор.
        clusterDisableClickZoom: true
    });

    objectManager.objects.options.set('preset', 'islands#blackDotIcon');
    objectManager.clusters.options.set('preset', 'islands#blackClusterIcons');
    mainMap.geoObjects.add(objectManager);

    create_points_on_map();
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

//создание точек на карте
function create_points_on_map(){
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

//установка активного тура
function set_active_tour(tour_id, points_id_array){
    remove_active_tour(); //убираем следы прыдудщего активного тура
    points_set_active(points_id_array); //подсвечиваем точки, которые соотвествуют активному туру
}

//удаление активного тура
function remove_active_tour() {
    all_points_set_default();
}

//сделать точки и кластеры с этими точками активными
function points_set_active(points_id_array) {
    points_id_array.forEach(function (point_id) {
        objectManager.objects.setObjectOptions(point_id, {
            preset: 'islands#blueDotIcon'
        });
    })

    objectManager.clusters.getAll().forEach(function (cluster) {
        cluster.properties.geoObjects.forEach(function (object) {
            if(object.id in points_id_array){
                objectManager.clusters.setClusterOptions(cluster.id, {
                    preset: 'islands#blueClusterIcons'
                });
            }
        })
    })
}

//устанавливает все точки и кластеры в дефолтное состояние
function all_points_set_default() {
    objectManager.clusters.getAll().forEach(function (cluster) {
        objectManager.clusters.setClusterOptions(cluster.id, {
            preset: 'islands#blackClusterIcons'
        });
    })

    objectManager.objects.getAll().forEach(function (objects) {
        objectManager.objects.setObjectOptions(objects.id, {
            preset: 'islands#blackDotIcon'
        });
    })
}

/*
* Блок обработки кнопок и действий на странице
* */

let $tour = $(".wrap");

//получает из блока экскурсии массив из id точек на карте
function block_to_points_array($tour) {
    let int_array = [];

    let points_str_array = $tour.data("points").split(";");
    points_str_array.forEach(function (value) {
        if(value) int_array.push(parseInt(value));
    })

    return int_array;
}

//при наведении на экскурсию
$tour.mouseenter(function() {
    let tour_id = parseInt($(this).data("tour_id"));
    let points_id_array = block_to_points_array($(this));

    set_active_tour(tour_id, points_id_array); //устанавливаем активный тур
})

$("body").css("overflow", "hidden")

let mobile;

$(window).on('load', function () {
    if ($(this).width() <= 992) {
        mobile_tours();
        mobile = true;
    } else {
        mobile = false;
    }
})

let slider_settings = {
    loop: false,
    nav: false,
    dots: true,
    margin: 0,
    items: 1,
    mouseDrag: false,
    //onChanged: callback_mobile,
    //onInitialized: callback_mobile_initialized,
}

let $map_tours = $(".map_slider");

function mobile_tours() {
    console.log("Въезали")
    $map_tours.owlCarousel(slider_settings);
}
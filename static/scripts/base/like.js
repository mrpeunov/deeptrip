$(document).ready(function() {
    let $tour_like = $('.preview_like');
    let $like_on_tour_page = $('#like');
    let $like_img_on_tour_page = $("#like_img");

    function like_clicked($elem){
        //клик по блоку с сердечком $elem

        //получаем список уже стоящих лайков
        let likes = JSON.parse(getCookie('likes'));
        let list = likes.list;

        //id экскурсии, которой поставили лайк
        let tour_id = Number($elem.data("tour_id"));
        console.log(tour_id);

        //проверяем, был ли блок лайкнут до этого
        if($elem.hasClass("liked")){
            //если был лайкнут
            list.forEach(function (value, i){
                if(tour_id === value){
                    list.splice(i, 1);
                }
            });
        } else{
            //если не был лайкнут, добавим номер в список
            list.push(tour_id);
        }

        //обновляем cookies
        likes.list = list
        setCookie('likes', JSON.stringify(likes));

        //изменим отображение
        $elem.toggleClass("liked");

        //ставим точку в меню
        console.log(list.length);
        if(list.length !== 0) $('#favorites').addClass('circle');
        else $('#favorites').removeClass('circle');
    }

    $tour_like.click(function(){
        like_clicked($(this));
    })

    $like_on_tour_page.click(function (){
        like_clicked($like_img_on_tour_page);
    })

    function init(){
        //инииализируем лайки

        //получаем уже стоящие лайки
        let likes = getCookie('likes');

        if(likes === undefined){
            //если записи в cookie не обнаружено

            //создаём запись
            likes = {list: []};
            setCookie('likes', JSON.stringify(likes));
        } else {
            //если уже есть запись в cookie

            //получаем значения
            likes = JSON.parse(likes);
            let list = likes.list;

            //добавляем отображение лайков
            $tour_like.each( function (){
                let $current_tour = $(this);
                let current_tour_id = $(this).data("tour_id");

                list.forEach(function (value){
                    if(current_tour_id === value){
                        $current_tour.addClass("liked")
                    }
                });
            });

            list.forEach(function (value){
                if($like_img_on_tour_page.data("tour_id") === value){
                    $like_img_on_tour_page.addClass("liked")
                }
            })

            //ставим точку в меню
            if(list.length !== 0) $('#favorites').addClass('circle');
        }
    }

    init();
});
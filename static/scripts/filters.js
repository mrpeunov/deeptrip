$(document).ready(function(){
    let $filter_count = $('#filter_count');
    let $filter_item = $('.filter_item');
    let $filters_show = $('#filters_show');

    function update_count(){
        //получаем список отмеченных
        let checked_array = [];

        $('.filter_item:checked').each(function(){
            checked_array.push($(this).attr('value'));
        });

        if(checked_array.length === 0){
            //если список пустой устанавлием максимальное значение

            $filter_count.html('Выберите фильтр');
            $filters_show.addClass('not_active');
        } else {
            //если не пустой
            let city_slug = $('#tours').data('city');

            //делаем ajax запрос на сервер
            $.ajax({
                url: '/api/v1/get_count_tours_for_filter_list/',
                method: 'GET',
                data: {
                    'checked_array': checked_array,
                    'city_slug': city_slug,
                },
                success: function(data) {
                    //обновляем количество
                    $filter_count.html('Найдено ' + data + ' экскурсий');

                    if(parseInt(data, 10) !== 0){
                        $filters_show.removeClass('not_active');
                    }

                },
                error: function(data) {
                    console.log("Error " + data);
                }
            });
        }
    }

    //изменение экрана
    $(window).resize(function(){
        $filter_item.prop('checked', false);
        update_count();
    });

    $filter_item.click(function (){
        update_count();
    })

    //обработаем клик по показать
    $filters_show.click(function(e){

        //по неактивной кнопке не переходит
        if($filters_show.hasClass('not_active')){
            e.preventDefault()
        }
    });
})
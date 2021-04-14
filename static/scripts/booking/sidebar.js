$(document).ready(function() {
    let $window = $(window);

    $window.on('load resize', function () {
        set_sidebar();
        update_width_block($(".booking_sidebar"), $(".booking_sidebar_block"));
    })

    //обновление ширины блока при обновлении
    function update_width_block($parent, $children) {
        $children.css('width', $parent.outerWidth());
    }

    // пробная версия функции для всех сайдбаров
    function set_sidebar($parent, $children, min_width) {
        $window.scroll(function () {
            if ($window.width() >= min_width) {
                //фиксирование на старте
                if ($parent.offset().top < $window.scrollTop()) {
                    $children.addClass("fixed")
                    update_width_block($parent, $children);
                } else {
                    $children.removeClass('fixed');
                }

                //сброс фиксирования на финише
                let finish = $window.scrollTop() + $children.height()
                if ($parent.position().top + $parent.height() <= finish) {
                    $children.addClass('fixed_bottom');
                } else {
                    $children.removeClass('fixed_bottom');
                }
            }
        });
    }

    set_sidebar($(".booking_sidebar"), $(".booking_sidebar_block"), 700);
})
$(function() {
    let $menu_popup = $('.menu_items');
    let $container = $('.container');


    function open_or_close(){
        $(".menu_button").toggleClass('menu_button_active')

		$menu_popup.slideToggle(300, function(){
			$menu_popup.toggleClass('menu_items_active');
		    $container.toggleClass('body_pointer');
		});
    }
	//обработаем нажатие на открытие/закрытие
	$(".menu_button").click(function(){
	    open_or_close();
	});

	//обработаем клик по body
    $(".container", "footer").click(function (){
        if ($container.hasClass('body_pointer')){
            open_or_close();
		}
    })


	$(window).resize(function() {
	    if(window.innerWidth > 768){
	        $menu_popup.css( "display", "flex");
        } else{
	        $menu_popup.css( "display", "none");
        }
    });
});
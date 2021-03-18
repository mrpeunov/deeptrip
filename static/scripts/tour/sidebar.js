let $window = $(window);
//фиксируемый блок
let calculate = $("#sidebar_calculate");
//блок родитель
let parent = $(".tour_sidebar");

$(document).ready(function(){
	$window.on('load resize', function () {
		if ($window.width() < 768) {
			//мобильная версия
			set_default();
		}
		else {
			//декстоп
			set_desktop();
		}
	})
})

function update_width(sidebar){
    let up = $(".tour_sidebar");
    let pl = parseInt(sidebar.css("padding-left"), 10);
    let pr = parseInt(sidebar.css("padding-right"), 10);
    sidebar.css('width', up.outerWidth() - pl - pr);
}

function set_default(){
	calculate.removeAttr('style');
	calculate.removeClass('fixed')
	calculate.removeClass('fixed_bottom')
}

function set_desktop(){
	let pt = parseInt(calculate.css("padding-top"), 10);
	let pb = parseInt(calculate.css("padding-bottom"), 10);
	let mt = parseInt(calculate.css("margin-top"), 10);
	let mb = parseInt(calculate.css("margin-bottom"), 10);

	let start = calculate.offset().top - pt;
	let finish = parent.position().top + parent.height();

	$window.scroll(function () {
		if($window.width() >= 768) {
			//фиксирование на старте
			if (start < $window.scrollTop()) {
				calculate.addClass('fixed');
				update_width(calculate);
				let right = $('.tour_content').css('padding-right');
				calculate.css('right', right)
			} else {
				calculate.removeClass('fixed');
			}

			//сброс фиксирования на финише
			if (finish < $window.scrollTop() + calculate.height() + pt + pb + mt + mb) {
				calculate.addClass('fixed_bottom');
				calculate.css("right", 0)
			} else {
				calculate.removeClass('fixed_bottom');
			}
		}
	});
}

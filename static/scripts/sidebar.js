//$(document).ready(function(){
//    $("#sidebar_calculate").sticky({topSpacing:25});
//});

function update_width(sidebar){
    let up = $('.tour_sidebar_information');
    let pl = parseInt(up.css("padding-left"), 10);
    let pr = parseInt(up.css("padding-right"), 10);

    sidebar.css('width', up.outerWidth() - pl - pr);
}

$(function(){
    //фиксируемый блок
	let calculate = $("#sidebar_calculate");

	let pt = parseInt(calculate.css("padding-top"), 10);
	let pb = parseInt(calculate.css("padding-bottom"), 10);
	let mt = parseInt(calculate.css("margin-top"), 10);
	let mb = parseInt(calculate.css("margin-bottom"), 10);

	//блок родитель
	let parent = $(".tour_sidebar");

	let $window = $(window);

	update_width(calculate);
    $window.resize(function (){
        update_width(calculate);
    })


	let start = calculate.offset().top;
	let finish = parent.position().top + parent.height();

	$window.scroll(function(){
	    //фиксирование на старте
		if (start < $window.scrollTop()) {
			calculate.addClass('tour_sidebar_calculate_fixed');
		} else {
			calculate.removeClass('tour_sidebar_calculate_fixed');
		}

		//сброс фиксирования на финише
		if(finish < $window.scrollTop() + calculate.height() + pt + pb + mt + mb){
		    calculate.addClass('tour_sidebar_calculate_bottom');
        } else {
		    calculate.removeClass('tour_sidebar_calculate_bottom');
        }
	});
});

update_calculate_price();

$(".standard_dropdown_choice").on('click', function () {
    let id = $(this).attr("id");

    let $choice = $("#" + id);
    let $list = $("#" +  id  + "_list");

    $list.toggleClass("none");
    $choice.toggleClass("underline");
    $choice.parent().toggleClass("standard_dropdown_wrap_active");
})

$(".standard_dropdown_list_item").on('click', function () {
    let choice_id = $(this).data("choice_id");
    let $choice = $("#" + choice_id);

    let text = $(this).html();

    $choice.html(text);
    $choice.trigger("click");
    $choice.attr("data-price", $(this).data("price"));

    update_calculate_price();
})

function update_calculate_price() {
    //расчёт в калькуляторе

    let rate = false;
    let children = false;
    let group = false;

    let rate_price = 0;
    let children_price = 0;
    let group_price = 0;

    $('.standard_dropdown_choice').each(function () {
        if($(this).data("type") === "rate"){
            rate = true;
            rate_price = parseFloat($(this).attr("data-price"));
        }

        if($(this).data("type") === "children"){
            children = true;
            children_price = parseFloat($(this).attr("data-price"));
        }

        if($(this).data("type") === "group") {
            group = true;
            group_price = parseFloat($(this).attr("data-price"));
        }
    })

    let result_price = 0;

    if (rate && (group || children)){
        result_price = rate_price * group_price + rate_price * children_price;
    }

    if (!rate && group && children){
        result_price = group_price + children_price;
    }

    if (rate && !group && !children){
        result_price = rate_price;
    }

    if (!rate && group && !children){
        result_price = group_price;
    }

    if (!rate && !group && children){
        result_price = children_price;
    }

    $('#calculate_price').html(result_price);

}

update_calculate_price();

$(".standard_dropdown_choice").on('click', function () {
    let id = $(this).attr("id");
    let $choice = $("#" + id);
    let $list = $("#" +  id  + "_list");

    //если по открытому кликают закрыть
    if($choice.hasClass("underline")){
        close_dropdown($choice, $list)
    } else{
        $(".standard_dropdown_choice").each(function () {
            close_dropdown($(this), $(this).next());
        })
        open_dropdown($choice, $list)
    }
})

function open_dropdown($choice, $list) {
    $list.removeClass("none");
    $choice.addClass("underline");
    $choice.parent().addClass("standard_dropdown_wrap_active");
}

function close_dropdown($choice, $list) {
    $list.addClass("none");
    $choice.removeClass("underline");
    $choice.parent().removeClass("standard_dropdown_wrap_active");
}


$(".standard_dropdown_list_item").on('click', function () {
    let choice_id = $(this).data("choice_id");
    let $choice = $("#" + choice_id);
    let $mobile_choice = $("#m_" + choice_id);

    let text = $(this).html();

    $choice.html(text);
    $mobile_choice.html(text);

    close_dropdown($choice, $choice.next())
    close_dropdown($mobile_choice, $mobile_choice.next())

    $mobile_choice.attr("data-price", $(this).data("price"));
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
            rate_price = parseFloat($(this).attr("data-price").replace(',', '.'));
        }

        if($(this).data("type") === "children"){
            children = true;
            children_price = parseFloat($(this).attr("data-price").replace(',', '.'));
        }

        if($(this).data("type") === "group") {
            group = true;
            group_price = parseFloat($(this).attr("data-price").replace(',', '.'));
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

    console.log("nnnn");

    $('.calculate_price').html(result_price);

}
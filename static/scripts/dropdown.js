
$(".standard_dropdown_choice").on('click', function () {
    let id = $(this).attr("id");

    let $choice = $("#" + id);
    let $list = $("#" +  id  + "_list");
    

    $list.toggleClass("none");
    $choice.toggleClass("underline");
})

$(".standard_dropdown_list_item").on('click', function () {
    let choice_id = $(this).data("choice_id");
    let $choice = $("#" + choice_id);

    let text = $(this).html();

    $choice.html(text);
    $choice.trigger("click");
})
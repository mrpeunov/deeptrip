function show_text(){
    let $text = $("#all_text")
    let $button = $("#show_text_button");

    if($text.css("display") === "none"){
        $button.html("Скрыть");
    }
    else{
        $button.html("Показать полностью");
    }

    $text.slideToggle(300);
}
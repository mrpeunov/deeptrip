function show_text(){
    let $text = $("#all_text")
    let $button = $("#show_text_button");
    if($text.css("display") === "none"){
        $text.css("display", "block");
        $button.html("Скрыть текст");
    }
    else{
        $text.css("display", "none");
        $button.html("Показать текст");
    }
}
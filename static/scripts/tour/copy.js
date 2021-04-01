$(document).ready(function() {
    $('#copy').on('click', function () {
        //копирование ссылки в буфер обмена
        let text = document.createElement('input');

        //берём текущую ссылку
        text.value = window.location.href;
        document.body.appendChild(text);
        text.select();
        document.execCommand('copy');
        document.body.removeChild(text);
    })
})
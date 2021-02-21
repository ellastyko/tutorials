/* В данном коде показаны базовые обращение к элементам страницы */
/* Также показаны основные события в jQuery (click, dbclick, hover  и т.д.)*/

/*  When all elements of page will be downloaded 
   functions in .ready() can be used */ 
$(document).ready(function () {

    /* Обращение к селекторам */
    $('h2').click(function() { //  By teg
        // Событие сработало
        alert("Ты кликнул на первую строку!");
    });
    $('.header-style').dblclick(function() { //  By class
        
        alert("Ты дважды кликнул на меня!");
    });
    $('#header').mouseup(function() { //  By id
        
        alert("Ты отпустил кнопку!");
    });
    $('h4').hover(function() { // 
        // При наведении мы задаем красный цвет для текста
        if ($(this).css("color") == "rgb(0, 0, 0)")     
            $(this).css({"color": "red"});
        else
            $(this).css({"color": "black"});
            
    });

    /* Больше видов обращения к элементам можна найти тут:
        https://basicweb.ru/jquery/jquery_selectors.php
       
       Виды событий: 
        https://basicweb.ru/jquery/jquery_events.php
    */
});
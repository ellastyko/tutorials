
/* Перед разбором кода этого урока рекомендуется ознакомиться с Ajax */
$(document).ready(function () {

    // If you press on 'sign in'
    $('form').submit(function(e) { 

      e.preventDefault(); // Page won`t reload untill code will be executed

      // Copy our values into object   
      var form = {
        login: $("[name='login']").val(), 
        password: $("[name='password']").val(),
        name: $("[name='name']").val(),
        status: $("[name='status']").val(),
      }
      form = JSON.stringify(form); // Конвертируем объект в JSON

      /* Здесь запрос отправится на cgi скрипт в котором будет обработан */
      $.ajax({
          url: '../cgi-bin/script.py', // строка, содержащая URL адрес, на который отправляется запрос
          type: 'POST',
          dataType: 'text', // Формат возвращаемых данных
          cache: false,    // Кеширование результатов
          contentType: 'application/json; charset=utf-8', // Формат вносимых данных
          data: form, //данные, которые будут отправлены на сервер
  
          success: function(data) { // Запрос успешен. Data - ответ сервера
            console.log(data);
          },
          error: function(xhr, data) {
            alert("Error");
          }
      });
    });
  
  
});

/* xhttp запросы расматриваются только в JS tutorial */
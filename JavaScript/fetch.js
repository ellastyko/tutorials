
window.addEventListener('load', (event) => {
    
    let response = await fetch(url);

    if (response.ok)        // если HTTP-статус в диапазоне 200-299                     
        let json = await response.json();  // получаем тело ответа (см. про этот метод ниже)
    else 
        alert("Ошибка HTTP: " + response.status);

    // https://learn.javascript.ru/fetch
});
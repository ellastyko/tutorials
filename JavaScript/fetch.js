
window.addEventListener('load', (event) => {
    
    let response = await fetch(url);

    if (response.ok) { // если HTTP-статус в диапазоне 200-299
    // получаем тело ответа (см. про этот метод ниже)
    let json = await response.json();
    } else {
    alert("Ошибка HTTP: " + response.status);
    }
    // https://learn.javascript.ru/fetch
});
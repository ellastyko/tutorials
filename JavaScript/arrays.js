arr = []
list = [1, 2, 3, 4]

arr.unshift(2); // Добавить в начало 
arr.push(1); // Добавить в конец 

arr.shift(); // Удалить первый элемент
arr.pop(); // Удалить последний элемент

arr.length; 

arr = arr.concat(list) // Возвращает объедененный список [1, 2, 3, 4, "a", "b", "c", "d"]
// Better use spread operator (advanced.js)



/* Более сложные */

arr.forEach( (value, index) => {
    return arr[index] = value++
}); // Функция вызывается для каждого элемента (Return undef.)


arr = arr.map(elem => {
    return elem++
}); // Функция вызывается для каждого элемента


arr.find(test); // Возвращает первый элемент который окажется валидным (определяется это в функции)
arr.findIndex(test); // Возвращает индекс первого элемента который окажется валидным (определяется это в функции)


arr.filter(test); // Возвращает список с только валидными элементами (определяется это в функции)
arr.every(test); // Возвращает true если все элементы валидны
arr.fill("*"); // Заполняет список *


// Функции 

function test(value) {
    if (typeof(value) === 'string') 
        return value;
}


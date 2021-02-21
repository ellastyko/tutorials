arr = []
list = [1, 2, 3, 4]
mass = ['a', 'b', 'c', 'd']

arr.push(1); // Добавить в конец 1
arr.unshift(2); // Добавить в начало 2

arr.pop(); // Удалить последний элемент
arr.shift(); // Удалить первый элемент

arr.length; 

arr = arr.concat(list) // Возвращает объедененный список [1, 2, 3, 4, "a", "b", "c", "d"]

/* Более сложные */
arr.forEach(inc); // Функция вызывается для каждого элемента (Return undef.)
arr = arr.map(inc); // Функция вызывается для каждого элемента
arr.find(test); // Возвращает первый элемент который окажется валидным (определяется это в функции)
arr.findIndex(test); // Возвращает индекс первого элемента который окажется валидным (определяется это в функции)
arr.filter(test); // Возвращает список с только валидными элементами (определяется это в функции)
arr.every(test); // Возвращает true если все элементы валидны
arr.fill("*"); // Заполняет список *


// Функции 
function func(value) {
    console.log(`forEach ${value}\n`);
}

function test(value) {
    if (typeof(value) === 'string') 
        return value;
}

function inc(value) {
    
    return value+=5;
}
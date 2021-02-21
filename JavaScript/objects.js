obj = {
    name: 'Vadik',
    surname: 'Sergeev',
    id: 1337
};
console.log(obj);

console.log(obj.name, obj.surname, obj.id)

obj.age = 50; // Добавляем новое поле



Json_obj = JSON.stringify(obj); // Конвертируем в Json
console.log(Json_obj);

new_obj = JSON.parse(Json_obj); // Конвертируем в объект
console.log(new_obj);
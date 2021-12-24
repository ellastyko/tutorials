/* ###  How to print text ### */

document.write("some text") // On html page
console.log("some text");   // In console

alert("some text");     // In notification
prompt("How old are you", 100); // Notification with ability to input something
confirm("We sended you a message") // User should to confirm in notification

/* ### How to create variables ### */

var a = 5;
let b = 'text';
const c = 'text';

/* Const example */
const d = 6;
// a = 8; // Ошибка
const f = [];
// b = ["hello"]; // Ошибка
f.push(1); // OK
console.log(f) // [1]


/* short variant */
var h = 5, i = 't';

/* Если var обьявить в цикле(цикл внутри функции) переменная будет видна во всей функции. 
   В свою очередь let будет видна только внутри цикла. */



/* ###  Types of data  ### */

typeof 35; // number
typeof "text"; // string
typeof true; // boolean
typeof [1, 2, 3]; // object
typeof null; // object
typeof undefined; // undefined
typeof NaN; // number



/* ### How to print variable ### */

var user = 'Vadim';

console.log(`Your name ${user}`)
// OR
console.log(`Your name ` + user)

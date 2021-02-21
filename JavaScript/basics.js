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

/* short variant */
var f = 5, g = 't';

/* Если var обьявить в цикле(цикл внутри функции) переменная будет видна во всей функции. 
   В свою очередь let будет видна только внутри цикла, как и в С++. */



/* ###  Types of data  ### */

typeof 35; // number
typeof "text"; // string
typeof true; // boolean
typeof [1, 2, 3]; // object
typeof null; // object
typeof undefined; // undefined



/* ### How to print variable ### */

var user = 'Vadim';

console.log(`Your name ${user}`)
// OR
console.log(`Your name ` + user)


var x = 0;
var list = ['a', 'b', 'c', 'd', 'e']


while(true) {

    if (x > 5) {
        break;
    }
    x++;
}



for (let i = 0; i < list.length; i++) {
    console.log(list[i]); // a b c d e
}

for (let i in list) {
    console.log(i); // 0 1 2 3 4
}

for (let i of list) { // Цикл for of аналогичен for in в python
    console.log(i); // a b c d e
}

var x = 0;
var list = ['a', 'b', 'c', 'd', 'e']


/* While cycles */
while(true) {

    if (x > 5) {
        break;
    }
    x++;
}

do {
    x++;
} while (x < 10)



/* For cycles */

for (let i = 0; i < list.length; i++) {
    console.log(list[i]); // a b c d e
}

for (let i in list) {
    console.log(i); // 0 1 2 3 4
}

for (let i of list) { 
    console.log(i); // a b c d e
}
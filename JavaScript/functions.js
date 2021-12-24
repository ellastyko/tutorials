
/* Functions and its variants */

function func(a) {
    console.log("standart");
}

const f = (a, b) => {
    console.log("un standart");
}

func(4);
f(5, 6);




let value = 10  

// if func has no brackets don't use return 
const getter = () => value 

getter() // 10

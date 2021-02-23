
// class parent {
//     constructor(name = 'pavel', surname = 'durov') {
//         this.name = name;
//         this.surname = surname;
//         alert(`Hello ${this.name} ${this.surname}`);
//     }
// }


// class child extends parent {
    
//     constructor(id = 0) {
//         alert(`Hello ${this.name} ${this.surname} ${id}`);
//     }
// }

// var x = new child();

var glo;

let a = {
    name: 'vad',
    age: 18,
}

glo = a;

delete a;
// glo = null;

console.log(typeof(glo));
console.log(glo)

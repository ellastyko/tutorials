const log = console.log


class Parent {

    constructor(name = 'pavel', surname = 'durov') {
        this.name = name;
        this.surname = surname;
        log(`Parent: ${this.name} ${this.surname}`);
    }
}


class Child extends Parent {
    
    constructor(age = 1) {
        super();
        this.age = age
        log(`Child: ${this.name} ${this.surname} ${this.age}`);
    }

    getAge = () => this.age



}

var chld = new Child(3);
log(chld.getAge())

// var glo;

// let a = {
//     name: 'vad',
//     age: 18,
// }

// glo = a;


// console.log(typeof(glo));
// console.log(glo)

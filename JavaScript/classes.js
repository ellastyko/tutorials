
class example {
    
    constructor(name = 'pavel', surname = 'durov') {
        this.name = name;
        this.surname = surname;
        alert(`Hello ${name} ${surname}`);
    }
    sayHi() {
        alert("Func!");
    }
}

var x = new example();
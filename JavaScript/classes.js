// REDO
class parent {
    constructor(name = 'pavel', surname = 'durov') {
        this.name = name;
        this.surname = surname;
        alert(`Hello ${this.name} ${this.surname}`);
    }
}


class child extends parent {
    
    constructor(id = 0) {
        alert(`Hello ${this.name} ${this.surname} ${id}`);
    }
}

var x = new child();

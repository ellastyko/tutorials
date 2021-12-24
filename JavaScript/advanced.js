
/* Destructurisation */

    /* functions */
    // easy
    function calc(a, b) {
        return [
            a + b,
            a - b
        ]
    }

    const [sum, sub] = calc(30, 20)

    // hard
    function calc2(a, b) {
        return [
            a + b,
            a - b,
            a * b,
            a / b,
            a ** b
        ]
    }

    const [summ,, multple, ...others] = calc2(30, 20)

    /* objects */
    const person = {
        name: 'Josh',
        surname: 'Pierce'
    }

    const { name, surname : srnm } = person

    // console.log(name, srnm) 

    function logPerson( { name, surname } ) {
        console.log(name, surname)
    }

    logPerson(person)



    /* Spread opearator */
    const cities = ['Moskow', 'Kyiv', 'Minsk']

    console.log(...cities) // 'Moskow Kyiv Minsk'

    const temp = [...cities] // Copy array in temp 

    function spread(a, b, c) {
        console.log(a, b, c) // 'Moskow' 'Kyiv' 'Minsk'
    }

    spread(...cities)

    
    /* Rest operator */

    function rest(a = 0, ...rest) {
        console.log(rest) // [2, 3, 4]
    }

    rest(1, 2, 3, 4)






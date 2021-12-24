
const url = `https://eonet.gsfc.nasa.gov/api/v2.1/events`

/*    1 variant    */
async function func1() {
    
    let promise = await fetch(url)

    return await promise.json()
}

/*    2 variant    */
function func2() {
    
    fetch(url)
    .then(response => response.json())
    .then(result => console.log(result))
}

func1()
// func2()

// https://learn.javascript.ru/fetch

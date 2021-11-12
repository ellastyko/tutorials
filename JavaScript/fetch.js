
const url = `https://jsonplaceholder.typicode.com/posts`

/*    1 variant    */
async function func1() {
    
    let promise = await fetch(url)

    console.log(await promise.json())
}

/*    2 variant    */
function func2() {
    
    fetch(url)
    .then(response => response.json())
    .then(result => console.log(result))
}

// func1()
// func2()

// https://learn.javascript.ru/fetch

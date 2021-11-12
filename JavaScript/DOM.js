
window.addEventListener('load', (event) => {
    
    
    document.addEventListener("click", function() {

        var text = document.getElementById("txt").value;
        console.log(text);
        document.getElementById("txt").innerHTML = "Hello World";
        
    });
});



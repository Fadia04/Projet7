
function getInputValue(){
    var inputVal = document.getElementById("myInput").value;
    var user_data = {
        question: inputVal
    }
    console.log(user_data)
    fetch("/question", {
        method: "POST",
        body: JSON.stringify(user_data)
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        console.log(data)
    });
}
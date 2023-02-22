function iha_delete(id) {
    let getID = document.getElementById(id);
    if (!getID)
        return;
    
    let csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    let xhr = new XMLHttpRequest();
    let formData = new FormData();

    // post işleminde gönderilecek id değeri
    formData.append("id", id);

    xhr.open("POST", "/delete");
    xhr.setRequestHeader("X-CSRFToken", csrf_token);
    
    // POST işleminden dönüş alınca burayı uygular
    xhr.onload = function() {
        // sunucudan dönen istek true ise elementi siler
        if (JSON.parse(xhr.response)["Message"] == true)
            getID.remove()
        else
            alert("Silinemedi.");
    };
    xhr.send(formData);
}

// butona tıklanmasını dinler
document.getElementById("delete").addEventListener("click", iha_delete);

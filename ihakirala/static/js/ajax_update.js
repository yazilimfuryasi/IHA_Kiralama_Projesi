function iha_update(id) {
    let getID = document.getElementById(id);
    if (!getID)
        return;
    let input = getID.querySelectorAll("input");
    if (!input)
        return;
    let kategori = getID.querySelector("select");
    let csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    let xhr = new XMLHttpRequest();
    let formData = new FormData();

    // birden fazla alert etiketi basmaması için koşul
    const alertLength = document.getElementsByClassName("alert");
        if (alertLength && alertLength.length > 0)
            alertLength[0].remove();

    // alert için oluşturulacak child elementi
    let durumElement = document.getElementById("durum");

    // veritabanına kayıt edilirken bekleme topacı
    let spinner = document.createElement("div")
    spinner.classList.add("spinner-border");
    durumElement.appendChild(spinner);

    let alert = document.createElement("div");

    // post işleminde gönderilecek değerler
    formData.append("id", id);
    formData.append("marka", input[0].value);
    formData.append("model", input[1].value);
    formData.append("weight", input[2].value);
    formData.append("flight_time", input[3].value);
    formData.append("kategori", kategori.value);

    xhr.open("POST", "/update");
    xhr.setRequestHeader("X-CSRFToken", csrf_token);

    // POST işleminden dönüş alınca burayı uygular
    xhr.onload = function() {
        spinner.remove()
        
        alert.classList.add("alert", "alert-primary");
        alert.id = "alert";
        if (JSON.parse(xhr.response)["Message"] == true)
                alert.textContent = "Başarıyla Kayıt Edildi";
        else
            alert.textContent = "Kayıt Edilemedi! Tekrar Dene";
        durumElement.appendChild(alert);
    };
    xhr.send(formData);

    // alert elementini 3 saniye ekranda tutar
    setTimeout(function(){
        alert.remove();
   },3000);
}

// butona tıklanmasını dinler
document.getElementById("update").addEventListener("click", iha_update);

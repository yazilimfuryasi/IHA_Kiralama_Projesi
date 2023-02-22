function iha_add() {
    // inputlar
    let marka = document.getElementById("id_marka");
    let model = document.getElementById("id_model");
    let weight = document.getElementById("id_weight");
    let flight_time = document.getElementById("id_flight_time");
    let kategori = document.getElementById("kategori")
    
    // birden fazla alert etiketi basmaması için koşul
    const alertLength = document.getElementsByClassName("alert");
        if (alertLength && alertLength.length > 0)
            alertLength[0].remove();

    // alert için oluşturulacak child elementi
    let durumElement = document.getElementById("durum");

    // alert için yeni div
    let alert = document.createElement("div");

    // tüm inputların doluluğu kontrol edilir
    if (marka.value && model.value && weight.value && flight_time.value){
        let csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        let xhr = new XMLHttpRequest();
        let formData = new FormData();

        // veritabanına kayıt edilirken bekleme topacı
        let spinner = document.createElement("div")
        spinner.classList.add("spinner-border");
        durumElement.appendChild(spinner);

        // post işleminde gönderilecek değerler
        formData.append("marka", marka.value);
        formData.append("model", model.value);
        formData.append("weight", weight.value);
        formData.append("flight_time", flight_time.value);
        formData.append("kategori", kategori.value);

        xhr.open("POST", "/add");
        xhr.setRequestHeader("X-CSRFToken", csrf_token);
        // POST işleminden dönüş alınca burayı uygular
        xhr.onload = function() {
            spinner.remove()
            marka.value = "";
            model.value = "";
            weight.value = "";
            flight_time.value = "";
            
            alert.classList.add("alert", "alert-primary");
            alert.id = "alert";
            if (JSON.parse(xhr.response)["Message"] == true)
                alert.textContent = "Başarıyla Kayıt Edildi";
            else
                alert.textContent = "Kayıt Edilemedi! Tekrar Dene";
            durumElement.appendChild(alert);
        };
        xhr.send(formData);
    }
    // boş bırakılan input olursa else düşer ve bootstrap alert sınıfı uygulanır
    else {
        alert.classList.add("alert", "alert-primary");
        alert.id = "alert";
        alert.textContent = "Lütfen Tüm Alanları Doldur";
        durumElement.appendChild(alert);
    }
}

// butona tıklanmasını dinler
document.getElementById("add").addEventListener("click", iha_add);

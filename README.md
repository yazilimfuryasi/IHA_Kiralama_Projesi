### 📖 İçindekiler
- [🛠 Hangi Teknolojiler Kullanıldı?](#-hangi-teknolojiler-kullanıldı)
- [🐳 Docker ile Çalıştırma](#-docker-ile-çalıştırma)
- [📸 Ekran Görüntüleri](#-ekran-görüntüleri)
_____
### 🛠 Hangi Teknolojiler Kullanıldı?
- Back end
    * Python
    * Django
    * Django-Rest Framework
    * JavaScript, Ajax
    * Docker
- Frond end
    * Şablon: https://kariyer.baykartech.com/
    * CSS / HTML
    * Bootstrap
- Veritabanı 
    * PostgreSql (Kategoriler, İHA)

- Fonksiyonlar
    * Kayıt, Giriş Formu
    * İHA Kayıt Sayfası (Marka, Model, Ağırlık, Uçuş Süresi, Kategori) (AJAX ile)
    * İHA Listeleme, Arama, Sıralama (API, AJAX ile)
    * İHA Güncelleme, Silme (AJAX ile)
_____
### 🐳 Docker ile Çalıştırma

✔ Environment Aktif Edin
<pre>source env/Scripts/activate</pre>

✔ Docker'ı Build Edip Çalıştırın
<pre>docker-compose up -d --build</pre>

✔ İki Servisinde Sorunsuz Şekilde Çalışması Gerekiyor
<pre>
[+] Running 2/2
    - Container postgres_db    Started
    - Container django_container  Started
</pre>

✔ Aşağıdaki Adrese Gidildiğinde Giriş Ekranı ile Karşılaşacaksınız
<pre>http://localhost:8000/</pre>

✔ Veritabanını Taşıyalım
<pre>docker-compose run app python3 manage.py makemigrations</pre>

<pre>docker-compose run app python3 manage.py migrate</pre>

✔ Superuser Oluşturun
<pre>docker-compose run app python3 manage.py createsuperuser</pre>

✔ Kullanıcı Oluşturduktan Sonra Admin Paneline Gidilip Kategori Ekleyin
<pre>http://localhost:8000/admin</pre>
_____
### 📸 Ekran Görüntüleri

📌 <b>Giriş</b>
_____
![login](https://user-images.githubusercontent.com/84662757/220663143-4e80e498-781f-4c55-9220-dd036f9aac0f.png)
_____
📌 <b>Kayıt</b>
_____
![kayıt](https://user-images.githubusercontent.com/84662757/220663228-096c5716-8fe3-4dfb-aa49-9940cd5852b4.png)
_____
📌 <b>Dashboard</b>
_____
![dashboard](https://user-images.githubusercontent.com/84662757/220707214-185cc271-f186-4359-a97f-73daa8e5325f.png)
_____
📌 <b>İHA Kayıt</b>
_____
![kayıt et](https://user-images.githubusercontent.com/84662757/220707695-2f9a9a7f-89da-4056-b49e-5b8402607958.png)
_____
📌 <b>İHA Listesi</b>
_____
![listele](https://user-images.githubusercontent.com/84662757/220706692-1b5d8607-b0cd-4678-95e4-b705ce6b123b.png)
_____
📌 <b>İHA Güncelleme, Silme</b>
_____
![güncelle](https://user-images.githubusercontent.com/84662757/220707393-993519f2-db25-4125-9cc6-638256ec6cc5.png)
_____
📌 <b>İHA Sabit Kanat Filtresi</b>
_____
![sabitkanat](https://user-images.githubusercontent.com/84662757/220706621-e6ec93a5-a2ac-403d-b94e-5f37685c15b0.png)
_____
📌 <b>Arama Çubuğu</b>
_____
![arama](https://user-images.githubusercontent.com/84662757/220706646-87739a7d-f269-41c8-a178-d910d24d8f2f.png)
_____

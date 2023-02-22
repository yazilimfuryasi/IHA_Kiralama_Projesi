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
![dashboard](https://user-images.githubusercontent.com/84662757/220663243-bf371caf-374c-4e38-9eb8-71e8f20d50ae.png)

_____
📌 <b>İHA Kayıt</b>
_____
![iha_kayıt](https://user-images.githubusercontent.com/84662757/220663154-3c24177e-45bc-4419-9be1-a77f7f079522.png)

_____
📌 <b>İHA Listesi</b>
_____
![liste](https://user-images.githubusercontent.com/84662757/220700557-e64824f2-8c7a-404f-8587-d73356e55e2d.png)

_____
📌 <b>İHA Güncelleme, Silme</b>
_____
![ihalar](https://user-images.githubusercontent.com/84662757/220663293-927299af-3701-4443-8f2a-21d269f9bc35.png)

_____
📌 <b>İHA Sabit Kanat Filtresi</b>
_____
![sabit kanat filtre](https://user-images.githubusercontent.com/84662757/220700616-260e35b8-a4d1-479a-a47c-149b8c17a7cf.png)

_____
📌 <b>Arama Çubuğu</b>
_____
![arama](https://user-images.githubusercontent.com/84662757/220700671-15ab9e74-742f-41b2-b391-7a05b900e819.png)
_____

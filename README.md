## İçindekiler
- [Neler Kullanıldı?](#neler-kullanıldı)
- [Docker ile Çalıştırma](#docker-ile-çalıştırma)
- [Ekran Görüntüleri](#ekran-görüntüleri)

### Neler Kullanıldı?
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

### Docker ile Çalıştırma

Env aktif etme
<pre>source env/Scripts/activate</pre>

Dockeri build edip çalıştırma
<pre>docker-compose up -d --build</pre>

İki servis de sorunsuz çalışması gerekiyor.
<pre>
[+] Running 2/2
    - Container postgres_db    Started
    - Container django_container  Started
</pre>

Bu adrese gidilip giriş ekranı karşılamalı
<pre>http://localhost:8000/</pre>

Veritabanını taşıyalım
<pre>docker-compose run app python3 manage.py makemigrations</pre>

<pre>docker-compose run app python3 manage.py migrate</pre>

superuser oluşturulup admin panelinden kategori oluşturulması gerekiyor.
<pre>docker-compose run app python3 manage.py createsuperuser</pre>

Kullanıcı oluşturduktan sonra admin paneline gidilip kategoriler eklenir
<pre>http://localhost:8000/admin</pre>

### Ekran Görüntüleri
Giriş
![login](https://user-images.githubusercontent.com/84662757/220663143-4e80e498-781f-4c55-9220-dd036f9aac0f.png)

Kayıt
![kayıt](https://user-images.githubusercontent.com/84662757/220663228-096c5716-8fe3-4dfb-aa49-9940cd5852b4.png)

Dashboard
![dashboard](https://user-images.githubusercontent.com/84662757/220663243-bf371caf-374c-4e38-9eb8-71e8f20d50ae.png)

İHA Kayıt
![iha_kayıt](https://user-images.githubusercontent.com/84662757/220663154-3c24177e-45bc-4419-9be1-a77f7f079522.png)

İHA Listesi
![liste](https://user-images.githubusercontent.com/84662757/220663588-c2574309-c459-4b4e-8f74-1559de260362.png)

İHA Güncelleme, Silme
![ihalar](https://user-images.githubusercontent.com/84662757/220663293-927299af-3701-4443-8f2a-21d269f9bc35.png)

İHA Sabit Kanat Filtresi
![sabit kanat filtre](https://user-images.githubusercontent.com/84662757/220663654-ec4acb51-47a2-4369-9797-86e0cafc7f7f.png)

Kelime Araması
![arama](https://user-images.githubusercontent.com/84662757/220663672-d241b8dc-58ce-44eb-9866-d0f6214ff4fe.png)


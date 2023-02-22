from django.contrib.auth.models import User
from django.db import models

class KATEGORI(models.Model):
    kategori = models.CharField(max_length=140)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    # Veriyi kullanırken yazdırılacak örnek isim
    def __str__(self):
        return self.kategori

    # Admin Panelinde Görülecek İsim
    class Meta:
        verbose_name_plural = "Kategori"

class IHA(models.Model):
    marka = models.CharField(max_length=140)
    model = models.CharField(max_length=140)
    weight = models.DecimalField("Ağırlık", max_digits=12, decimal_places=0)
    flight_time = models.DecimalField("Uçuş Süresi", max_digits=12, decimal_places=0)
    kategori = models.ForeignKey(KATEGORI, on_delete=models.CASCADE)

    # Veriyi ekleyen kullanıcı ID'leri
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    # Veriyi kullanırken yazdırılacak örnek isim
    def __str__(self):
        return str(self.username.username)

    # Admin Panelinde Görülecek İsim
    class Meta:
        verbose_name_plural = "İHA"

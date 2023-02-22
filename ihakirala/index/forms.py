from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import IHA
from django import forms

# Kullanıcı Kayıt Formu
class KAYIT(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(KAYIT, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True
        if commit:
            user.save()
        return user

# İHA Kayıt Formu
class IHA_Form(ModelForm):
    class Meta:
        model = IHA
        fields = ("marka", "model", "weight", "flight_time", "kategori")

    def save(self, commit=True):
        user = super(IHA_Form, self).save(commit=False)
        if commit:
            user.save()
        return user

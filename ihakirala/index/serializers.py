from rest_framework import serializers
from .models import IHA

class IHA_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = '__all__'

    # Kategoriler ID olarak geldiği için ismiyle değiştirilir
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['kategori'] = instance.kategori.kategori
        return data

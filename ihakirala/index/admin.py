from django.contrib import admin
from .models import KATEGORI, IHA

class KategoriAdmin(admin.ModelAdmin):
    exclude = ("username",)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.username = request.user
        obj.save()

class IHA_Admin(admin.ModelAdmin):
    exclude = ("username",)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.username = request.user
        obj.save()

admin.site.register(KATEGORI, KategoriAdmin)
admin.site.register(IHA, IHA_Admin)

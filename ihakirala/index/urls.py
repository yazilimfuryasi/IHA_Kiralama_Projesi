from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.signin, name="login"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logoutPage, name="logout"),
    path('add', views.ADD_IHA, name="add"),
    path('update', views.UPDATE_IHA, name="update"),
    path('delete', views.DELETE_IHA, name="delete"),
    path('listele', views.listele, name="listele"),
    path('admin', admin.site.urls),
    path('search/', views.filter_search, name="search"),
    
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

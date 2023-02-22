from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import IHA_Form
from django.http import HttpResponse, JsonResponse
from .models import IHA, KATEGORI
from .serializers import IHA_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.apps import apps

@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")

# Veritabanından Kayıtlı İHA Silme
@login_required(login_url="login")
def DELETE_IHA(request):
    if request.method == "POST":
        iha = IHA.objects.filter(username_id=request.user.id, id=request.POST.get("id"))
        iha.delete()
        return JsonResponse({"Message": True})
    return JsonResponse({"Message": False})

# Kullanıcı verilerini buradan günceller
@login_required(login_url="login")
def UPDATE_IHA(request):
    if request.method == "POST":
        iha = IHA.objects.get(username_id=request.user.id, id=request.POST.get("id"))

        new = request.POST.copy()
        new.pop('id', None)
        new.pop('kategori', None)
        """
            is_valid doğrulaması yapabilmesi için gelen verilerin veritabanıyla eşleşebilmesi gerekiyor.
            Bu yüzden string olarak gelen kategori değerini id ile değiştiriyoruz. 
        """
        new.update({"kategori":KATEGORI.objects.get(kategori=request.POST.get("kategori")).id})
        
        form = IHA_Form(new, instance=iha)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.username_id = request.user.id
            form2.marka = new.get("marka")
            form2.model = new.get("model")
            form2.weight = new.get("weight")
            form2.flight_time = new.get("flight_time")
            form2.kategori_id = new.get("kategori")
            form2.save()
            return JsonResponse({"Message": True})
        return JsonResponse({"Message": False})

    DATA = {"ihalar": IHA.objects.filter(username_id=request.user.id),
            "kategoriler": KATEGORI.objects.all(),}
    return render(request, "update.html", DATA)

# Yeni İHA kayıt etme
@login_required(login_url="login")
def ADD_IHA(request):
    if request.method == "POST":
        new = request.POST.copy()
        new.pop('kategori', None)
        """
            is_valid doğrulaması yapabilmesi için gelen verilerin veritabanıyla eşleşebilmesi gerekiyor.
            Bu yüzden string olarak gelen kategori değerini id ile değiştiriyoruz. 
        """
        new.update({"kategori":KATEGORI.objects.get(kategori=request.POST.get("kategori")).id})

        form = IHA_Form(new)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.username_id = request.user.id
            form2.kategori_id = new.get("kategori")
            form2.save()
            return JsonResponse({"Message": True})
        return JsonResponse({"Message": False})

    DATA = {"kategoriler": KATEGORI.objects.all(),}
    return render(request, "add.html", DATA)

# Arama ve filtreleme için oluşturulan API
@api_view(['GET'])
def filter_search(request):
    flight_time = request.query_params.get('flight_time', None)
    kategoriName = request.query_params.get('Kategori', None)
    search = request.query_params.get('search', None)
    
    listele = IHA.objects.all()
    if search:
        # marka veya model olarak arama yapar
        listele = listele.filter(Q(marka__icontains=search) | Q(model__icontains=search))
    if kategoriName:
        listele = listele.filter(kategori__kategori=kategoriName)
    if flight_time:
        if flight_time == 'ascending':
            # Değeri küçükten büyüğe doğru sıralar
            listele = listele.all().order_by('-flight_time')
        elif flight_time == 'descending':
            # Değeri büyükten küçüğe doğru sıralar
            listele = listele.all().order_by('flight_time')
    if listele:
        serialized = IHA_Serializer(listele, many=True)
        return Response(serialized.data)
    else:
        return Response({})

# Kayıtlı tüm İHA'ları listeler
@login_required(login_url="login")
def listele(request):
    DATA = {"ihalar": IHA.objects.all(),
            "kategori": KATEGORI.objects.all()}
    return render(request, "list.html", DATA)

# Giriş yapma
def signin(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Username or Password Not Correct")
        return redirect(signin)
    return render(request, "login.html")

# Kayıt olma
def register(request):
    if request.user.is_authenticated: 
        return redirect(signin)

    if request.method == "POST":
        post = request.POST
        if post.get("password1") == post.get("password2") and post.get("username") and post.get("email"):
            username = post.get("username")
            password = post.get("password1")
            User.objects.create_user(username=username, email=post.get("email"), password=password)
            user = authenticate(username=username, password=password)
            login(request, user) # giriş yap
            return redirect(signin)
        return redirect("register")
    return render(request, "register.html")

# Oturumu sonlandırma
@login_required(login_url="login")
def logoutPage(request):
    logout(request)
    return redirect(signin)

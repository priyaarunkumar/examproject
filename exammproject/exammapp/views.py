from django.contrib import auth, messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from. models import Place
from django.contrib.auth.models import User
from .forms import PersonCreationForm
from .models import Person, City
from .form import PersonCreation
from .models import Quantity, Prize

# Create your views here.
def fun(request):
    return render(request,"category.html")


def details(request,id):

    obj=Place.objects.get(id=id)
    return render(request,"details.html",{'obj':obj})
def regi(request):




    if request.method == 'POST':


        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        con = request.POST['con']
        if password == con:


            user=User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('exammapp:deliver')
        else:
            messages.info(request,"pwd and confirm pwd are not same")





    return render(request,"regi.html")






def register(request):




    if request.method == 'POST':


        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        con = request.POST['con']
        if password==con:


             user=User.objects.create_user(username=username, password=password, email=email)
             user.save()
             return redirect('/')
        else:
            messages.info(request,"password nd confirm pwd are not same")






    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)

            return redirect('/')
        else:
            return redirect('exammapp:login')

    return render(request,"login.html")
def log(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('exammapp:deliver')
        else:
            return redirect('exammapp:log')
    return render(request,"log.html")
def deliver(request):
    return render(request,"delivery.html")
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exammapp:order')
    return render(request, 'home.html', {'form': form})
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id)

    return JsonResponse(list(cities.values('id', 'name')), safe=False)


def order(request):
    form = PersonCreation()
    if request.method == 'POST':
        form = PersonCreation(request.POST)
        if form.is_valid():


            form.save()

            return redirect('exammapp:success')





    return render(request, 'homee.html', {'form': form})
def load_prize(request):
    food_id = request.GET.get('food_id')
    prize = Prize.objects.filter(food_id=food_id)

    return JsonResponse(list(prize.values('id', 'name')), safe=False)
def success(request):

    return render(request,"success.html")






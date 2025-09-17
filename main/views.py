from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    productList = Product.objects.all()
    context =  {
        'appName': "Jaa Soccer",
        'name': "Mirza Radithya Ramadhana",
        'npm': 2406405563,
        'class': "PBP B",
        'productList': productList
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)


def show_xml(request):
    productList = Product.objects.all()
    xmlData = serializers.serialize("xml", productList)
    return HttpResponse(xmlData, content_type="application/xml")

def show_json(request):
    productList = Product.objects.all()
    jsonData = serializers.serialize("json", productList)
    return HttpResponse(jsonData, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        product = Product.objects.filter(pk=id)
        xmlData = serializers.serialize("xml", product)
        return HttpResponse(xmlData, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        productList = Product.objects.filter(pk=id)
        jsonData = serializers.serialize("json", productList)
        return HttpResponse(jsonData, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
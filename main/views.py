from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.

def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "my" and request.user.is_authenticated:
        productList = Product.objects.filter(user=request.user)
    elif filter_type == "jersey":
        productList = Product.objects.filter(category='jersey')
    elif filter_type == "ball":
        productList = Product.objects.filter(category='ball')
    elif filter_type == "boots":
        productList = Product.objects.filter(category='boots')
    elif filter_type == "accessories":
        productList = Product.objects.filter(category='accessories')
    elif filter_type == "merchandise":
        productList = Product.objects.filter(category='merchandise')
    elif filter_type == "training":
        productList = Product.objects.filter(category='training')
    else:
        productList = Product.objects.all()
    context =  {
        'appName': "Jaa Soccer",
        'name': request.user,
        'npm': 2406405563,
        'class': "PBP B",
        'productList': productList,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'filter': filter_type == "all",
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'name': request.user,
        'npm': 2406405563,
        'class': "PBP B",
        }
    return render(request, "create_product.html", context)

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
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        for product in productList
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    try:
        product = Product.objects.filter(pk=id)
        xmlData = serializers.serialize("xml", product)
        return HttpResponse(xmlData, content_type="application/xml")
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
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        next_url = request.POST.get('next') or request.GET.get('next')
        if next_url:
            response = HttpResponseRedirect(next_url)
        else:
            response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    category = request.POST.get("category")
    stock = request.POST.get("stock")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        category=category,
        stock = stock,
        price = price,
        description = description,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    name = request.POST.get("name")
    category = request.POST.get("category")
    stock = request.POST.get("stock")
    price = request.POST.get("price") 
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    product.name = name
    product.category = category
    product.stock = stock
    product.price = price
    product.description = description
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.save()
    return HttpResponse(b"UPDATED", status=200)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
@csrf_exempt
def delete_product_ajax(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return JsonResponse({"detail": "Product deleted successfully"}, status=200)
    return JsonResponse({"detail": "Invalid request"}, status=400)

def check_login_status(request):
    return JsonResponse({
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    })

@csrf_exempt
def login_ajax(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({
                'success': True,
                'message': 'Login successful!',
                'redirect_url': '/'
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({
                'success': False,
                'message': 'Invalid username or password.'
            })
    return JsonResponse({'success': False, 'message': 'Invalid request.'})

@csrf_exempt
def logout_ajax(request):
    if request.method == 'POST':
        logout(request)
        response = JsonResponse({'success': True})
        response.delete_cookie('last_login')
        
        return response
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            error_msg = '; '.join([f"{k}: {v[0]}" for k,v in form.errors.items()])
            return JsonResponse({'success': False, 'error': error_msg}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
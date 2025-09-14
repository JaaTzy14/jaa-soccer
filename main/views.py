from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from main.models import Product

# Create your views here.

def show_main(request):
    context =  {
        'appName': "Jaa Soccer",
        'name': "Mirza Radithya Ramadhana",
        'npm': 2406405563,
        'class': "PBP B"
    }
    return render(request, "main.html", context)

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
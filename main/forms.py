from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "stock", "price", "description", "thumbnail", "is_featured"]
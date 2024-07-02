from django.forms import ModelForm
from django.contrib.auth import get_user_model

from .models import Product


User = get_user_model()


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "preview", "category", "price"]

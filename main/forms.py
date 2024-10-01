from django.forms import ModelForm
from main.models import Product, Category
from django import forms

class ProductForm(ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "rating", "categories"]
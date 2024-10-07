from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "rating", "image"]

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"])
        # if not name:  # Check if the result is an empty string
        #     raise ValidationError("This field cannot be blank.")
        return name

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"])
        # if not description:  # Check if the result is an empty string
        #     raise ValidationError("This field cannot be blank.")
        return description

    def clean_image(self):
        image = strip_tags(self.cleaned_data["image"])
        # if not image:  # Check if the result is an empty string
        #     raise ValidationError("This field cannot be blank.")
        return image
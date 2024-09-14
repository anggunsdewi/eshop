from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductForm

# Create your views here.
def show_main(request):
    product_entries = Product.objects.all()
    
    context = {
        'by' : 'Anggun Sasmitha Dewi',
        'kelas' : 'PBP A',
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
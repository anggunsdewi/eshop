from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Moisturizer COSRX',
        'price': '200000',
        'description': 'COSRX OIL FREE Ultra Moisturizing Lotion (with Birch Sap) merupakan pelembab all-in-one. Lotion yang cocok untuk semua jenis kulit, termasuk kulit sensitive',
        'stock': '10',
        'rating': '4.3',
    }

    return render(request, "main.html", context)
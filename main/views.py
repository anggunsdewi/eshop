from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Air Mineral Akua',
        'price': '4000',
        'description': 'Air minum dalam botol plastik sebesar 600ml',
        'stock': '10',
    }

    return render(request, "main.html", context)
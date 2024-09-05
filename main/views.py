from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165673',
        'name': 'Anggun Sasmitha Dewi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
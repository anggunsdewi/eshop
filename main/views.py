import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from main.models import Product, Cart, CartItem
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    
    context = {
        'name': request.user.username,
        'product_entries' : product_entries,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
           user = form.get_user()
           login(request, user)
           response = HttpResponseRedirect(reverse("main:show_main"))
           response.set_cookie('last_login', str(datetime.datetime.now()))
           return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def decrement_product(request, id):
    product = Product.objects.get(pk=id)
    if product.stock == 0:
        messages.error(request, 'This product is out of stock!')
        return HttpResponseRedirect(reverse('main:show_main'))
    product.stock -= 1
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def increment_product(request, id):
    product = Product.objects.get(pk=id)
    product.stock += 1
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def categories(request):
    makeup_products = Product.objects.filter(categories__name='Makeup')
    skincare_products = Product.objects.filter(categories__name='Skincare')
    daily_use_products = Product.objects.filter(categories__name='Daily Use')
    return render(request, 'categories.html', {
        'makeup_products': makeup_products,
        'skincare_products': skincare_products,
        'daily_use_products': daily_use_products,
    })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    context = {'cart': cart, 'items': items}
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')



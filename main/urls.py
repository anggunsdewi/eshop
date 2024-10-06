from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, decrement_product, increment_product, delete_product, edit_product, home, categories, view_cart, add_to_cart, remove_from_cart, product_list, add_product_entry_ajax



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('decrement-product/<uuid:id>/', decrement_product, name='decrement_product'),
    path('increment-product/<uuid:id>/', increment_product, name='increment_product'),
    path('delete-product/<uuid:id>/', delete_product, name='delete_product'),
    path('edit-product/<uuid:id>/', edit_product, name='edit_product'),
    path('home/', home, name='home'),
    path('categories/', categories, name='categories'),
    path('products/', product_list, name='product_list'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
]
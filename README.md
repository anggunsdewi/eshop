Nama : Anggun Sasmitha Dewi 
NPM : 2306165673 
Kelas : PBP A

Tautan PWS: http://anggun-sasmitha-eshoppbp.pbp.cs.ui.ac.id/


<details>
    <summary>Tugas 2 PBP</summary>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
#### A. Membuat sebuah proyek Django baru
 - Membuat direktori baru pada komputer
 - Membuat repositori baru pada github
 - Menghubungkan direktori komputer dengan repositori di github
 - Menginstall django dengan membuat virtual environment melalui perintah `python -m venv env`
 - Mengaktifkan virtual environment Windows dengan perintah `env\Scripts\activate`
 - Membuat berkas `requirements.txt` untuk menambahkan beberapa dependencies
 - Melakukan instalasi terhadap dependencies yang ada dengan perintah `pip install -r requirements.txt`
 - Membuat proyek django dengan perintah `django-admin startproject eshop .`
 - Memastikan bahwa berkas `manage.py` aktif dengan perintah `python manage.py runserver`

#### B. Membuat aplikasi dengan nama main pada proyek
 - Menjalankan perintah `python manage.py startapp main`
 untuk membuat aplikasi baru dengan nama main
 - Mendaftarkan aplikasi main ke dalam proyek dengan menambahkan `'main'` ke dalam variabel INSTALLED_APPS yang ada pada `settings.py` di dalam direktori proyek eshop

#### C. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
 - Melakukan konfigurasi routing URL dengan membuat berkas `urls.py` di dalam direktori main, kemudian menambahkan perintah dalam urls.py dalam direktori main yang berisi:
    ```
    from django.urls import path
    from main.views import show_main
    app_name = 'main'
    urlpatterns = [
        path('', show_main, name='show_main'),
        ]
    ```
 - Membuka berkas `urls.py` dalam direktori proyek eshop kemudian mengimpor fungsi
`from django.urls import path, include`
 - Menambah perintah berikut untuk mengarahkan ke tampilan main:
    ```
    urlpatterns = [
        path('', include('main.urls')),
    ]
    ```

#### D. Membuat model pada aplikasi main dengan berkas models.py dan menambahkan perintah:
 - Menambahkan perintah mada berkas models.py dengan:
    ```
    from django.db import models
    class Product(models.Model):
        by = models.CharField(max_length=255)
        kelas = models.CharField(max_length=255)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        stock = models.IntegerField()
        rating = models.FloatField()

        def name_of_product(self):
            return self.name
        
        def is_available(self):
            return self.stock > 0
        
        def is_good(self):
            return self.rating > 3
    ```

#### E. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML
 - Membuat sebuah fungsi pada views.py yang berisi perintah:
    ```
    from django.shortcuts import render
    from .models import Product

    def show_main(request):
        context = {
            'by' : 'Anggun Sasmitha Dewi',
            'kelas' : 'PBP A',
            'name' : 'Moisturizer COSRX',
            'price': '200000',
            'description': 'COSRX OIL FREE Ultra Moisturizing Lotion (with Birch Sap) merupakan pelembab all-in-one. Lotion yang cocok untuk semua jenis kulit, termasuk kulit sensitive',
            'stock': '10',
            'rating': '4.3',
        }

        return render(request, "main.html", context)
    ```

#### F. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
 - Menambahkan perintah pada berkas urls.py pada direktori main yang berisi:
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

#### G. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
 - Membuat proyek baru dengan menekan tombol `Create New Project`
 - Pada berkas `settings.py`, menambahkan URL PWS pribadi ke dalam ALLOWED_HOSTS
 - Menjalankan perintah `git branch -M main`
 - Menjalankan perintah `git push pws main:master` untuk selanjutnya



### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](image.png)
Alur program:
- Klien mengirimkan permintaan melalui internet dan diterima oleh urls.py
- Django memeriksa urls.py untuk menentukan view mana yang harus memproses permintaan tersebut
- View di views.py memproses permintaan dengan membaca atau menulis data melalui model di models.py
- View kemudian menggunakan template HTML untuk merender halaman web
- Django mengirimkan respons dalam bentuk halaman HTML ke klien melalui internet


### Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git merupakan sebuah sistem kontrol yang membantu programmer dalam berkolaborasi secara tim. Dengan git, programmer dapat melacak perubahan dan memantau semua revisi yang telah dilakukan pada program.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena django merupakan full-stack framework, yang berarti mencakup semua aspek pengembangan aplikasi web, mulai dari database, pengelolaan URL, hingga pengiriman template ke front-end.
Django terkenal dengan filosofi "batteries included," yang berarti framework ini dilengkapi dengan berbagai fitur bawaan yang berguna, seperti otentikasi, ORM (Object-Relational Mapping), dan admin interface. Selain itu, django memiliki dokumentasi yang sangat lengkap dan terstruktur, sehingga lebih mudah dipelajari oleh pemula Django juga sangat kuat dan fleksibel. Pemula bisa mulai dengan aplikasi sederhana dan kemudian memperluasnya seiring dengan meningkatnya pengetahuan mereka. 

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara database relasional dan kode Python. ORM memungkinkan programmer untuk bekerja dengan database menggunakan objek-objek Python dibanding menulis kode SQL secara langsung.
</details>

<details>
    <summary>Tugas 3 PBP</summary>

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data delivery membantu developer dalam mengirimkan data secara cepat dan efisien. Data delivery juga memastikan bahwa data yang berada pada aplikasi frontend, server, maupun database tetap sinkron. Pada tugas kali ini, kita membutuhkan data delivery karena e-commerce membutuhkan pengiriman data secara cepat dan tepat waktu agar pengguna dapat berinteraksi dengan platform tanpa adanya delay.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, lebih baik JSON dalam data delivery. Struktur JSON dibuat sederhana, mirip seperti struktur dictionary pada Python. Pembacaan JSON lebih mudah dilakukan dibanding XML yang mengharuskan adanya elemen-elemen dengan tag pembuka dan penutup (seperti HTML). Selain itu, JSON dirancang untuk berfungsi langsung dengan JavaScript, di mana JavaScript dapat langsung memproses dan mengubah JSON menjadi objek tanpa memerlukan parsing yang kompleks. 
Hal itulah yang menurut saya menjadi alasan juga mengapa JSON lebih populer dibanding XML. JSON lebih mudah dibaca karena formatnya lebih ringkas (tidak memerlukan tag pembuka dan penutup seperti XML). Selain itu, kode untuk membaca dan membuat JSON dapat ditulis dalam bahasa pemrograman apapun. 

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method is_valid() pada form Django adalah untuk melakukan validasi terhadap data yang dikirimkan oleh user melalui form. Method ini memeriksa apakah data yang dimasukkan oleh user sesuai dengan aturan yang ditentukan dalam form tersebut, seperti jenis data, panjang teks, atau format tertentu. Method ini akan mengembalikan nilai True apabila data yang dimasukkan oleh user sudah valid dengan ketentuan, dan mengembalikan False apabila tidak valid. 

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan csrf_token (Cross-Site Request Forgery token) saat membuat form di Django untuk melindungi web dari serangan CSRF, di mana penyerang mencoba membuat pengguna tanpa disadari melakukan permintaan tidak sah ke server. 
Setiap kali sebuah form di-submit, Django memeriksa apakah ada csrf_token yang valid dan cocok dengan token yang telah di-authorize pengguna. Jika kita tidak menambahkan csrf_token dalam form Django, web menjadi rentan terhadap serangan CSRF. Dalam serangan ini, penyerang dapat memanipulasi user dengan mengirimkan request palsu ke server dari situs web yang telah di-authorize oleh user. 
Dengan dikirimkannya request palsu, penyerang dapat memanfaatkan kesempatan ini untuk mengeksekusi tindakan yang tidak diinginkan user, seperti mengubah atau menghapus data. Selain itu, penyerang dapat mengirim permintaan ke server dengan kredensial user tanpa sepengetahuan oleh user. 

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
 - Membuat berkas baru pada direktori 'main' dengan nama forms.py
 - Menambahkan kode pada berkas forms.py yang berisi:
    ```
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "stock", "rating"]
    ```
 - Membuka berkas views.py yang ada dalam direktori main dan menambahkan kode:
    ```
    from django.shortcuts import render, redirect
    from main.models import Product
    from main.forms import ProductForm
    from django.http import HttpResponse
    from django.core import serializers

    def show_main(request):
        product_entries = Product.objects.all()
        
        context = {
            'by' : 'Anggun Sasmitha Dewi',
            'kelas' : 'PBP A',
            'product_entries' : product_entries
        }

        return render(request, "main.html", context)

    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
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
    ```

 - Membuat routing URL untuk masing-masing views dengan membuka urls.py pada direktori main dan mengimport fungsi `create_product`, `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` serta menambahkan kode:
    ```
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```
- Membuat berkas HTML baru dengan nama create_product.html dan menambahkan kode:
    ```
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add Product</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```

- Menambahkan kode pada berkas main.py yang berisi:
    ```
    {% extends 'base.html' %}
    {% block content %}
    <h1>Shop at Beyoutiful</h1>

    {% if not product_entries %}
    <p>Belum ada data product pada Beyoutiful.</p>
    {% else %}
    <table>
    <tr>
        <th>Product Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Stock</th>
        <th>Rating</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data product di bawah baris ini 
    {% endcomment %} 
    {% for product_entry in product_entries %}
    <tr>
        <td>{{product_entry.name}}</td>
        <td>{{product_entry.price}}</td>
        <td>{{product_entry.description}}</td>
        <td>{{product_entry.stock}}</td>
        <td>{{product_entry.rating}}</td>
    </tr>
    {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_product' %}">
    <button>Add New Product</button>
    </a>
    {% endblock content %}
    ```

</details>
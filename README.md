Nama : Anggun Sasmitha Dewi 
NPM : 2306165673 
Kelas : PBP A

Tautan PWS: http://anggun-sasmitha-eshoppbp.pbp.cs.ui.ac.id/

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
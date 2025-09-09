Nama            : Mirza Radithya Ramadhana
NPM             : 2406405563
Kelas           : PBP B
Tautan PWS      : https://mirza-radithya-jaasoccer.pbp.cs.ui.ac.id/
Tautan GitHub   : https://github.com/JaaTzy14/jaa-soccer

Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Checklist 1: Membuat sebuah proyek Django baru.
        Saya membuat folder baru bernama jaa-soccer yang berfungsi sebagai direktori utama. Pada direktori tersebut, saya menginisialisasi virtual environment, membuat file requirements.txt yang berisi dependencies, lalu menginstall seluruh dependencies tersebut. Setelah itu, saya menginisiasi proyek django dengan nama jaa_soccer. Selanjutnya, saya membuat file .env untuk development dan file .env.prod untuk production yang berisi konfigurasi enviroment variables. Terakhir, saya menyesuaikan settings.py agar membaca variabel tersebut, menambahkan ALLOWED_HOSTS, dan mengatur database agar otomatis memakai SQLite saat development serta PostgreSQL saat production.
    - Checklist 2: Membuat aplikasi dengan nama main pada proyek tersebut.
        Saya menjalankan perintah "python manage.py startapp main" untuk membuat aplikasi dengan nama main. Selanjutnya, saya mendaftarkan aplikasi tersebut ke daftar aplikasi pada file settings.py. Terakhir, saya membuat direktori templates pada direktori aplikasi main, membuat file main.html, lalu menulis beberapa kode singkat pada html tersebut.
    - Checklist 3: Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        Saya melakukan routing dengan cara menambahkan "path('', include('main.urls'))" pada daftar urlpatterns di file urls.py direktori proyek sehingga aplikasi main dapat diakses.
    - Checklist 4: Membuat model pada aplikasi main dengan nama Product dan beberapa atribut.
        Saya membuat model product dengan menambahkan class product pada models.py di direktori main. Saya juga menambahkan beberapa atribut, seperti name dan price, dengan tipe datanya masing-masing. Setelah itu, saya melakukan membuat dan mengaplikasikan migrasi model agar perubahan pada models.py terefleksikan dalam database.
    - Checklist 5: Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        Saya mendefinisikan fungsi show_main pada views.py. Setelah itu, saya menambahkan context yang berisi nama aplikasi, nama saya, npm saya, dan kelas saya. Fungsi tersebut akan mereturn render ke template main.html dengan membawa data context sehingga informasi dapat ditampilkan pada HTML.
    - Checklist 6: Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        Saya mengimpor fungsi show_main dari views.py pada direkroti app main, mendefinisikan app_name untuk penamaan routing, lalu menambahkan "path('', show_main, name='show_main')" agar ketika aplikasi diakses melalui URL utama, fungsi show_main yang telah dibuat akan dipanggil dan menampilkan halaman sesuai template.
    - Checklist 7: Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat.
        Saya membuat proyek baru di PWS dengan nama jaasoccer, menyimpan credentials, lalu menyalin konfigurasi dari .env.prod ke tab Environs. Setelah itu, saya menambahkan URL deployment ke ALLOWED_HOSTS pada settings.py, melakukan git add, commit, dan push, kemudian menjalankan perintah Project Command dan memasukkan credentials yang telah disimpan untuk melakukan deployment.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    URL: https://www.ibmmainframer.com/static/django/images/MVT_req_resp.png
    Ketika seorang pengguna ingin mengakses server Django, request akan masuk ke urls.py. File itu akan mencocokkan alamat URL yang diminta dengan route yang sudah ada. Jika ditemukan routenya, Django akan meneruskan request ke fungsi yang ada di views.py. Di dalam view, fungsi akan dijalankan. Fungsi tersebut bisa sekadar menyiapkan data, atau berinteraksi dengan models.py untuk membaca maupun menulis ke database. Data yang didapat kemudian diproses dan dikirimkan ke template HTML agar ditampilkan dalam bentuk halaman web yang bisa dilihat oleh pengguna. Setelah itu, server mengirim respons HTML tersebut kembali ke browser, sehingga pengguna bisa melihat hasilnya.

3. Jelaskan peran settings.py dalam proyek Django!
    File settings.py berfungsi untuk mengatur konfigurasi dari suatu proyek, seperti daftar aplikasi, host, dan database. Dengan kata lain, file tersebut menjadi tempat utama untuk mengatur mekanisme proyek sesuai agar sesuai dengan kebutuhan.

4. Bagaimana cara kerja migrasi database di Django?
    Migrasi pada Django berfungsi untuk menjaga struktur data base sinkron dengan model yang dibuat pada models.py. Ketika kita menambah atau mengubah model,kita harus menjalankan makemigrations untuk membuat file migrasi yang berisi instruksi perubahan model, lalu menjalankan migrate untuk menerapkan perubahan tersebut ke dalam data base.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut saya, ada beberapa alasan mengapa framework django sering dijadikan pembelajaran. Pertama, Django bisa digunakan secara cross-platform. Kedua, Django dibuat menggunakan python sehingga ramah bagi pemula. Ketiga, Django memiliki dokumentasi yang lengkap sehingga dapat memudahkan pengembang. Keempat, Django menyediakan ORM yang membuat pengembang dapat dengan mudah mentransfer data dari database menjadi sebuah objek. Terakhir, Django menyediakan salah satu security terbaik.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Tidak ada, sudah baik.

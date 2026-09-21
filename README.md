Nama : Muhammad Zaky Robbani
NPM : 2506597712
Kelas : PBP D

### tugas 1 tidak ada jawaban

### tugas 2
1. Ketika pengguna membuka halaman portofolio baru, permintaan pertama kali diteruskan ke urls.py di dictionary proyek. Lalu dari urls.py proyek, akan diteruskan ke urls.py di main, yang kemudian akan diteruskan ke views.py di main. File views.py di main akan membuat context dan memanggil html file yang ada di folder "templates", lalu mengembalikan file html tersebut yang sudah di implementasi dengan context sesuai dengan documentary Django.

2. Karena jika hanya ingin perubahan kedepannya, hal yang harus dilakukan hanya dengan mengubah database yang terhubung dengan model tersebut tanpa harus menyentuh file htmlnya sama sekali

3. "makemigrations" mendeteksi semua perubahan model dan membuat file migrasi berdasarkan perubahan tersebut. "migrate" membaca file migrasi tersebut dan melakukan perubahan pada database model sesuai dengan perubahan yang dilakukan

ai disclosure: use chatgpt to verify all of my answer

### tugas 3
1. karena objek ModelForm dapat memudahkan pembuatan form dengan mendefinisikan objek ModelForm yang kemudian dapat digunakan di berbagai halaman tanpa harus mengetik ulang form tersebut. csrf token digunakan untuk memastikan keamanan dengan mencocokkan cookie id dengan csrf token agar pihak ketiga tidak dapat melakukan hal buruk dengan memanfaatkan csrf (cross site request forgery) attack.

2. karena format JSON lebih mudah untuk digunakan dan lebih di support ketimbang XML di berbagai programming language yang dipakai saat

3. proses serialization adalah proses yang mengubah data-data objek suatu programming language menjadi JSON text yang kemudian dapat disimpan dan dikirim. Namun proses serialization memerlukan penerima data untuk meng-deserialize JSON text tersebut agar dapat dimengerti oleh programnya kembali

ai disclosure: use chatgpt to explain how csrf token works in the real world, and verify the other answer
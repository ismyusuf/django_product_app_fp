# Link Demo Proyek & Website Proyek
youtube https://youtu.be/0a2UFkYqwBQ

web https://muhyusuf2.pythonanywhere.com/
# Django Product Management App

Sistem manajemen produk berbasis Django untuk **Tes Junior Programmer FastPrint**.

## Deskripsi

Proyek ini adalah sistem manajemen produk yang:

- Mengambil data dari API eksternal FastPrint (`api_get_data.py`)
- Menyimpan data ke database PostgreSQL (3 tabel: Produk, Kategori, Status)
- Menyediakan fitur CRUD (Tambah, Edit, Hapus) melalui antarmuka web
- Menampilkan data yang hanya berstatus **"bisa dijual"** (dengan opsi lihat semua)
- Menyediakan REST API menggunakan Django REST Framework (Serializer)
- Form validasi: nama produk wajib diisi, harga harus angka positif
- Alert konfirmasi JavaScript saat hapus produk
- Dokumentasi lengkap (README)

## Tech Stack

- **Framework**: Django 6.0.2
- **API Framework**: Django REST Framework (Serializer)
- **Database**: PostgreSQL (utama) / SQLite (alternatif)
- **Python**: 3.12
- **Frontend**: Tailwind CSS via CDN

## Struktur Proyek

```
django_product_app_fp/
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database (backup)
├── api_get_data.py           # Script untuk import data dari API
├── api_consume.ipynb         # Notebook untuk consume API
├── product_app/              # Konfigurasi Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── products/                 # App utama
    ├── models.py             # Model: Produk, Kategori, Status
    ├── views.py              # Views untuk web interface
    ├── views_api.py          # ViewSet untuk REST API
    ├── serializers.py        # Serializer untuk API
    ├── forms.py              # Form dengan validasi
    ├── urls.py               # URL routing web
    ├── urls_api.py           # URL routing API
    ├── templates/            # HTML templates
    └── migrations/           # Database migrations
```

## Model Data

### Kategori

| Field         | Type           | Description          |
| ------------- | -------------- | -------------------- |
| id            | AutoField      | Primary key          |
| nama_kategori | CharField(100) | Nama kategori produk |

### Status

| Field       | Type           | Description   |
| ----------- | -------------- | ------------- |
| id          | AutoField      | Primary key   |
| nama_status | CharField(100) | Status produk |

### Produk

| Field       | Type           | Description        |
| ----------- | -------------- | ------------------ |
| id          | AutoField      | Primary key        |
| nama_produk | CharField(200) | Nama produk        |
| harga       | IntegerField   | Harga produk       |
| kategori    | ForeignKey     | Relasi ke Kategori |
| status      | ForeignKey     | Relasi ke Status   |

## Instalasi

### 1. Clone Repository

```bash
git clone <repository-url>
cd django_product_app_fp
```

### 2. Buat Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework psycopg2-binary requests
```

Atau buat file `requirements.txt` dengan:

```
django>=6.0.2
djangorestframework
psycopg2-binary
requests
```

Lalu install:

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Database

**Opsi A: PostgreSQL (Default)**

1. Install PostgreSQL
2. Buat database:

```sql
CREATE DATABASE productdb;
```

3. Sesuaikan kredensial di `product_app/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'productdb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**Opsi B: SQLite (Alternatif)**

Ubah konfigurasi di `product_app/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 5. Migrasi Database

```bash
python manage.py migrate
```

### 6. Import Data dari API (Opsional)

```bash
python api_get_data.py
```

Script ini akan:

- Mengambil data dari API eksternal FastPrint
- Generate kredensial berdasarkan tanggal server
- Import data Kategori, Status, dan Produk ke database

### 7. Buat Superuser (Opsional)

```bash
python manage.py createsuperuser
```

### 8. Jalankan Server

```bash
python manage.py runserver
```

Akses aplikasi di: http://127.0.0.1:8000

## Endpoint

### Web Interface

| URL              | Method    | Description                             |
| ---------------- | --------- | --------------------------------------- |
| `/`              | GET       | Daftar produk (filter: bisa dijual)     |
| `/semua/`        | GET       | Daftar semua produk (tanpa filter)      |
| `/add/`          | GET, POST | Tambah produk baru                      |
| `/edit/<id>/`    | GET, POST | Edit produk                             |
| `/delete/<id>/`  | GET, POST | Hapus produk (dengan JS confirm + page) |

### REST API

| URL                     | Method | Description         |
| ----------------------- | ------ | ------------------- |
| `/api/produk/`          | GET    | Daftar semua produk |
| `/api/produk/`          | POST   | Tambah produk baru  |
| `/api/produk/<id>/`     | GET    | Detail produk       |
| `/api/produk/<id>/`     | PUT    | Update produk       |
| `/api/produk/<id>/`     | DELETE | Hapus produk        |
| `/api/kategori/`        | GET    | Daftar kategori     |
| `/api/status/`          | GET    | Daftar status       |

### Contoh Request API

**GET All Products**

```bash
curl http://127.0.0.1:8000/api/produk/
```

**POST New Product**

```bash
curl -X POST http://127.0.0.1:8000/api/produk/ \
  -H "Content-Type: application/json" \
  -d '{"nama_produk": "Produk Baru", "harga": 50000, "kategori": 1, "status": 1}'
```

## Fitur Validasi

### Form (Web Interface)

- Nama produk minimal 3 karakter
- Harga harus angka positif
- Kategori wajib dipilih
- Status wajib dipilih

### Serializer (API)

- Nama produk tidak boleh kosong
- Harga harus > 0
- Kategori wajib
- Status wajib

## Admin Panel

Akses admin panel di: http://127.0.0.1:8000/admin/

## Troubleshooting

### Error: psycopg2 not installed

```bash
pip install psycopg2-binary
```

### Error: Database connection refused

1. Pastikan PostgreSQL running
2. Cek kredensial di settings.py
3. Pastikan database sudah dibuat

### Error: Migrations pending

```bash
python manage.py makemigrations
python manage.py migrate
```

"""
=============================================================================
  Script: api_get_data.py
  Deskripsi: Mengambil data produk dari API FastPrint dan menyimpan ke database
  
  Cara kerja:
  1. Melakukan request ke API untuk mendapatkan waktu server
  2. Generate username & password berdasarkan waktu server dan local
  3. Mengambil data produk dari API
  4. Menyimpan data Kategori, Status, dan Produk ke database Django
=============================================================================
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_app.settings')
django.setup()

from products.models import Produk, Kategori, Status
import requests
from datetime import datetime
import hashlib
import json

# ── URL API ──────────────────────────────────────────────────────────────────
API_URL = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"


def get_server_date():
    """Step 1: Request ke API untuk mendapatkan tanggal server dari header 'Date'."""
    print("[1/4] Mengambil waktu server...")
    response = requests.post(API_URL)
    server_date_str = response.headers.get('Date', '')
    if not server_date_str:
        print("  ERROR: Header 'Date' tidak ditemukan di response.")
        sys.exit(1)
    print(f"  Server Date: {server_date_str}")
    return server_date_str


def generate_credentials(server_date_str):
    """
    Step 2: Generate username dan password berdasarkan waktu server.
    
    Format username : tesprogrammerDDMMYYCHH
    Format password : md5("bisacoding-DD-MM-YY")
    
    DD = tanggal, MM = bulan, YY = 2 digit tahun, HH = jam (dari server)
    """
    print("[2/4] Generate kredensial...")
    server_date = datetime.strptime(server_date_str, '%a, %d %b %Y %H:%M:%S %Z')
    
    # Username: menggunakan tanggal dari server dan jam dari local
    local_time = datetime.now()
    local_hour = local_time.strftime('%H')
    username = f"tesprogrammer{server_date.strftime('%d%m%y')}C{local_hour}"
    
    # Password: bisacoding-DD-MM-YY lalu di-hash MD5
    password_raw = f"bisacoding-{server_date.strftime('%d-%m-%y')}"
    password_md5 = hashlib.md5(password_raw.encode()).hexdigest()
    
    print(f"  Username : {username}")
    print(f"  Password : {password_raw} -> MD5: {password_md5}")
    return username, password_md5


def fetch_products(username, password_md5):
    """Step 3: Mengambil data produk dari API menggunakan kredensial."""
    print("[3/4] Mengambil data produk dari API...")
    payload = {
        'username': username,
        'password': password_md5
    }
    response = requests.post(API_URL, data=payload)
    data = response.json()
    
    if not data.get('data'):
        print(f"  ERROR: Tidak ada data. Response: {json.dumps(data, indent=2)}")
        sys.exit(1)
    
    products = data['data']
    if not isinstance(products, list):
        print(f"  ERROR: Format data tidak sesuai. Type: {type(products)}")
        sys.exit(1)
    
    print(f"  Berhasil mengambil {len(products)} produk dari API")
    if products:
        print(f"  Kolom data: {list(products[0].keys())}")
    return products


def import_to_database(products_data):
    """
    Step 4: Import data ke database Django.
    
    Proses:
    - Get or create Kategori berdasarkan nama
    - Get or create Status berdasarkan nama
    - Get or create Produk berdasarkan nama_produk (update jika sudah ada)
    """
    print(f"[4/4] Menyimpan {len(products_data)} produk ke database...")
    
    created_count = 0
    updated_count = 0
    
    for item in products_data:
        # Get or create Kategori
        kategori, _ = Kategori.objects.get_or_create(
            nama_kategori=item['kategori']
        )
        
        # Get or create Status
        status, _ = Status.objects.get_or_create(
            nama_status=item['status']
        )
        
        # Pastikan harga berupa integer
        try:
            harga = int(item['harga'])
        except (ValueError, TypeError):
            harga = 0
        
        # Get or create Produk (gunakan nama_produk sebagai identifier unik)
        produk, created = Produk.objects.get_or_create(
            nama_produk=item['nama_produk'],
            defaults={
                'harga': harga,
                'kategori': kategori,
                'status': status
            }
        )
        
        if created:
            created_count += 1
        else:
            # Update jika sudah ada
            produk.harga = harga
            produk.kategori = kategori
            produk.status = status
            produk.save()
            updated_count += 1
    
    print(f"\n  === HASIL IMPORT ===")
    print(f"  Produk baru   : {created_count}")
    print(f"  Produk update : {updated_count}")
    print(f"  Total kategori: {Kategori.objects.count()}")
    print(f"  Total status  : {Status.objects.count()}")
    print(f"  Total produk  : {Produk.objects.count()}")


# ── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 60)
    print("  IMPORT DATA PRODUK DARI API FASTPRINT")
    print("=" * 60)
    
    # Step 1: Dapatkan waktu server
    server_date_str = get_server_date()
    
    # Step 2: Generate kredensial
    username, password_md5 = generate_credentials(server_date_str)
    
    # Step 3: Ambil data dari API
    products_data = fetch_products(username, password_md5)
    
    # Step 4: Simpan ke database
    import_to_database(products_data)
    
    print("\n" + "=" * 60)
    print("  SELESAI! Data berhasil diimport ke database.")
    print("=" * 60)
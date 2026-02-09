import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_app.settings')
django.setup()

from products.models import Produk, Kategori, Status
import requests
from datetime import datetime
import hashlib
import json

# URL API
url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

# Step 1: Get server date for credentials
response = requests.post(url)
server_date_str = response.headers['Date']

# Step 2: Generate username and password
def generate_credentials(server_date_str):
    """Generate username and password based on server date"""
    server_date = datetime.strptime(server_date_str, '%a, %d %b %Y %H:%M:%S %Z')
    local_time = datetime.now()
    local_hour = local_time.strftime('%H')  # 2-digit local hour
    username = f"tesprogrammer{server_date.strftime('%d%m%y')}C{local_hour}"
    password = f"bisacoding-{server_date.strftime('%d-%m-%y')}"
    return username, password

username, password = generate_credentials(server_date_str)

# Step 3: Get data from API
def get_data_api(username, password):
    params = {'username': username, 'password': hashlib.md5(password.encode()).hexdigest()}
    response = requests.post(url, data=params)
    return response.json()

data = get_data_api(username, password)

# Step 4: Import data to Django models
# Data is a dict with 'data' key containing list of dicts
products_data = data.get('data', [])
if not isinstance(products_data, list):
    print("Unexpected data structure for 'data':", type(products_data))
    exit(1)

if products_data:
    print("First item keys:", list(products_data[0].keys()))
else:
    print("No data to import")
    exit(0)

for item in products_data:
    # Get or create Kategori
    kategori, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
    
    # Get or create Status
    status, _ = Status.objects.get_or_create(nama_status=item['status'])
    
    # Get or create Produk
    produk, created = Produk.objects.get_or_create(
        id_produk=item['id_produk'],
        defaults={
            'nama_produk': item['nama_produk'],
            'harga': item['harga'],
            'kategori': kategori,
            'status': status
        }
    )
    if not created:
        # Update if already exists
        produk.nama_produk = item['nama_produk']
        produk.harga = item['harga']
        produk.kategori = kategori
        produk.status = status
        produk.save()

print("Data imported successfully!")
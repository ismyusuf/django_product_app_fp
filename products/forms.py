from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        error_messages = {
            'nama_produk': {
                'required': 'Nama produk tidak boleh kosong.',
            },
            'harga': {
                'required': 'Harga tidak boleh kosong.',
            },
            'kategori': {
                'required': 'Kategori harus dipilih.',
            },
            'status': {
                'required': 'Status harus dipilih.',
            },
        }
        widgets = {
            'nama_produk': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-all outline-none text-slate-900 dark:text-white',
                'placeholder': 'Contoh: ALCOHOL GEL POLISH CLEANSER'
            }),
            'harga': forms.NumberInput(attrs={
                'class': 'w-full pl-10 pr-4 py-2.5 bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-all outline-none text-slate-900 dark:text-white',
                'placeholder': '0'
            }),
            'kategori': forms.Select(attrs={
                'class': 'w-full px-4 py-2.5 bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-all outline-none text-slate-900 dark:text-white appearance-none'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-2.5 bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary transition-all outline-none text-slate-900 dark:text-white appearance-none'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.required = False

    def clean_nama_produk(self):
        nama_produk = self.cleaned_data.get('nama_produk')
        if nama_produk and len(nama_produk.strip()) < 3:
            raise forms.ValidationError("Nama produk minimal 3 karakter.")
        return nama_produk.strip() if nama_produk else nama_produk

    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if harga is not None and harga <= 0:
            raise forms.ValidationError("Harga harus lebih besar dari 0.")
        return harga
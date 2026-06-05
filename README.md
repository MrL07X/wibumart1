# 🎌 WibuMart — Sistem Penjualan Merchandise Anime Berbasis Web
**Mata Kuliah:** Bahasa Pemrograman (CIE201)

---

## 👥 Anggota Kelompok
| Nama | NIM | Peran |
|------|-----|-------|
| Muhammad Luthfi Rifat Rustama | 20250801038 | Database |
| Indra Setiawan | 20250801180 | Front End |
| Bryllent Arcielio Lim | 20250801044 | Back End |
| Alif Sudzarmais Rumafa | 20250801132 | UI/UX |

---

## 🚀 Cara Menjalankan

### 1. Install Python 3.10+
Pastikan Python sudah terinstall di komputer kamu.

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi
```bash
python app.py
```

### 4. Buka browser
Kunjungi **http://127.0.0.1:5000**

---

## 📁 Struktur Project
```
wibumart/
├── app.py              ← Backend Flask (routes, fungsi, data)
├── requirements.txt    ← Daftar library Python
├── README.md           ← Dokumentasi ini
└── templates/
    ├── base.html       ← Template dasar (navbar, footer, cart sidebar)
    ├── index.html      ← Halaman utama & katalog produk
    ├── checkout.html   ← Halaman checkout (form & pembayaran)
    └── struk.html      ← Halaman struk / receipt
```

---

## 🐍 Komponen Python yang Digunakan

| Komponen | Implementasi |
|----------|-------------|
| **Tipe Data** | `str`, `int`, `float`, `list`, `dict`, `bool` |
| **Operator Aritmatika** | `total = harga × jumlah` |
| **Operator Perbandingan** | `if kategori == "all"` |
| **Struktur Kontrol** | `if-elif-else`, `for` loop |
| **Fungsi/Subprogram** | `hitung_total()`, `filter_produk()`, `format_rupiah()` |
| **List Comprehension** | `[p for p in PRODUK if p['kategori'] == kategori]` |
| **Dictionary** | Data produk disimpan sebagai `list[dict]` |
| **Session** | Keranjang belanja disimpan di Flask session |
| **Jinja2 Template** | Render HTML dari data Python |
| **Flask Routes** | `@app.route()` untuk setiap halaman |

---

## ✨ Fitur Aplikasi
- 🛍️ Katalog produk dengan filter kategori
- 🛒 Keranjang belanja real-time (AJAX)
- 👤 Form input data pembeli dengan validasi
- 💳 Pilih metode pembayaran (COD / Transfer Bank)
- 🧾 Struk pembelian otomatis
- 🌟 UI modern bertema anime (dark blue + orange)

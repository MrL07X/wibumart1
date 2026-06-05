"""
╔══════════════════════════════════════════════════════════════════════╗
║       WIBUMART — Sistem Penjualan Merchandise Anime Berbasis Web     ║
║       Mata Kuliah : Bahasa Pemrograman (CIE201)                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  Anggota Kelompok:                                                   ║
║  • Muhammad Luthfi Rifat Rustama  (20250801038)  — Database          ║
║  • Indra Setiawan                 (20250801180)  — Front End         ║
║  • Bryllent Arcielio Lim          (20250801044)  — Back End          ║
║  • Alif Sudzarmais Rumafa         (20250801132)  — UI/UX             ║
╚══════════════════════════════════════════════════════════════════════╝
"""

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from datetime import datetime
import random
import string

# ── Inisialisasi Aplikasi Flask ──────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = "wibumart-cie201-secret-2025"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  DATA PRODUK  (List of Dictionaries — Tipe Data & Struktur Data Python)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRODUK: list = [
    # ── FIGURE ──────────────────────────────────────────────────────────────
    {
        "id": 1,
        "nama": "Figure Naruto Uzumaki",          # String
        "harga": 150000,                          # Integer
        "kategori": "figure",
        "emoji": "🥷",
        "warna": "#E8612A",
        "badge": "TERLARIS",
        "badge_tipe": "popular",
        "deskripsi": "Figure premium 25cm pose Rasengan, detail tinggi, limited edition",
        "stok": 15,
        "rating": 4.9,                            # Float
    },
    {
        "id": 2,
        "nama": "Figure Luffy Gear 5",
        "harga": 185000,
        "kategori": "figure",
        "emoji": "😄",
        "warna": "#D4A017",
        "badge": "NEW",
        "badge_tipe": "new",
        "deskripsi": "Figure GK pose Sun God Nika, tinggi 28cm, kualitas museum grade",
        "stok": 8,
        "rating": 5.0,
    },
    {
        "id": 3,
        "nama": "Figure Gojo Satoru",
        "harga": 200000,
        "kategori": "figure",
        "emoji": "🫧",
        "warna": "#6C63FF",
        "badge": "HOT",
        "badge_tipe": "hot",
        "deskripsi": "Figure eksklusif dengan efek Infinity Domain Expansion panel",
        "stok": 5,
        "rating": 4.8,
    },
    {
        "id": 4,
        "nama": "Figure Mikasa Ackerman",
        "harga": 170000,
        "kategori": "figure",
        "emoji": "⚔️",
        "warna": "#3D9970",
        "badge": "",
        "badge_tipe": "",
        "deskripsi": "Figure detail dengan mantel Survey Corps & omni-directional blade",
        "stok": 12,
        "rating": 4.7,
    },
    # ── POSTER ──────────────────────────────────────────────────────────────
    {
        "id": 5,
        "nama": "Poster One Piece Wano",
        "harga": 45000,
        "kategori": "poster",
        "emoji": "🗺️",
        "warna": "#C0392B",
        "badge": "A2",
        "badge_tipe": "",
        "deskripsi": "Poster full color A2, glossy UV coating premium, anti-pudar",
        "stok": 50,
        "rating": 4.8,
    },
    {
        "id": 6,
        "nama": "Poster Demon Slayer",
        "harga": 45000,
        "kategori": "poster",
        "emoji": "🌸",
        "warna": "#D63384",
        "badge": "A2",
        "badge_tipe": "",
        "deskripsi": "Poster A2 matte finish, warna vivid edisi Hinokami Kagura",
        "stok": 40,
        "rating": 4.9,
    },
    {
        "id": 7,
        "nama": "Poster Attack on Titan",
        "harga": 40000,
        "kategori": "poster",
        "emoji": "🏰",
        "warna": "#795548",
        "badge": "A2",
        "badge_tipe": "",
        "deskripsi": "Poster final season A2, scene epik Eren Yeager The Rumbling",
        "stok": 35,
        "rating": 4.7,
    },
    # ── AKSESORIS ────────────────────────────────────────────────────────────
    {
        "id": 8,
        "nama": "Gantungan Kunci Anime",
        "harga": 25000,
        "kategori": "aksesoris",
        "emoji": "🗝️",
        "warna": "#0288D1",
        "badge": "SET 5",
        "badge_tipe": "",
        "deskripsi": "Set 5 gantungan kunci acrylic premium berbagai karakter anime",
        "stok": 100,
        "rating": 4.6,
    },
    {
        "id": 9,
        "nama": "Pin Badge Collection",
        "harga": 35000,
        "kategori": "aksesoris",
        "emoji": "📌",
        "warna": "#E65100",
        "badge": "SET 10",
        "badge_tipe": "",
        "deskripsi": "Set 10 pin badge metal electroplating berbagai seri anime top",
        "stok": 80,
        "rating": 4.5,
    },
    {
        "id": 10,
        "nama": "Tote Bag Canvas Anime",
        "harga": 75000,
        "kategori": "aksesoris",
        "emoji": "🎒",
        "warna": "#2E7D32",
        "badge": "NEW",
        "badge_tipe": "new",
        "deskripsi": "Tote bag canvas 12oz tebal, sablon full color, anti-air & tahan cuci",
        "stok": 25,
        "rating": 4.8,
    },
    {
        "id": 11,
        "nama": "Stiker Pack Anime",
        "harga": 20000,
        "kategori": "aksesoris",
        "emoji": "✨",
        "warna": "#6A1B9A",
        "badge": "40pcs",
        "badge_tipe": "",
        "deskripsi": "40 lembar stiker vinyl waterproof glossy berbagai karakter anime",
        "stok": 200,
        "rating": 4.6,
    },
]

# ── Anggota Tim ──────────────────────────────────────────────────────────────
TIM: list = [
    {"nama": "Muhammad Luthfi Rifat Rustama", "peran": "Database",   "nim": "20250801038", "emoji": "🗄️"},
    {"nama": "Indra Setiawan",                "peran": "Front End",  "nim": "20250801180", "emoji": "🎨"},
    {"nama": "Bryllent Arcielio Lim",         "peran": "Back End",   "nim": "20250801044", "emoji": "⚙️"},
    {"nama": "Alif Sudzarmais Rumafa",         "peran": "UI/UX",      "nim": "20250801132", "emoji": "🖌️"},
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  FUNGSI / SUBPROGRAM  (sesuai desain sistem pada proposal)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def ambil_keranjang() -> list:
    """Mengambil data keranjang dari session."""
    return session.get("keranjang", [])


def simpan_keranjang(keranjang: list) -> None:
    """Menyimpan data keranjang ke session."""
    session["keranjang"] = keranjang
    session.modified = True


def hitung_total(keranjang: list) -> int:
    """
    Subprogram HitungTotal(harga, jumlah)
    Menghitung total harga berdasarkan jumlah barang yang dibeli.
    totalHarga = hargaBarang × jumlahBarang
    """
    # Operator aritmatika: perkalian & penjumlahan
    return sum(item["harga"] * item["jumlah"] for item in keranjang)


def format_rupiah(angka: int) -> str:
    """Memformat angka menjadi format Rupiah Indonesia."""
    return f"Rp {angka:,.0f}".replace(",", ".")


def hitung_jumlah_item(keranjang: list) -> int:
    """Menghitung total jumlah item dalam keranjang."""
    return sum(item["jumlah"] for item in keranjang)


def cari_produk(product_id: int):
    """Mencari produk berdasarkan ID menggunakan perulangan."""
    # Struktur kontrol: perulangan for
    for produk in PRODUK:
        if produk["id"] == product_id:   # Operator perbandingan ==
            return produk
    return None                           # None jika tidak ditemukan


def buat_nomor_invoice() -> str:
    """Membuat nomor invoice unik secara acak."""
    chars: str = string.ascii_uppercase + string.digits
    kode: str = "".join(random.choices(chars, k=6))
    return f"WM-{kode}"


def filter_produk(kategori: str) -> list:
    """
    Subprogram TampilProduk()
    Menampilkan daftar produk beserta harga berdasarkan kategori.
    """
    # Struktur kontrol: percabangan if-else
    if kategori == "all":
        return PRODUK
    else:
        # List comprehension — fitur Python
        return [p for p in PRODUK if p["kategori"] == kategori]


# Daftarkan filter ke Jinja2
app.jinja_env.filters["rupiah"] = format_rupiah


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ROUTES / ENDPOINT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route("/")
def beranda():
    """Halaman utama — katalog produk."""
    kategori: str = request.args.get("cat", "all")
    daftar_produk: list = filter_produk(kategori)
    keranjang: list = ambil_keranjang()
    jumlah_item: int = hitung_jumlah_item(keranjang)

    return render_template(
        "index.html",
        produk=daftar_produk,
        kategori_aktif=kategori,
        tim=TIM,
        keranjang_count=jumlah_item,
    )


@app.route("/tambah-keranjang", methods=["POST"])
def tambah_keranjang():
    """API: Menambahkan produk ke keranjang (AJAX)."""
    data = request.get_json()
    product_id: int = int(data.get("id", 0))

    produk = cari_produk(product_id)
    if not produk:
        return jsonify({"sukses": False, "pesan": "Produk tidak ditemukan"}), 404

    keranjang: list = ambil_keranjang()

    # Cek apakah produk sudah ada di keranjang
    item_ada = None
    for item in keranjang:
        if item["id"] == product_id:
            item_ada = item
            break

    if item_ada:
        item_ada["jumlah"] += 1        # Operator aritmatika: penambahan
    else:
        keranjang.append({
            "id":      produk["id"],
            "nama":    produk["nama"],
            "harga":   produk["harga"],
            "emoji":   produk["emoji"],
            "warna":   produk["warna"],
            "jumlah":  1,
        })

    simpan_keranjang(keranjang)

    return jsonify({
        "sukses":       True,
        "pesan":        f"{produk['nama']} ditambahkan ke keranjang!",
        "keranjang_count": hitung_jumlah_item(keranjang),
        "total":        format_rupiah(hitung_total(keranjang)),
    })


@app.route("/update-keranjang", methods=["POST"])
def update_keranjang():
    """API: Mengubah jumlah item di keranjang (AJAX)."""
    data = request.get_json()
    product_id: int = int(data.get("id", 0))
    aksi: str = data.get("aksi", "")   # 'tambah' atau 'kurang'

    keranjang: list = ambil_keranjang()

    for item in keranjang:
        if item["id"] == product_id:
            if aksi == "tambah":
                item["jumlah"] += 1
            elif aksi == "kurang":
                item["jumlah"] -= 1
                if item["jumlah"] <= 0:          # Operator perbandingan
                    keranjang.remove(item)
            break

    simpan_keranjang(keranjang)

    return jsonify({
        "sukses":          True,
        "keranjang_count": hitung_jumlah_item(keranjang),
        "total":           format_rupiah(hitung_total(keranjang)),
        "keranjang":       keranjang,
    })


@app.route("/hapus-item", methods=["POST"])
def hapus_item():
    """API: Menghapus produk dari keranjang (AJAX)."""
    data = request.get_json()
    product_id: int = int(data.get("id", 0))

    keranjang: list = ambil_keranjang()
    keranjang = [item for item in keranjang if item["id"] != product_id]
    simpan_keranjang(keranjang)

    return jsonify({
        "sukses":          True,
        "keranjang_count": hitung_jumlah_item(keranjang),
        "total":           format_rupiah(hitung_total(keranjang)),
        "keranjang":       keranjang,
    })


@app.route("/data-keranjang")
def data_keranjang():
    """API: Mengembalikan data keranjang saat ini (AJAX)."""
    keranjang: list = ambil_keranjang()
    return jsonify({
        "keranjang":       keranjang,
        "total":           format_rupiah(hitung_total(keranjang)),
        "total_angka":     hitung_total(keranjang),
        "keranjang_count": hitung_jumlah_item(keranjang),
    })


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    """
    Halaman checkout — Input data pembeli.
    Menerapkan validasi input (tidak boleh kosong).
    """
    keranjang: list = ambil_keranjang()

    # Struktur kontrol: percabangan
    if not keranjang:
        return redirect(url_for("beranda"))

    errors: dict = {}

    if request.method == "POST":
        nama_pembeli:  str = request.form.get("nama", "").strip()
        alamat:        str = request.form.get("alamat", "").strip()
        metode_bayar:  str = request.form.get("metode", "")

        # Validasi Input — tidak boleh kosong
        if not nama_pembeli:
            errors["nama"] = "⚠ Nama tidak boleh kosong"
        if not alamat:
            errors["alamat"] = "⚠ Alamat tidak boleh kosong"
        if metode_bayar not in ("COD", "Transfer"):
            errors["metode"] = "⚠ Pilih metode pembayaran"

        if not errors:
            # Simpan data transaksi ke session
            total: int = hitung_total(keranjang)
            nomor_invoice: str = buat_nomor_invoice()
            waktu: str = datetime.now().strftime("%A, %d %B %Y — %H:%M")

            session["transaksi"] = {
                "nama":         nama_pembeli,
                "alamat":       alamat,
                "metode":       metode_bayar,
                "total":        total,
                "total_fmt":    format_rupiah(total),
                "invoice":      nomor_invoice,
                "waktu":        waktu,
                "items":        keranjang.copy(),
            }

            # Kosongkan keranjang setelah berhasil
            simpan_keranjang([])
            return redirect(url_for("struk"))

    total: int = hitung_total(keranjang)
    return render_template(
        "checkout.html",
        keranjang=keranjang,
        total=format_rupiah(total),
        total_angka=total,
        errors=errors,
        keranjang_count=hitung_jumlah_item(keranjang),
    )


@app.route("/struk")
def struk():
    """
    Halaman struk / receipt — Output hasil transaksi.
    Subprogram TampilkanHasil(totalHarga, metodeBayar)
    """
    transaksi: dict = session.get("transaksi")
    if not transaksi:
        return redirect(url_for("beranda"))

    return render_template("struk.html", tx=transaksi)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ENTRY POINT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if __name__ == "__main__":
    print("=" * 60)
    print("  🎌  WIBUMART — Merchandise Anime System")
    print("  📚  Mata Kuliah: Bahasa Pemrograman (CIE201)")
    print("  🌐  Buka: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)

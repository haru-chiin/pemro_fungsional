import matplotlib.pyplot as plt

data_transaksi = [
    ("Produk A", 50,10),
    ("Produk B", 30,25),
    ("Produk C", 20,30),
    ("Produk D", 60,8),
    ("Produk E", 40,15),
    ("Produk F", 75,5),

]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk = [barang[1] for barang in data_transaksi]
jumlah_terjual = [barang[2] for barang in data_transaksi]

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.scatter(harga_produk, jumlah_terjual)
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Terjual')
plt.title('Scatter Plot: Harga Produk vs Jumlah Terjual')
plt.show()

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = [barang[1]*barang[2] for barang in data_transaksi]

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
nama_produk = [barang[0] for barang in data_transaksi]
plt.bar(nama_produk, pendapatan_produk)
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan')
plt.title('Bar Chart: Pendapatan Produk')
plt.show()
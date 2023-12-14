from PIL import Image

# TODO 1: Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open('E:/Semester 5/Fungsio/Modul6/Percobaan/tes.jpg')
overlay_image = Image.open('E:/Semester 5/Fungsio/Modul6/Percobaan/tes2.png')

# TODO 2: Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert('RGB')

# TODO 3: (optional) Perkecil ukuran gambar overlay menggunakan method resize()
# Contoh: overlay_image = overlay_image.resize((new_width, new_height))

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4: Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))

# TODO 5: Simpan gambar hasil edit
background_image.save('E:/Semester 5/Fungsio/Modul6/Percobaan/tes22222.png')

# TODO 6: Tampilkan
background_image.show()

from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
img = Image.open('E:/Semester 5/Fungsio/Modul6/Percobaan/tes.jpg')

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enchancer = ImageEnhance.Brightness(img)
brightened = enchancer.enhance(10)

enchancer = ImageEnhance.Contrast(brightened)
final_image = enchancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save('E:/Semester 5/Fungsio/Modul6/Percobaan/tes5.jpg')

# TODO 4: Tampilkan
img.show(final_image)

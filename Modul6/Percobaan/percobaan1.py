# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from PIL import Image , ImageDraw, ImageFont

# # im = mpimg.imread('E:/Semester 5/Fungsio/Modul6/Percobaan/tes2.png')
# ima = Image.open('E:/Semester 5/Fungsio/Modul6/Percobaan/tes2.png')
# # ima.save('E:/Semester 5/Fungsio/Modul6/Percobaan/tes2baru.png')
# font = ImageFont.truetype("E:/Semester 5/Fungsio/Modul6/Percobaan/Hypeday.ttf")
# grayscale_image = ima.convert('L')
# draw = ImageDraw.Draw(grayscale_image)

# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('E:/Semester 5/Fungsio/Modul6/Percobaan/tes2.png')

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype("Hypeday.ttf", 70)
text = "andaru - 252"

# Dapatkan kotak pembatas teks
bbox = draw.textbbox((0, 0), text, font)

# Hitung posisi teks agar berada di tengah gambar secara horizontal dan vertikal
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height - text_height) // 2

draw.text((text_x, text_y), text, font=font, fill="black")


# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('E:/Semester 5/Fungsio/Modul6/Percobaan/tes22.png')

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
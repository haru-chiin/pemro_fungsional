def transformasi_translasi(tx, ty):
    def translasi(x, y):
        return x + tx, y + ty
    return translasi

def transformasi_dilatasi(sx, sy):
    def dilatasi(x, y):
        return x * sx, y * sy
    return dilatasi

import math

def transformasi_rotasi(sudut):
    def rotasi(x, y):
        radian = math.radians(sudut)
        x_baru = x * math.cos(radian) - y * math.sin(radian)
        y_baru = x * math.sin(radian) + y * math.cos(radian)
        return x_baru, y_baru
    return rotasi

# Contoh kasus
titik_awal = (3, 5)

# 1. Translasi
translasi_func = transformasi_translasi(2, -1)
titik_translasi = translasi_func(*titik_awal)
print(f"Koordinat setelah translasi: {titik_translasi}")

# 2. Dilatasi
dilatasi_func = transformasi_dilatasi(2, -1)
titik_dilatasi = dilatasi_func(*titik_awal)
print(f"Koordinat setelah dilatasi: {titik_dilatasi}")

# 3. Rotasi
rotasi_func = transformasi_rotasi(30)
titik_rotasi = rotasi_func(*titik_awal)
print(f"Koordinat setelah rotasi: {titik_rotasi}")

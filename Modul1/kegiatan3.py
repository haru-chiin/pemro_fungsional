# Sistem Penilaian Akhir Mahasiswa
print ("Sistem Penilaian Akhir Mahasiswa")
# Fungsi untuk menghitung nilai akhir
def rumus_na(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menghitung nilai akhir semua mahasiswa
def rumus_sna(data_mahasiswa):
    #pembuatan dictionary
    data_nilai_akhir = {}
    #rumus perulangan perhitungan rumus 
    for nama, nilai in data_mahasiswa.items(): 
        nilai_akhir = rumus_na(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan nilai akhir
def show(data_nilai_akhir):
    print("Hasil nilai akhir mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama : {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai key, uts dan uas sebagai value dalam dictionary)
        'Andaru': {'uts': 85, 'uas': 90},
        'Adi': {'uts': 78, 'uas': 88},
        'Wardoyo': {'uts': 92, 'uas': 89},
    }
    
    data_nilai_akhir = rumus_sna(data_mahasiswa)
    show(data_nilai_akhir)

if __name__ == "__main__":
    main()

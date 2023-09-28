# Sistem Penilaian Akhir Mahasiswa
print ("Sistem Penilaian Akhir Mahasiswa")
# Fungsi untuk menghitung nilai akhir (na)
def rumus_na(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menghitung semua nilai akhir (sna)
def rumus_sna(data_mahasiswa):
    #pembuatan dictionary
    data_nilai_akhir = {}
    #rumus perulangan perhitungan rumus 
    for nama, nilai in data_mahasiswa.items(): 
        nilai_akhir = rumus_na(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# fungsi untuk menampilkan nilai akhir
def show(data_nilai_akhir):
    print("Hasil nilai akhir mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama : {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))
        
# data mahasiswa (nama = key, uts dan uas = value)
def main():
    data_mahasiswa = {
        'Andaru': {'uts': 85, 'uas': 90},
        'Adi': {'uts': 78, 'uas': 88},
        'Wardoyo': {'uts': 92, 'uas': 89},
    }
    
    data_nilai_akhir = rumus_sna(data_mahasiswa)
    show(data_nilai_akhir)

if __name__ == "__main__":
    main()

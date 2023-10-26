def konversi (m):
    def hari(h):
        def jam(j):
            def menit(t):
                return (m * 7 * 24 * 60) + (h * 24 *60) + (j * 60) + t
            return menit
        return jam
    return hari

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]


for item in data:
    data_split = item.split()
    minggu = int(data_split[0])
    hari = int(data_split[2])
    jam = int(data_split[4])
    menit = int (data_split[6])
    hasil = konversi(minggu)(hari)(jam)(menit)
    print(f"{item} = {hasil} menit")

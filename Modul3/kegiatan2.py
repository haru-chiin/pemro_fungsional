
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

fix_data = []

for item in data:
    parts = item.split()
    pisah = filter(lambda a: a.isdigit(), parts)
    fix_data.append(list(pisah))

for data in fix_data:
    print(data)

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

pisah_int = list(filter(lambda a: isinstance(a, int),random_list))
pisah_float = list(filter(lambda a: isinstance(a, float),random_list))
pisah_string = list(filter(lambda a: isinstance(a,str),random_list))

fix_data = []

for item in pisah_int:
    satuan = item % 10
    puluhan = (item // 10) % 10
    ratusan = item // 100
    fix_data.append({"ratusan ":ratusan, "puluhan":puluhan, "satuan":satuan})
    
print("Data Float = ",pisah_float)
print("Data int = ")
for item in fix_data:
    print (item)
print("Data Sting = ",pisah_string)
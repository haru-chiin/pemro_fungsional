random_list = [105, 3.1, "hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

data_int = {}
data_float = ()
string_data = []

for item in random_list:
    if isinstance(item, int):
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        data_int[item] = (satuan, puluhan, ratusan)
    elif isinstance(item, float):
        data_float += (item,)
    elif isinstance(item, str):
        string_data.append(item)

print("data integer : (satuan , puluhan , ratusan)")
print(data_int)

print("data float :")
print(data_float)

print("data String : ")
print(string_data)



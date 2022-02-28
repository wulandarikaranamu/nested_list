data_0 = [1,2]
data_1 = [3,4]
data_2 = [5,6]

data_list = [1,2,3,4,5,6]
print(f"data listnya biasa:",(data_list))

print("-------------------batas----------------")

list_2D = data_0,data_1,data_2,data_list
print(f"data listnya 2D:,{list_2D}")


print("-------------------batas----------------")

list_3D = data_0,data_1,data_2,data_list
print(f"data listnya 2D:,{list_3D}")

print("-------------------batas----------------")

#CONTOH PENGGUNAAN 

peserta_0 = ["merry",18,"mamuju"]
peserta_1 = ["mayang",16,"mamuju"]
peserta_2 = ["andi",22,"mamuju"]

list_peserta = peserta_0,peserta_1,peserta_2
print(f"peserta maraton tahun 1770,{list_peserta}")

print("-------------------batas----------------")

for peserta in (list_peserta):
    print(f"nama peserta\t:,{peserta[0]}")
    print(f"umur peserta\t:,{peserta[1]}")
    print(f"asal  peserta\t:,{peserta[2]}")
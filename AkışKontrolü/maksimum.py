#with if blocks
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
sayi3 = int(input("3. Sayı: "))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
	buyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
	buyuk = sayi2
else:
	buyuk = sayi3

print("Max = ",buyuk)

#with max() fonction
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
sayi3 = int(input("3. Sayı: "))

print(max(sayi1, sayi2, sayi3))

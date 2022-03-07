# kullanıcıdan üç kenar uzunluğu alarak,bu kenarlarla bir üçgen yapılabilir mi kontrol edelim. 
kenar1 = int(input("1. Kenar: "))
kenar2 = int(input("2. Kenar: "))
kenar3 = int(input("3. Kenar: "))

if((kenar2-kenar3) < kenar1 < (kenar2+kenar3)) and ((kenar1-kenar3) < kenar2 <( kenar1+kenar3)) and (kenar1-kenar2 < kenar3 < (kenar1+kenar2)):
	print("There can be triangle.")
else:
	print("SORRY: there can not be triangle.")


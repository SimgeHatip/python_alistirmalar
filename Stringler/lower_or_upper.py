#girilen bir kelimenin tamamı küçük harflerden mi oluşuyor?

kelime = input("Bir kelime yazınız: ")
if(kelime==kelime.lower()):
	print("Kelime tamamen küçük harflerden oluşuyor.")
else:
	print("Kelimede büyük harf bulunuyor.")

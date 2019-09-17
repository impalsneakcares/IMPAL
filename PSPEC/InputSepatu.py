print("====================================")
print("	   LAYANAN SEPATU    ")
print("Bronze: 20k (3 hari)  ")
print("Silver: 30k (2 hari)  ")
print("Gold  : 35k (1 hari)  ")
print("====================================")
mrk = str(input("Masukkan Merk Sepatu: "))
wrn = str(input("Masukkan Warna Sepatu: "))
lyn = str(input("Pilih layanan: "))

if(lyn == "Bronze" or lyn == "bronze"):
	print("Terimakasih, pesanan anda akan segera kami proses!\n")
	print("Sepatu anda dengan merk "+mrk+" berwarna "+wrn+" dengan layanan "+lyn)
elif(lyn == "Silver" or lyn == "silver"):
	print("Terimakasih, pesanan anda akan segera kami proses!\n")
	print("Sepatu anda dengan merk "+mrk+" berwarna "+wrn+" dengan layanan "+lyn)
elif(lyn == "Gold" or lyn == "gold"):
	print("Terimakasih, pesanan anda akan segera kami proses!\n")
	print("Sepatu anda dengan merk "+mrk+" berwarna "+wrn+" dengan layanan "+lyn)
else:
	print("Maaf, kami hanya memiliki 3 layanan")




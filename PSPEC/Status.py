#untuk input status pengerjaan dari staff
def Staff():
	statusnya = int(input("Statusnya: "))
	return (statusnya)

#informasi status pengerjaan untuk customer
def Customer():
	status = Staff()
	
	if status == 1:
		print("status: ")
		print("Picked up")

	elif status == 2:
		print("status pengerjaan: ")
		print("Dalam antrian")

	elif status == 3:
		print("status pengerjaan: ")
		print("Dicuci")

	elif status == 4:
		print("status pengerjaan: ")
		print("Pengeringan")

	elif status == 5:
		print("status pengerjaan: ")
		print("Selesai")

	elif status == 6:
		print("status: ")
		print("Delivered")
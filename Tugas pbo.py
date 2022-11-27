nama = "Mulham"
nim = "D0221418"
print("""Nama : {}
Nim : {}""".format(nama,nim))
print('''Pilihan Operasi
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga''')
perintah = input("Masukkan Perintah: ")
if perintah == '1':
	print("Menghitung Luas Persegi")
	p = int(input ( "Masukkan panjang : " ) )
	l = int( input ( "Masukkan lebar : " ) )
	persegi = p*l
	print ( "Luas persegi adalah : " + str ( persegi ) )
elif perintah == '2':
	print('Menghitung luas lingkaran')
	r = int(input('masukan jari-jari lingkaran: '))
	phi = 3.14
	L = phi * (r * r)
	print('Luas lingakaran dengan jari-jari {} adalah {}'.format(r, L))
elif perintah == '3':
	a = float(input("Masukkan panjang alas: ")) 
	t = float(input("Masukkan tinggi segitiga: ")) 
	luas = 0.5*a*t
	print("Luas segitiga adalah : "+ str(luas))
while True :
	print('''Pilihan Operasi
	
	1. Volume Bangun Ruang
	2. Luas Bangun Ruang''')
	print()
	p = int(input('Masukkan Pilihan Anda :'))
	if p == 1:
		print('''Pilihan Operasi
		
		1. Volume Kubus
		2. Volume Kerucut
		3. Volume Tabung''')
		print()
		o = int(input('Masukkan Pilihan Anda :'))
		if o == 1:
			print  ( "--- Program Menghitung Volume Kubus ---\n" )
			r = int(input('Panjang rusuk (cm) :'))
			v = r*r*r
			print ( "Volume Kubus adalah " + str (v ) + ' cm' )
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
				
		elif o == 2:
			print  ( "--- Program Menghitung Volume Kerucut ---\n" )
			tinggi= float ( input ( "Masukan Jari-jari Tinggi : " )) 
			jari= float ( input ( "Masukan Jari-jari Lingkaran : " ))
			phi = 22/7
			pelukis = (jari*jari)+(tinggi*tinggi)
			volume= int(1 / 3 *phi*jari*jari*tinggi)
			print  ( "Volume Kerucut  " ,  volume)
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
				
				
		elif o == 3:
			print  ( "--- Program Menghitung Volume Tabung ---\n" )
			a = int ( input ( "Masukkan Jari-jari : " ) )
			b = int ( input ( "Masukkan Tinggi : : " ) )
			c = 22/7
			hsl = int ( ( c* ( a*a ) ) *b )
			print ( "Luas volume adalah %d " % ( hsl ) )
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
		else :
			print()
			print('Periksa masukan anda!!')
			print()
		
	elif p == 2:
		print('''Pilihan Operasi
		
		1. Luas Kubus
		2. Luas Kerucut
		3. Luas Tabung''')
		print()
		b = int(input('Masukkan Pilihan Anda :'))
		if b == 1:
			print  ( "--- Program Menghitung Luas Kubus ---\n" )
			r = int(input('masukkan panjang rusuk :'))
			luas = 6*(r*r)
			print ( "Luas Kubus adalah " + str (luas ) + ' cm' )
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
				
		elif b == 2:
			import math
			print  ( "--- Program Menghitung Luas Kerucut ---\n" )
			tinggi= int ( input ( "Masukan Jari-jari Tinggi : " )) 
			jari= int ( input ( "Masukan Jari-jari Lingkaran : " ))
			phi = 22/7
			pelukis = math.sqrt((jari*jari)+(tinggi*tinggi))
			luas= int (phi*jari*(jari+pelukis))
			print  ( "Luas Kerucut " ,  luas) 
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
		elif b == 3:
			print  ( "--- Program Menghitung Luas Tabung ---\n" )
			a = int ( input ( "Masukkan Jari-jari : " ) )
			b = int ( input ( "Masukkan Tinggi : : " ) )
			c = 22/7
			hsl = int ( 2*c*a * (a+b))
			print ( "Luas volume adalah %d " % ( hsl ) )
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
		else :
			print()
			print('Periksa masukan anda!!')
			print()
	else:
		print()
		print('Periksa masukan anda!')
		print()
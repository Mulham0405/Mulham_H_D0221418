import math

class Volume:
    def __init__(self):
        self.sisi = 0
        self.panjang = 0 
        self.lebar = 0
        self.tinggi = 0
        self.jari_jari = 0
        self.phi = 22/7
        self.pelukis = math.sqrt
        

    def kubus(self):
        print("Volume Kubus:", self.sisi**3)
    
    def kerucut(self):
    	print("Volume kerucut",1 / 3 *self.phi*self.jari_jari*self.jari_jari*self.tinggi)

    def tabung(self):
        print("Volume Tabung:", math.pi * (self.jari_jari ** 2) * self.tinggi)

class Luas:
    def __init__(self):
        self.sisi = 0
        self.panjang = 0 
        self.lebar = 0
        self.tinggi = 0
        self.jari_jari = 0
        self.phi = 22/7
        self.pelukis = math.sqrt((self.jari_jari*self.jari_jari)+(self.tinggi*self.tinggi))
        
    def kerucut(self):
    	print("luas kerucut :",self.phi*self.jari_jari*(self.jari_jari+self.pelukis))

    def kubus(self):
        print("Luas Kubus:", 6 * (self.sisi**2))

    def tabung(self):
        print("Luas Tabung:", 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi))


volume = Volume()
luas = Luas()




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
			volume.sisi = r
			volume.kubus()
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
				
		elif o == 2:
			print  ( "--- Program Menghitung Volume Kerucut ---\n" )
			tinggi= float ( input ( "Masukan Jari-jari Tinggi : " )) 
			jari= float ( input ( "Masukan Jari-jari Lingkaran : " ))
			volume.jari_jari = jari
			volume.tinggi = tinggi
			print()
			volume.kerucut()
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
				
				
		elif o == 3:
			print  ( "--- Program Menghitung Volume Tabung ---\n" )
			a = int ( input ( "Masukkan Jari-jari : " ) )
			b = int ( input ( "Masukkan Tinggi : : " ) )
			volume.jari_jari = a
			volume.tinggi = b
			print()
			volume.tabung()
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
			s = int(input('masukkan panjang rusuk :'))
			luas.sisi = s
			print()
			luas.kubus()
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
				
		elif b == 2:
			print  ( "--- Program Menghitung Luas Kerucut ---\n" )
			tinggi= input ( "Masukan Jari-jari Tinggi : " )
			jari= float(input ( "Masukan Jari-jari Lingkaran : " ))
			luas.jari_jari = jari
			luas.tinggi = tinggi
			print()
			luas.kerucut()
			print('Lanjut atau tidak?')
			c = input('Jika lanjut ketik y, t kalau berhenti :')
			if c == 't':
				break
		elif b == 3:
			print  ( "--- Program Menghitung Luas Tabung ---\n" )
			a = int ( input ( "Masukkan Jari-jari : " ) )
			b = int ( input ( "Masukkan Tinggi : : " ) )
			luas.jari_jari = a
			luas.tinggi =  b
			print()
			luas.tabung()
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
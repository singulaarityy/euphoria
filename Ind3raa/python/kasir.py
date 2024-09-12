pembeli = input("Masukan Nama Anda: ")
print("Halo", pembeli, "mau pesan apa?")

def makanan():
    global totalmkn
    global porsi
    global mkn
    
    print("\n===============================")
    print("         Menu Makanan          ")
    print("===============================")
    print("1. Bakso          = Rp. 5000")
    print("2. Mie            = Rp. 5000")
    print("3. Roti Bakar     = Rp. 2000")
    print("4. Sate Kambing   = Rp. 10000")
    print("===============================\n")
    
    nomor = int(input("Nomor Berapa: "))
    
    if nomor > 4:
        print("\n------Tidak ada pilihan lagi------\n")  
        return makanan()
    
    porsi = int(input("Berapa Porsi: "))

    if nomor == 1: 
        totalmkn = porsi * 5000
        print()
        print(porsi, "Porsi Bakso = Rp.", totalmkn)
        mkn = "Bakso"
    elif nomor == 2:
        totalmkn = porsi * 5000
        print()
        print(porsi, "Porsi Mie = Rp.", totalmkn)
        mkn = "Mie"
    elif nomor == 3:
        totalmkn = porsi * 2000
        print()
        print(porsi, "Porsi Roti Bakar = Rp.", totalmkn)
        mkn = "Roti Bakar"
    elif nomor == 4:
        totalmkn = porsi * 10000
        print()
        print(porsi, "Porsi Sate Kambing = Rp.", totalmkn)
        mkn = "Sate Kambing"

makanan()
       
def minuman():
    global totalmnm
    global gelas
    global mnm

    print("\n===============================")
    print("         Menu Minuman           ")
    print("===============================")
    print("1. Teh           = Rp. 3000")
    print("2. Soda Gembira  = Rp. 5000")
    print("3. Es Mani       = Rp. 10000")
    print("4. Susu          = Rp. 5000")
    print("===============================\n")

    nomor = int(input("Nomor Berapa: "))

    if nomor > 4:
        print("\n------Tidak ada pilihan lagi------\n")  
        return minuman()
    
    gelas = int(input("Mau berapa Gelas: "))

    if nomor == 1:
        totalmnm=gelas*3000
        print()
        print(gelas,"Gelas Teh = Rp",totalmnm)
        mnm = "teh"
    elif nomor == 2:
        totalmnm=gelas*5000
        print()
        print(gelas,"Gelas Soda Gembira = Rp",totalmnm)   
        mnm = "Soda Gembira"
    elif nomor == 3:
        totalmnm=gelas*10000
        print()
        print(gelas,"Gelas Es Mani = Rp",totalmnm)  
        mnm = "Es Mani"  
    elif nomor == 4:
        totalmnm=gelas*5000
        print()
        print(gelas,"Gelas Susu = Rp",totalmnm)
        mnm = "Susu" 
    else:
        print()
        print("------Tidak ada pilihan lagi------")
        print() 
minuman()

# Membuat struk belanja
print("\n===============================")
print("         Struk Belanja         ")
print("===============================")
print("Nama Pelanggan:\t", pembeli)
print("===============================")
print("Porsi Makanan: ", porsi)
print("Makanan:",mkn, "= Rp.",totalmkn)
print("---------------------------------")
print("Gelas Minuman: ", gelas)
print("Minuman:",mnm, "= Rp.",totalmnm)
print("===============================")
total_belanja = totalmkn + totalmnm
print("Total Belanja= Rp.", total_belanja)
print()
print("Terima kasih telah berbelanja di toko kami!")
print("===============================")
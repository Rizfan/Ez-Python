from random import randint

def pilih_mode():
    print('\nPilih mode : ')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Campur')
    print('4. Akhiri Program')
    try:
        perintah = int(input("\nMasukkan Perintah (1-4) : "))
        if(perintah > 4 or perintah <= 0):
            print("\nProgram tidak mengenali perintah yang dimasukkan, Silahkan memilih dari perintah yang tersedia!")
            return pilih_mode()
        else:
            return mode(perintah)
    except ValueError:
        print("\nProgram tidak mengenali perintah yang dimasukkan, Silahkan memilih dari perintah yang tersedia!")
        return pilih_mode()

def mode(perintah):
    #mode penjumlahan
    if(perintah == 1):
        print("\n\nBaik, pilih mode penjumlahan ya, sekarang pilih jenis kuis apa?")
        return pilih_kuis(perintah)

    #mode pengurangan
    elif(perintah == 2):
        print("\n\nBaik, pilih mode pengurangan ya, sekarang pilih jenis kuis apa?")
        return pilih_kuis(perintah)
    
    #mode campur
    elif(perintah == 3):
        print("\n\nBaik, pilih mode campur ya, sekarang pilih jenis kuis apa?")
        return pilih_kuis(perintah)
    else:
        print("Program Berakhir")

def pilih_kuis(perintah):
    print('Pilih jenis kuis : ')
    print('1. Kuis Lepas')
    print('2. Kuis 5')
    print('3. Ganti Mode')
    print('4. Akhiri Program')
    try:
        jenis_kuis = int(input("\nMasukkan jenis kuis (1-4) : "))
        if(jenis_kuis > 4 or jenis_kuis < 0):
            print("Program tidak mengenali jenis kuis yang dimasukkan, Silahkan memilih dari jenis kuis yang tersedia!\n")
            return pilih_kuis(perintah)
        else:
            return kuis(jenis_kuis, perintah)
    except ValueError:
        print("Program tidak mengenali jenis kuis yang dimasukkan, Silahkan memilih dari jenis kuis yang tersedia!\n")
        return pilih_kuis(perintah)

def kuis(jenis_kuis, perintah):
    #kuis lepas
    if(jenis_kuis == 1):
        return kuis_lepas(perintah)
    
    #kuis 5
    elif(jenis_kuis == 2):
        return kuis_lima(perintah)

    #ganti mode
    elif(jenis_kuis == 3):
        return pilih_mode()
    
    #akhiri program
    else:
        print("Program Berakhir")

def kuis_lepas(perintah):
    #kuis penjumlahan
    if(perintah == 1):
        while True:
            a = randint(0,10)
            b = randint(0,10)
            print(f"\n\nBerapa {a} + {b}?")
            c = a+b
            jawab = input("Jawab : ")
            if(jawab.lower() == "akhiri kuis"):
                print("\n")
                return pilih_kuis(perintah)
            else:
                try:
                    jawab = int(jawab)
                    if(jawab == c):
                        print("Hore kamu benar!")
                    else :
                        print(f"Masih kurang tepat, ya. Jawabannya adalah {c}")
                except ValueError:
                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
    
    #kuis pengurangan
    elif(perintah == 2):
        while True:
            a = randint(0,10)
            b = randint(0,10)
            if(b > a):
                print(f"\n\nBerapa {b} - {a}?")
                c = b-a
            else: 
                print(f"\n\nBerapa {a} - {b}?")
                c = a-b
            jawab = input("Jawab : ")
            if(jawab.lower() == "akhiri kuis"):
                print("\n")
                return pilih_kuis(perintah)
            else:
                try:
                    jawab = int(jawab)
                    if(jawab == c):
                        print("Hore kamu benar!")
                    else :
                        print(f"Masih kurang tepat, ya. Jawabannya adalah {c}")
                except ValueError:
                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
    
    #kuis campur
    elif(perintah==3):
        
        while True:
            count = randint(1,10)
            a = randint(0,10)
            b = randint(0,10)
            if count % 2 != 0:
                print(f"\n\nBerapa {a} + {b}?")
                c = a+b
            else:
                if(b > a):
                    print(f"\n\nBerapa {b} - {a}?")
                    c = b-a
                else: 
                    print(f"\n\nBerapa {a} - {b}?")
                    c = a-b

            jawab = input("Jawab : ")

            if(jawab.lower() == "akhiri kuis"):
                print("\n")
                return pilih_kuis(perintah)
            else:
                try:
                    jawab = int(jawab)
                    if(jawab == c):
                        print("Hore kamu benar!")
                    else :
                        print(f"Masih kurang tepat, ya. Jawabannya adalah {c}")
                except ValueError:
                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
    
def kuis_lima(perintah):
    #kuis penjumlahan
    if(perintah == 1):
        nilai = 0
        for i in range(5):
            a = randint(0,10)
            b = randint(0,10)
            print(f"\n\nBerapa {a} + {b}?")
            c = a+b

            try:
                jawab = int(input("Jawab : "))
                if(jawab == c):
                    print("Hore kamu benar!")
                    nilai = nilai + 20
                else :
                    print(f"Masih kurang tepat, ya. Jawabannya adalah {c}")
            except ValueError:
                print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

        print(f"\nScore kamu : {nilai}\n\n")
        return pilih_kuis(perintah)

    #kuis pengurangan
    elif(perintah == 2):
        nilai = 0
        for i in range(5):
            a = randint(0,10)
            b = randint(0,10)
            if(b > a):
                print(f"\n\nBerapa {b} - {a}?")
                c = b-a
            else: 
                print(f"\n\nBerapa {a} - {b}?")
                c = a-b

            try:
                jawab = int(input("Jawab : "))
                if(jawab == c):
                    print("Hore kamu benar!")
                    nilai = nilai + 20
                else :
                    print(f"Masih kurang tepat, ya. Jawabannya adalah {c}")
            except ValueError:
                print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

        print(f"\nScore kamu : {nilai}\n\n")
        return pilih_kuis(perintah)

    #kuis campuran
    elif(perintah == 3):
        nilai = 0
        for i in range(5):
            count = randint(1,10)
            a = randint(0,10)
            b = randint(0,10)
            if count % 2 != 0:
                print(f"\n\nBerapa {a} + {b}?")
                c = a+b
            else:
                if(b > a):
                    print(f"\n\nBerapa {b} - {a}?")
                    c = b-a
                else: 
                    print(f"\n\nBerapa {a} - {b}?")
                    c = a-b

            try:
                jawab = int(input("Jawab : "))
                if(jawab == c):
                    print("Hore kamu benar!")
                    nilai = nilai + 20
                else :
                    print(f"Masih kurang tepat, ya. Jawabannya adalah {c}")
            except ValueError:
                print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

        print(f"\nScore kamu : {nilai}\n\n")
        return pilih_kuis(perintah)


print('Halo, Selamat Datang di Mathbot!')
pilih_mode()



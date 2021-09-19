print("Selamat datang di kalkulator IPK!")

jml_matkul = int(input("Masukkan Jumlah Mata Kuliah : "))

while(jml_matkul < 0):
    jml_matkul = int(input("Masukkan Jumlah Mata Kuliah : "))

sks_lulus = 0
total_sks = 0
mutu_lulus = 0
total_mutu = 0

for n in range(1, jml_matkul+1):
    nama_matkul = str(input(f"\nMasukkan nama mata kuliah ke-{n} : "))
    jml_sks = int(input("Masukkan Jumlah SKS "+nama_matkul+" : "))
    while(jml_sks < 0):
        print("Jumlah SKS yang kamu masukkan tidak valid")
        jml_sks = int(input("Masukkan Jumlah SKS "+nama_matkul+" : "))
    else:
        nilai = int(input(f"Masukkan nilai yang kamu dapatkan : "))
        while(nilai < 0 or nilai > 100):
            print("Nilai yang kamu masukkan tidak valid")
            nilai = int(input(f"Masukkan nilai yang kamu dapatkan : "))
        else:
            if(nilai <= 39):
                bobot = 0
            elif(nilai <= 54):
                bobot = 1
            elif(nilai <= 59):
                bobot = 2
            elif(nilai <= 64):
                bobot = 2.30
            elif(nilai <= 69):
                bobot = 2.70
            elif(nilai <= 74):
                bobot = 3
            elif(nilai <= 79):
                bobot = 3.30
            elif(nilai <= 84):
                bobot = 3.70
            else:
                bobot = 4
                    
            if(bobot <= 1):
                ket = "Tidak Lulus"
            else:
                ket = "Lulus"

            if (ket == "Lulus"):
                sks_lulus = jml_sks + sks_lulus
                mutu_lulus = jml_sks * bobot + mutu_lulus 

            total_sks = jml_sks + total_sks
            total_mutu = total_mutu + (jml_sks * bobot)

IPK = mutu_lulus/sks_lulus
IPT = mutu_lulus/total_sks

print(f"\nJumlah SKS lulus : {sks_lulus}/{total_sks}")
print(f"Jumlah mutu lulus : {mutu_lulus:.2f}/{total_mutu:.2f}")
print(f"Total IPK kamu adalah {IPK:.2f}")
print(f"Total IPT kamu adalah {IPT:.2f}")


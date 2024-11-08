import math

# Fungsi untuk validasi input
def validasi_input(input_value):
    try:
        nilai = float(input_value)
        if nilai > 0:
            return nilai
        else:
            print("Nilai harus positif!")
            return None
    except ValueError:
        print("Masukkan angka yang valid!")
        return None

# Fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

# Fungsi untuk menghitung luas persegi panjang (alas tabung)
def hitung_luas_persegi_panjang(tinggi, jari_jari):
    keliling_lingkaran = 2 * math.pi * jari_jari
    return keliling_lingkaran * tinggi

# Fungsi untuk menghitung luas permukaan tabung
def hitung_luas_permukaan_tabung(tinggi, jari_jari):
    luas_lingkaran = hitung_luas_lingkaran(jari_jari)
    luas_selimut = hitung_luas_persegi_panjang(tinggi, jari_jari)
    return (2 * luas_lingkaran) + luas_selimut

# Fungsi untuk menampilkan menu dan meminta pilihan
def tampilkan_menu():
    print("-----------------------------------------")
    print("Pilih Perhitungan:")
    print("1. Hitung Luas Lingkaran")
    print("2. Hitung Luas Persegi Panjang (alas tabung)")
    print("3. Hitung Luas Permukaan Tabung")
    print("4. Keluar")
    pilihan = input("Pilihan Anda : ")
    return pilihan

# Tampilan antarmuka awal
print("=========================================")
print("       Aplikasi Penghitung Luas")
print("=========================================")

while True:
    tinggi_input = input("Masukkan tinggi tabung (cm)    : ")
    jari_jari_input = input("Masukkan jari-jari lingkaran (cm) : ")

    tinggi = validasi_input(tinggi_input)
    jari_jari = validasi_input(jari_jari_input)

    if tinggi and jari_jari:
        pilihan = tampilkan_menu()

        if pilihan == '1':
            luas_lingkaran = hitung_luas_lingkaran(jari_jari)
            print(f"Luas Lingkaran: {luas_lingkaran:.2f} cm^2")
        elif pilihan == '2':
            luas_persegi_panjang = hitung_luas_persegi_panjang(tinggi, jari_jari)
            print(f"Luas Persegi Panjang: {luas_persegi_panjang:.2f} cm^2")
        elif pilihan == '3':
            luas_permukaan_tabung = hitung_luas_permukaan_tabung(tinggi, jari_jari)
            print(f"Luas Permukaan Tabung: {luas_permukaan_tabung:.2f} cm^2")
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid.")
    else:
        print("Input tidak valid. Program dihentikan.")
        break

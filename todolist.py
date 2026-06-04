daftar_tugas = []
status_tugas = [] # Isinya nanti cuma "Belum Selesai" atau "Selesai"

# Function 1: Untuk menampilkan menu utama
def tampilkan_menu():
    print("\nTO DO LIST")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")
    print("======================")

# Function 2: Untuk melihat semua tugas yang ada
def lihat_tugas():
    if len(daftar_tugas) == 0:
        print("\nBelum ada tugas yang dicatat.")
    else:
        print("\n--- DAFTAR TUGAS ANDA ---")
        # Perulangan FOR untuk nampilin list sama nomor urutnya 
        for i in range(len(daftar_tugas)):
            print(f"{i + 1}. [{status_tugas[i]}] {daftar_tugas[i]}")

# Function 3: Untuk menambah tugas baru
def tambah_tugas():
    tugas_baru = input("Masukkan nama tugas baru: ")
    if tugas_baru == "": 
        print("Nama tugas tidak boleh kosong!")
    else:
        daftar_tugas.append(tugas_baru)
        status_tugas.append("Belum Selesai") # Setiap tugas baru statusnya otomatis belum selesai
        print("Tugas berhasil ditambahkan!")

while True:
    tampilkan_menu()
    
    # Input pilihan menu dari user
    pilihan = input("Pilih menu (1-5): ")
    
    # Kondisi IF-ELSE buat jalanin fitur 
    if pilihan == "1":
        tambah_tugas()
        
    elif pilihan == "2":
        lihat_tugas()
        
    elif pilihan == "3":
        lihat_tugas()
        if len(daftar_tugas) > 0: # Cuman bisa jalan kalau ada tugasnya
            print("\n--- TANDAI SELESAI ---")
            nomor = int(input("Pilih nomor tugas yang sudah selesai: "))
            
            # Validasi agar nomor yang diinput ga ngawur
            if nomor > 0 and nomor <= len(daftar_tugas):
                status_tugas[nomor - 1] = "Selesai"
                print("Status tugas berhasil diperbarui!")
            else:
                print("Nomor tugas tidak ditemukan!")
                
    elif pilihan == "4":
        lihat_tugas() # Tampilin dulu tugasnya sebelum dihapus
        if len(daftar_tugas) > 0:
            print("\n--- HAPUS TUGAS ---")
            nomor = int(input("Pilih nomor tugas yang mau dihapus: "))
            
            # Validasi input nomor hapus
            if nomor > 0 and nomor <= len(daftar_tugas):
                # Menghapus data di kedua list berdasarkan index
                tugas_dihapus = daftar_tugas.pop(nomor - 1)
                status_tugas.pop(nomor - 1)
                print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")
            else:
                print("Nomor tugas tidak ditemukan!")
                
    elif pilihan == "5":
        print("\nProgram selesai. Terima kasih!")
        break # Whilenya stop
        
    else:
        # Validasi jika user ketik selain angka 1-5
        print("Pilihan salah! Silakan masukkan angka 1 sampai 5.")
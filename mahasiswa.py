import json

def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    jurusan = input("Masukkan jurusan mahasiswa: ")
    
    data_mahasiswa = {
        'nama': nama,
        'nim': nim,
        'jurusan': jurusan
    }
    
    return data_mahasiswa

def simpan_data(data):
    with open('data_mahasiswa.json', 'w') as file:
        json.dump(data, file)

def baca_data():
    try:
        with open('data_mahasiswa.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def update_data(nim):
    data = baca_data()
    for mahasiswa in data:
        if mahasiswa['nim'] == nim:
            nama = input("Masukkan nama mahasiswa: ")
            jurusan = input("Masukkan jurusan mahasiswa: ")
            mahasiswa['nama'] = nama
            mahasiswa['jurusan'] = jurusan
            simpan_data(data)
            print("Data mahasiswa berhasil diperbarui.")
            return
    print("NIM mahasiswa tidak ditemukan.")

def hapus_data(nim):
    data = baca_data()
    for mahasiswa in data:
        if mahasiswa['nim'] == nim:
            data.remove(mahasiswa)
            simpan_data(data)
            print("Data mahasiswa berhasil dihapus.")
            return
    print("NIM mahasiswa tidak ditemukan.")

def main():
    data = baca_data()
    
    while True:
        print("=== Aplikasi Pendataan Mahasiswa ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == '1':
            mahasiswa_baru = tambah_data()
            data.append(mahasiswa_baru)
            simpan_data(data)
            print("Data mahasiswa berhasil ditambahkan!")
        elif pilihan == '2':
            print("=== Data Mahasiswa ===")
            if len(data) > 0:
                for mahasiswa in data:
                    print("Nama   : ", mahasiswa['nama'])
                    print("NIM    : ", mahasiswa['nim'])
                    print("Jurusan: ", mahasiswa['jurusan'])
                    print("-------------------")
            else:
                print("Belum ada data mahasiswa.")
        elif pilihan == '3':
            nim = input("Masukkan NIM mahasiswa yang akan diperbarui: ")
            update_data(nim)
        elif pilihan == '4':
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            hapus_data(nim)
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()

######################## IMPORT ########################
import random
import getpass
from tabulate import tabulate

######################## HEADER ########################
header_acara = ['KODE TIKET',
                'EVENT',
                'QTY',
                'MIN UMUR',
                'TIPE TIKET',
                'HARGA']

######################## DATA UTAMA ########################
main_acara = [["TIX-5926",'WCU17 INA vs FRA',50000,17,'REG',250000],
            ["TIX-8873",'WCU17 INA vs FRA',20000,13,'VIP',450000],
            ["TIX-1537",'COLDPLAY CONCERT',30000,17,'REG',1500000],
            ["TIX-6281",'COLDPLAY CONCERT',12000,17,'VIP',4000000],
            ["TIX-3278",'COLOR RUN JAKARTA',800, 17,'REG',1500000],
            ["TIX-1652",'DAKWAH MAMA DEDEH',120,13,'REG',50000],
            ["TIX-1248",'DRUM MASTERCLASS 2023',80,17,'REG',1500000]]

######################## LIST KOSONG UNTUK MENAMPUNG DATA PEMBELI ########################
data_diri_pembeli = []

######################## FUNCTION KODE ACAK UNTUK KODE TIKET PADA DISPLAY ########################
def kode():
    while True:
        kode_input = f"TIX-{random.randint(1000, 9999)}"
        for i in range(len(main_acara)):
            if main_acara[i][0] == kode_input:     
                continue
        else:           
            return kode_input

######################## FUNCTION KODE ACAK UNTUK KODE PEMBELIAN TIKET ########################
def user_kode():
    while True:
        kode_input_user = f"USERTIX-{random.randint(1000, 9999)}"
        for i in range(len(data_diri_pembeli)):
            if data_diri_pembeli[i][0] == kode_input_user:     
                continue
        else:           
            return kode_input_user

######################## FUNCTION MENU AWAL ########################                             
def user_in():
    print("\n\n ~ ~ ~ Selamat datang di TiketKITA ! ~ ~ ~\n\n")
    print("""Masuk sebagai :
1. Admin
2. User
3. Exit Program""") 

######################## FUNCTION MENU ADMIN ########################
def fitur_admin():
    print("\n")
    print('Selamat datang,admin!\n')
    print('''Menu utama admin :
1. Buka list event
2. Tambah event
3. Menghapus tiket
4. Update Event          
5. Buka Data Pembeli
6. Logout
          ''')
    
######################## FUNCTION DISPLAY LIST EVENT ########################
def list_event():
    penampung_list_acara = []
    for i in range(len(main_acara)):
        penampung_list_acara.append([i + 1, main_acara[i][0], main_acara[i][1], main_acara[i][2], main_acara[i][3], main_acara[i][4], main_acara[i][5]])
    print(tabulate(penampung_list_acara, headers=["Nomor"] + header_acara))

######################## FUNCTION MENAMBAHKAN EVENT ########################
def add_event():
    print("\n")
    # Nama Event
    while True:
        a_event = input('Masukkan nama event : ').strip()
        if not a_event:
            print('Tidak boleh kosong')
        else:
            break
    # Kuantitas
    while True:
        b_qty = (input('Masukkan Jumlah tiket tersedia : '))
        if b_qty.isdigit() == False:
            print('Masukkan angka !!')
        else:
            break
    # Batasan umur
    while True:
        c_age = (input('Masukkan batasan umur : '))  
        if c_age.isdigit() == False:
            print('Masukkan angka !!')
        else:
            break
    # Tipe Tiket
    while True:
        d_type = input('Masukkan tipe tiket (REG/VIP): ').upper()
        if d_type == "VIP" or d_type == "REG":
            break
        else:
            print("Pilihan tipe hanya VIP/REG")
    # Harga
    while True:
        e_price = (input('Masukkan harga tiket : '))  
        if e_price.isdigit() == False:
            print('Masukkan angka !!')
        else:
            break
        
    main_acara.append([kode(),a_event.upper(),int(b_qty),int(c_age),d_type,int(e_price)])

######################## FUNCTION MENU HAPUS ########################
def opsi_hapus():
    print('''Silahkan pilih opsi hapus : 
1. Lanjut menghapus dengan Kode event
2. Cari kode event dengan nama
3. Menu Sebelumnya          
          ''')

######################## FUNCTION HAPUS ########################
def hapus():  
    while True: 
        hapus = input('Masukkan kode tiket yang ingin dihapus :  ')
        con_hapus2 = 0
        for i in range(len(main_acara)):
            if hapus.isdigit() and hapus in main_acara[i][0] and len(hapus) == 4 :
                main_acara.pop(i)
                con_hapus2 = 1
                break
        if con_hapus2 == 0:
            print('kode Tiket tidak ditemukan')      
        else :
            break   

######################## FUNCTION MENU ADMIN CARI DATA BY NAMA EVENT UNTUK KODE LALU HAPUS ########################
def cari_nama_hapus():
    while True:
        nama_hapus = input('Masukkan Nama Event yang ingin anda hapus : ')
        tampung_data_hapus = []
        header_acara = ['KODE TIKET', 'EVENT', 'QTY', 'MIN UMUR', 'TIPE TIKET', 'HARGA']
        con_hapus = 0
        
        for i in range(len(main_acara)):
            if nama_hapus.upper() in main_acara[i][1].upper():
                tampung_data_hapus.append([i + 1, main_acara[i][0], main_acara[i][1], main_acara[i][2], main_acara[i][3], main_acara[i][4], main_acara[i][5]])
                con_hapus += 1
        
        if con_hapus == 0:
            print('Event Tidak Ada !')
        else:
            print(tabulate(tampung_data_hapus, headers=["Nomor"] + header_acara))
            hapus()
            break

######################## FUNCTION MENU UPDATE ########################
def opsi_update():
    print('''
1. Update by Ticket Code
2. Search Event name
3. Menu Sebelumnya              
''')

######################## FUNCTION UPDATE ########################
def update():        
    while True:
        con_update = 0
        n = input('Masukkan kode : ')
        for i in range(len(main_acara)):
            if n in main_acara[i][0] and len(n) == 4:
                con_update = 1

                nama_baru = input('Masukkan Update nama : ').upper()
                main_acara[i][1] = nama_baru
                
                while True:
                    qty_baru = input('Masukkan update jumlah tiket : ')
                    if qty_baru.isdigit() == False:
                        print('Masukkan angka !!')
                    else:
                        main_acara[i][2] = int(qty_baru)
                        break

                while True:
                    age_baru = input('Masukkan update minimal umur :  ')
                    if age_baru.isdigit() == False:
                        print('Masukkan angka !!')
                    else:
                        main_acara[i][3] = int(age_baru)
                        break

                while True:
                    price_baru = input('Masukkan update harga :  ')
                    if price_baru.isdigit() == False:
                        print('Masukkan angka !!')
                    else:
                        main_acara[i][5] = int(price_baru)
                        break
                break
        else:
            print('Kode tidak ditemukan')
        if con_update == 1:
            break

######################## FUNCTION MENU ADMIN CARI DATA BY NAMA EVENT UNTUK KODE LALU UPDATE ########################
def cari_nama_update():
    while True:
        nama_update = input('Masukkan Nama Event yang ingin anda update : ')
        tampung_data_update = []
        header_acara = ['KODE TIKET', 'EVENT', 'QTY', 'MIN UMUR', 'TIPE TIKET', 'HARGA']
        
        for i in range(len(main_acara)):
            if nama_update.upper() in main_acara[i][1].upper():
                tampung_data_update.append([i + 1, main_acara[i][0], main_acara[i][1], main_acara[i][2], main_acara[i][3], main_acara[i][4], main_acara[i][5]])
            
        if tampung_data_update:
            print(tabulate(tampung_data_update, headers=["Nomor"] + header_acara))
            update()
            break
        else:
            print('Nama Tidak Ditemukan !')

######################## FUNCTION UNTUK DATA PEMBELI ########################            
def data_pembeli():
    print('Data pembeli : ')
    penampung_data_pembeli = []
    header_pembeli = ['Kode Pembelian', 'Event', 'Tipe Tiket', 'Qty Tiket', 'Nama Pembeli', 'Umur', 'No.ID', 'No.Telepon']
    
    for i in range(len(data_diri_pembeli)):
        penampung_data_pembeli.append([data_diri_pembeli[i][0], data_diri_pembeli[i][1], data_diri_pembeli[i][2], data_diri_pembeli[i][3], data_diri_pembeli[i][4], data_diri_pembeli[i][5], data_diri_pembeli[i][6], data_diri_pembeli[i][7]])
    
    print(tabulate(penampung_data_pembeli, headers=header_pembeli))

######################## FUNCTION MENU USER ########################
def fitur_user():
    print('''Menu utama User :
1. Buka Daftar Tiket
2. Cari Tiket
3. Beli Tiket
4. Menu Sebelumnya
''')
    
######################## FUNCTION MENU USER CARI DATA DARI KODE TIKET ########################
def user_cari_tiket():
    while True:
        cari_tiket_user = input('Masukkan Nama tiket : ')
        list_cari_tiket_user = []
        header_acara = ['KODE TIKET', 'EVENT', 'QTY', 'MIN UMUR', 'TIPE TIKET', 'HARGA']
        
        for i in range(len(main_acara)):
            if cari_tiket_user.upper() in main_acara[i][1].upper():
                list_cari_tiket_user.append([i + 1, main_acara[i][0], main_acara[i][1], main_acara[i][2], main_acara[i][3], main_acara[i][4], main_acara[i][5]])

        if list_cari_tiket_user:
            print(tabulate(list_cari_tiket_user, headers=["Nomor"] + header_acara))
            break
        else:
            print('Tiket Tidak ada')

######################## FUNCTION MENU USER BELI TIKET ########################
def beli_tiket():
    while True:
        keranjang_tiket = []
        kode_tiket_beli = input('Masukkan Kode tiket yang akan dibeli : ')
        if kode_tiket_beli.isdigit() and len(kode_tiket_beli) == 4:
            for i in range(len(main_acara)):
                if kode_tiket_beli in main_acara[i][0] and kode_tiket_beli.isdigit() and len(kode_tiket_beli) == 4:
                    while True:
                        qty_beli = (input('Masukkan Jumlah tiket yang akan anda beli : '))
                        if qty_beli.isdigit() == True and (0 < int(qty_beli) <= 2) :
                            if int(qty_beli) <= main_acara[i][2]:
                                keranjang_tiket.append([main_acara[i][1],int(qty_beli),main_acara[i][5]])
                                main_acara[i][2] -= int(qty_beli)     
                                
                                for k in range(len(keranjang_tiket)):          
                                    print("|Nama Event\t\t|Jumlah Tiket\t\t|harga total")
                                    print(f"|{keranjang_tiket[k][0]}\t\t|{keranjang_tiket[k][1]}\t\t|{keranjang_tiket[k][2]*keranjang_tiket[k][1]}")
                                    print('Silahkan Isi data pembelian tiket anda : ')

                                while True:
                                    data_nama = input('Masukkan nama anda : ').upper()
                                    if data_nama.replace(' ','').isalpha():
                                        break
                                    else:
                                        print('Nama hanya karater')

                                while True:
                                    data_umur = input('Masukkan umur anda : ')
                                    if data_umur.isdigit() and int(data_umur) >= main_acara[i][3]:
                                        break
                                    else:
                                        print('Masukkan angka / batasan umur tidak sesuai!')

                                while True:
                                    data_ID  = input('Masukkan nomor Identitas anda (10-16 digit): ')
                                    if data_ID.isdigit() and 10 <= len(data_ID) <= 16:
                                        break
                                    else:
                                        print('Masukkan angka min 10 dan max 16 digit!')
                                                                                        
                                while True:
                                    data_tlp  = input('Masukkan nomor Telefon anda (10-12 digit) : ')
                                    if data_tlp.isdigit() and 10 <= len(data_tlp) <= 12: 
                                        break
                                    else:
                                        print('Masukkan angka min 10 dan max 12 digit !')
                                
                                while True:
                                    print(f'Total yang harus anda bayar adalah : Rp.{keranjang_tiket[k][1]*keranjang_tiket[k][2]}')
                                    try:
                                        bayar = int(input('Masukkan Uang yang ingin anda bayar : '))
                                        if keranjang_tiket[k][1]*keranjang_tiket[k][2] > bayar:
                                            print(f'Pembayaran Dibatalkan, Uang anda kurang Rp.{(keranjang_tiket[k][1]*keranjang_tiket[k][2])-(bayar)}')
                                            continue
                                        elif keranjang_tiket[k][1]*keranjang_tiket[k][2] < bayar :
                                            print(f'Pembayaran Dibatalkan, nominal tidak sesuai dengan total bill ')
                                            continue
                                        else:
                                            print('\n')
                                            print('Pembayaran berhasil, selamat menikmati acara anda!')
                                            print('\n')
                                        data_diri_pembeli.append([user_kode(), main_acara[i][1], main_acara[i][4], qty_beli, data_nama, int(data_umur), data_ID, data_tlp])
                                        break
                                    except ValueError:
                                        print('Masukkan nominal angka !')    
                                break
                            else:
                                print(f'Tidak cukup beli {qty_beli} tiket, tiket tersisa {main_acara[i][2]}')
                        else:
                            print('Masukkan Jumlah yang benar, maximal 2 tiket !') 
            break
        else:
            print("Kode tidak tersedia, Masukkan kode yang benar ! ")  

######################## MAIN FUNCTION ########################
while True:
    try:
        while True:
            ######################## INPUT UNTUK MASUK MENU UTAMA ########################
            user_in()
            masuk = int(input('Masuk sebagai : '))
            ######################## INPUT 1 UNTUK MASUK SEBAGAI ADMIN ########################
            if masuk == 1: 
                ######################## INPUT PASSWORD ADMIN ########################
                ######################## ADMIN LOGIN ########################
                password = getpass.getpass("Masukkan password: ")        
                if password == '12345':
                    while True:
                        try:
                            fitur_admin()           
                            admin = int(input('Silahkan pilih fitur admin : \n'))
                            ######################## FITUR 1 ADMIN "TAMPILKAN DATA" ########################
                            if admin == 1:
                                list_event()
                            ######################## FITUR 2 ADMIN "TAMBAH DATA" ########################    
                            elif admin == 2:
                                list_event()
                                add_event()
                                list_event()                
                            ######################## FITUR 3 ADMIN "HAPUS DATA" ########################    
                            elif admin == 3:
                                list_event()
                                while True:
                                    try:
                                        opsi_hapus()
                                        search_hapus = int(input('Masukkan opsi hapus : '))
                                        ######################## SUBFITUR 1 ADMIN HAPUS "HAPUS DENGAN KODE TIKET" ########################
                                        if search_hapus == 1 :
                                            hapus()
                                            list_event()
                                        ######################## SUBFITUR 2 ADMIN HAPUS "CARI KODE TIKET DENGAN KEYWORD NAMA LALU HAPUS DENGAN KODE" ########################    
                                        elif search_hapus == 2 :
                                            cari_nama_hapus()
                                            list_event()
                                        ######################## KEMBALI KE MENU SEBELUMNYA (FITUR ADMIN) ########################
                                        elif search_hapus == 3:
                                            break
                                        else:
                                            print('Pilihan hanya 1-3')
                                    except:
                                        print('Opsi Tidak tersedia')
                                print('List setelah dihapus')
                                print("\n")
                                list_event()               
                            ######################## FITUR 4 ADMIN "UPDATE DATA" ########################    
                            elif admin == 4:
                                list_event()
                                while True:
                                    try:    
                                        opsi_update()
                                        search_update = int(input('Masukkan Opsi Pencarian : '))
                                        ######################## SUBFITUR 1 ADMIN UPDATE "UPDATE DENGAN KODE TIKET" ########################
                                        if search_update == 1:
                                            update()
                                            list_event()
                                        ######################## SUBFITUR 2 ADMIN UPDATE "CARI KODE TIKET DENGAN KEYWORD NAMA LALU UPDATE DENGAN KODE" ########################
                                        elif search_update == 2:
                                            cari_nama_update()
                                        ######################## KEMBALI KE MENU SEBELUMNYA (FITUR ADMIN) ########################    
                                        elif search_update == 3:
                                            break
                                        else:
                                            print('Pilihan hanya 1-3')
                                    except:
                                        print('Pilihan Tidak Tersedia')
                                list_event()
                            ######################## FITUR 5 ADMIN "TAMPILKAN DATA PEMBELIAN" ########################    
                            elif admin == 5:
                                print("\n")
                                data_pembeli()
                                print("\n")
                            ######################## ADMIN LOGOUT ########################    
                            elif admin == 6:
                                break                 
                            else : 
                                print('Pilhan fitur admin yang tersedia hanya 1-4')
                        except:
                            print('Pilihan tidak tersedia')
                else :
                    print('Password Salah!')      
            ######################## INPUT 2 UNTUK MASUK SEBAGAI USER ########################                
            elif masuk == 2:
                while True:
                    try:
                        fitur_user()
                        user = int(input('Silahkan pilih fitur user : '))
                        ######################## FITUR 1 USER "TAMPILKAN DATA" ########################
                        if user == 1:
                            list_event()
                        ######################## FITUR 2 USER "CARI DATA DENGAN KEYWORD NAMA" ########################    
                        elif user == 2:
                            list_event()
                            print("\n")
                            user_cari_tiket()
                            print("\n")
                        ######################## FITUR 3 USER BELI TIKET ########################    
                        elif user == 3:
                            list_event()
                            beli_tiket()
                        ######################## DARI MENU USER KEMBALI KE MENU MASUK ########################               
                        elif user == 4:
                            break                   
                        else: 
                            print('Pilhan fitur user yang tersedia hanya 1 -3 ')
                    except:
            
                        print('Pilihan Tidak Tersedia')
            ######################## INPUT 2 UNTUK EXIT PROGRAM ########################
            elif masuk == 3:
                break      
            else:
                print('Opsi Hanya 1-3')
    except:
        print('Pilihan tidak tersedia')
import time
def clear_screan():
    print('\033c', end="")
def display_menu():
    clear_screan()
    print('=' *35)
    print('KALKULATOR SEDERHANA')
    print('=' *35)
    print('pilihan')
    print('1.tambah')
    print('2.kali')
    print('3.kurang')
    print('4.bagi')
    print('5.keluar')
    print('=' *35)

def tambah(x,y):   
    return x + y
def kali(x,y):
    return x * y
def kurang(x,y):
    return x - y
def bagi(x,y):
    if y == 0 :
        print('tidak bisa di bagi 0')
        return None
    return x / y

while True:
    display_menu()
    pilihan = input('masukkan penjumblahan yang inging di jumbelahkan 1/2/3/4 ' )



    if pilihan not in('1','2','3','4'):
      print('pilihan tidak ada silahkan tekan enter untuk keluar')
      continue

    if pilihan ==5:
        print('keluar dari kalkulator')
    break
    
angka1 = float(input('masukkan pilihan pertama '))
angka2 = float(input('masukkan pilihan kedua '))

if pilihan =='1':
    hasil = tambah (angka1, angka2)
    print(f'hasil: {angka1} + {angka2} = {hasil}')
elif pilihan =='2':
    hasil = kali (angka1, angka2)
    print(f'hasil: {angka1} * {angka2} = {hasil}')
elif pilihan =='3':
    hasil = kurang (angka1, angka2)
    print(f'hasil: {angka1} - {angka2} = {hasil}')
elif pilihan =='4':
    hasil = bagi (angka1, angka2)
    print(f'hasil: {angka1} / {angka2} = {hasil}')
    if hasil is not None:
        print(f'hasil: {angka1} / {angka2} = {hasil}')

input('tekan enter untuk keluar')
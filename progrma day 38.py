print("perulangan bersarang atau bertingkat")
print('contoh pertama')
for i in range(0,3+1):
    print('perulangan luar [i]=',i)
    for j in range(5):
        print('perulangan luar[i][j]=',i,j)
#perulangan bertingkat itu akan pertama mengeksekusi bagian perulangan pertama dan
#perulangan di dalamnya akan di ulang sesuai perulangan pertama
#contoh apa bila prulangan pertma di ulang sebanyak 3 dan perulangan ke 5 maka jumlah ke seluruha yang
#yang di ulang itu 3 * 5 =15

print('contoh ke 2')            #baris maksudnya untuk membuat berapa anyak # vertikal
for baris in range (2):         # kolom artinya panjang ke samping atau banyak # horizontal
    for kolom in range(7):
        print( '#', end = ' ')
    else:
        print('')

print('atau')
for baris in range (2):
    print('* ', end = '')
    for kolom in range(5):
        print( '#' '@' , end = ' ')
    else:
        print('')

print('menggunakan while')
listkota=['jakarta','surabaya','makassar']
kota=[]
for i in listkota:
    print(kota)
    while listtempat:
        print('--->',listtempat.pop(0))

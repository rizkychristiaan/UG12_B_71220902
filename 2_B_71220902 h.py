print ("~~~ Selamat datang di kalkulator sederhana ~~~")
a = input("Masukan operator matematika yang ingin anda hitung: ")
while True:
    if a == '+':
        angka1 = int(input("mau penjumblahan brapa: "))
        angka2 = int(input("print berapa banyak: "))
        for i in range(angka2):
            print(f'{i+1} + ')


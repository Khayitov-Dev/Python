
# dostlar = ['ali','vali','sherali','jumanazar','oybek','amir temir']
#            0      1      2          3          4         5

# dostlar[0] = 'bobo'
# a = dostlar.count('ali')
# print(a)
# raqamlar = [1432,334,5,63457,8,344]
# print(raqamlar)



# raqamlar.append(10)
# print(raqamlar)

# dostlar.insert(0, 'bobo')
# print(dostlar)

# raqamlar.remove(1)
# print(raqamlar)

# raqamlar.clear()
# print(raqamlar)

# raqamlar.pop(-4)
# print(raqamlar)

# dostlar.pop(3)
# print(dostlar)

# dostlar.sort()
# print(dostlar)

# raqamlar.sort()
# print(raqamlar)

# dostlar.reverse()
# print(dostlar)

# dostlar1 = dostlar.copy()
# print(dostlar1)

# print(dostlar)
# print(len(dostlar))
# print(raqamlar)
# print(len(raqamlar))



# dostlar.extend(raqamlar)
# print(dostlar)
# print(len(dostlar))




# print(dostlar)
# print(dostlar[-1].upper())
# print(dostlar[2:4])
# print(dostlar[-1].upper().isupper())

# print(len(dostlar))
# print(len(raqamlar))
# print(dostlar.index('ali'))
# print(dostlar[0])



# dostlar = ('ali','vali','sherali','jumanazar','oybek','oybek','oybek','amir temir')


# print(type(dostlar))

# dostlar[0] = 'bobo'
# print(dostlar)


# soni = dostlar.count('oybek')
# print(soni)


# print(dostlar[1:3])

# kordinatalar = [(1,2),(2,3),(23,121),(213,231)]
# print(kordinatalar)
# kordinatalar[1] = (32,32)
# print(type(kordinatalar))
# print(kordinatalar)


#>>>>>>>>>>>>>>>>>>>>>>>>> RANGE <<<<<<<<<<<<<<<<<<<<<<<<<<<

# sonlar = list(range(1,100))
# print(sonlar)

# juft_sonlar = list(range(0,20,2))
# toq_sonlar = list(range(1,20,2))

# print(f'Bu juft sonlar: {juft_sonlar}')
# print(f'Bu toq sonlar {toq_sonlar}')



# for son in range(100):
#     print(son**2)


# mashinist = ['Ali','oybek','sheroz','javohir','maruf','islom']

# for mashina in mashinist:
#     print(f"Hurmatli {mashina.title()} sizni 20 Mart kuni soat 21:00 da Malibu rusmli mashinangiz tayyor bo'ladi!")
# print("Hurmat bilan 'GM'!")







# sonlar = list(range(31))

# sonlar_kubi = []

# for son in sonlar:
#     sonlar_kubi.append(son**3)
# print(f'Bu sonlar: {sonlar}')
# print(f'Bu sonlarning kubi: {sonlar_kubi}')


# my_tuple = ('max',12,'toshkent')

# name,age,city = my_tuple

# print(f"Ismi {name.title()} Yoshi {age} Manzili {city.upper()}")

# yil = 2022
# ism = input('Ismingizni kiriting:\n>>>')
# familiya = input('Familiyangizni kiriting:\n>>>')
# yosh = int(input('Yoshingizni kiriting:\n>>>'))
# manzil = input('Manzilingizni kiriting:\n>>>')



# print(f"Asslomu alaykum {ism.title()} {familiya.title()} Tug'ilgan yilingizni: {yil-yosh} Manzilingiz: {manzil.title()}")




# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

# ismlar = ['Ali','Vali','Hasan','Husan','Olim']
# for ism in ismlar:
#     print(f"Assalom alaykum, {ism.title()}. Xush kelibsiz!")
# print(f"Kod {len(ismlar)} marta takrorlandi")




# kinolar = []
# print("5 ta sevimli kinoingiz qaysilar?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)    

# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)





# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, 
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.


# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing.
# Ro'yxatni konsolga chiqaring.




# kirish = int(input('Qatorlar sonini kiriting: '))

# for qator in range(1, kirish+1):
#     for ustun in range(1, qator+1):
#         print("*", end=" ")
#     print()


# import sys
# my_list = [0, 1, 2, "hello", True]
# my_tuple = (0, 1, 2, "hello", True)
# print(sys.getsizeof(my_list), 'bytes')
# print(sys.getsizeof(my_tuple), 'bytes')

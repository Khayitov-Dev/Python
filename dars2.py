# O'zgaruvchilar va String(Matnlik Habar)


# ism = 'Ali'
# familiya = 'Valiyev'

# print(ism + " " + familiya)



# ism = 'Ozod'
# familiya = 'Alisherov'
# yosh = 45

# print(f" Mening ismim: {ism},\n familiyam {familiya}\t yoshim: {yosh} da!")

# UPPER, LOWER, TITLE

# ism = 'jaVlon'
# familiya = 'shodMonov'

# ism_sharif = ism +" "+ familiya

# print(ism_sharif.upper())
# print(ism_sharif.upper().isupper())

# print(ism_sharif.lower())
# print(ism_sharif.lower().islower())

# print(ism_sharif.title())
# print(ism_sharif.title().istitle())

# print(ism_sharif.capitalize())



# moshina = '                       Malibu                        '
# print(moshina)
# print(f"Mening mashinam {moshina.rstrip()} edi!")
# print(f"Mening mashinam {moshina.lstrip()} edi!")
# print(f"Mening mashinam {moshina.strip()} edi!")




# markaz = '                       marvel                        '
# print(f"Bizning o'quv markazimiz {markaz.title().strip()}")
# print(len(markaz))



# markaz = "Marvell Academy"
# #         0123456

# print(markaz[0],markaz[1],markaz[2],markaz[3],markaz[4],markaz[5],markaz[6])

# print(markaz.index('a'))








# ism = input("Ismingiz nima?\n>>>")
# print(f"Asslaomu alaykum {ism.title()}")



# ism = input("Ismingiz nima?\n>>>")
# familiya = input("Familiyangiz nima?\n>>>")
# yil = 2022
# yosh = int(input("Qachon tug'ilgansiz?\n>>>"))

# print(f" Asslaomu alaykum {ism.title()} {familiya.title()}.\n Sizning yoshingiz {yil-yosh}da!")


# print("5+3")
# print(5+3)


















# Integer,Float yoki Sonlar bilan ishlash


from math import *


# print(pow(5,5))

# print(max(1,2,121,2112,1212,12,3,332,212,121,2121,213,23,234,42))
# print(min(1,2,121,2112,1212,12,3,332,212,121,2121,213,23,234,42))

# print(round(123.5))
# print(floor(123.5))
# print(ceil(123.5))
# print(sqrt(36))




# son1 = float(input("Birinchi sonni kiriting:\n>>> "))
# son2 = float(input("Ikkinchi sonni kiriting:\n>>> "))

# print(f"Javob: {son1+son2}")


# x = int(input("Istalgan son kirting:\n>>>"))
# print(x, ' ning kvadrati ', x**2, ' ga teng!')



# yosh = int(input("Yoshingiz nechida?\n>>>"))
# t_yil = 2022-yosh

# print("Siz ", t_yil, " da tug'ilgansiz!")


# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# print(f"{a} + {b} =", a+b)
# print(f"{a} - {b} =", a-b)
# print(f"{a} x {b} =", a*b)
# print(f"{a} / {b} =", a/b)
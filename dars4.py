# kirish = int(input('Qatorlar sonini kiriting: '))

# for qator in range(1, kirish+1):
#     for ustun in range(1, qator+1):
#         print("*", end=" ")
#     print()

# import sys

# my_list = [0,1,2, "salom",True]
# my_tuple = (0,1,2, "salom",True)

# print(sys.getsizeof(my_list), 'bytes')
# print(sys.getsizeof(my_tuple), 'bytes')











# ismlar = ['ali','salim','doston','polat','yamach']

# for ism in ismlar:
#     if ism == 'yamach':
#         print(ism.upper())
#     else:
#         print(ism.title())

# ismlar = str(input('Ismingiz nima>>>'))

# if ismlar == 'yamach' or ismlar == 'oybek':
#     print('Hush kelibsiz')
# else:
#     print('Biz sizni kutmadik!')

# yosh = int(input('Yoshingiz nechida:>>>'))

# if yosh == 100:
#     print('Siz bir asr yashadingiz!')
# elif yosh >= 18:
#     print('Siz kattasiz!')
# elif yosh < 0:
#     print("Siz hali tavallud topmagansiz!")
# else:
#     print('Siz yosh bolasiz!')


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: 
#     price = 0
# elif yosh<=12: 
#     price = 5000
# elif yosh<65:
#     price = 10000
# else:
#     price = 8000
# print(f"Sizga kirish {price} so'm")


# num1 = float(input('Birinchi sonni kiriting:\n>>>'))
# op = input('Operator kiriting:\n>>>')
# num2 = float(input('Ikkinchi sonni kiritng:\n>>>'))


# if op == '+':
#     print(f'Javob: {num1+num2}')
# elif op == '-':
#     print(f'Javob: {num1-num2}')
# elif op == '/':
#     print(f'Javob: {num1/num2}')
# elif op == '*':
#     print(f'Javob: {num1*num2}')
# else:
#     print('Xato operator kiritdingiz')


# son = float(input("Juft son kiriting: "))
# if son % 2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")


# users = ['alisher','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")








# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va
# foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
# va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.















# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")


son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
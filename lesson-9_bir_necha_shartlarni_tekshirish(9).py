# 9 - Dars: Bir nechta shartlarni tekshirish
# Muallif : Omadbek
# Sana : 8.04.2023

  # if-elif-else ketma-ketligi:
    
#yosh = int(input("Yoshingiz nechida?\n>>>"))
#if yosh <= 4:
 #   print("Sizga kirish bepul.")
#elif yosh <= 12:
#    print("Sizga kirish 5000 so'm.")
#else:
#    print("Sizga kirish 10000 so'm.")

 # Kod yozishda yaxshi amaliyotlardan biri, kodlarni qisqa yozish va buyruqlarni
# qayta-qayta takrorlamaslik. Shuning uchun print() qayta-qayta yozish o'rniga
# biror o'zgaruvchidan foydalandik.(masalan - price)

#yosh = int(input("Yoshingiz nechida?\n>>>"))
#if yosh <= 4:
 #   price = 0
#elif yosh <= 12:
#    price = 5000
#else:
#    price = 10000
#print(f"Sizga kirish {price} so'm.")

#if-elif-else zanjirida bit nechta elif lar bo'lishi mumkin. Misol uchun, hayvonot
# bog'i qariyalar uchun chegirma e'lon qilsa, kodimizni quyidagicha 
# o'zgartirishimiz mumkin:
    
# yosh = int(input("Yoshingiz nechida? \n>>>"))
#if yosh <= 4:
 #   price = 0
#elif yosh <=12:
#    price = 5000
#elif yosh <=65:
 #   price = 10000
#else :
 #   price = 8000
#print(f"Sizga kirish {price} so'm.")

# if-elif-else zanjirida ham else qismi majburiy emas:
#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
 #   price = 0
#elif yosh<=12:
 #   price = 5000
#elif yosh<65:
 #   price = 10000
#elif yosh>=65:
#    price = 8000    
#print(f"Sizga kirish {price} so'm")

#or operatori.

# kun = input("Bugun nima kun? \n>>> ")
#if kun.lower() == "shanba" or kun.lower() == "yakshanba":
 #   print("Bugun dam olish kuni.")
#else:
 #   print("Bugun ish kuni.")

#budget = int(input("Ushbu qurilma uchun qancha mablag' sarflamoqchisiz? \n> "))
#if budget == 3000  or budget > 3000:
 #   print("Siz ushbu qurilma uchun yetarli mablag'ga egasiz.")
#else:
 #   print("Sizning mablag'ingiz yetarli emas.")

# and operatori
#kun = input("Bugun qaysi kun? \n> ")
#harorat = float(input("Havo harorati necha gradus? \n> "))
#if kun.lower() == "yakshanba" and harorat >= 30:
#    print("Cho'milgani kettik.")
#else:
#    print(("Uyda dam olamiz."))

#mobile = input("Qaysi turdagi telefon harid qilmoqchisiz? \n> ")
#price = int(input("Telefon harid qilish uchun qancha mablag'ga egasiz? \n> "))
#if mobile.lower() == "iphone" and price >= 4100:
 #   print("Bizda siz uchun ko'p tanlovlar mavjud.😉")
#else:
 #   print("Kechirasiz, bizdan ushbu turdagi haridni amalga oshirolmaysiz. 😩")

# Bir necha shartlarni ketma-ket yozishimiz mumkin:
#kun = input("Bugun qaysi kun? \n> ")
#harorat = float(input("Bugun havo harorati qanday? \n> "))
#if kun.lower() == "shanba" or kun.lower() == "yakshanba" and harorat >= 30:
 #   print("Cho'milgani kettik.")
#elif kun.lower() == "shanba" or kun.lower() == "yakshanba" and harorat <= 30:
 #   print("Bugun uyda dam olamiz.")

# Boolean ma'lumot turi
#narh = 15000 # mijoz 15000 ga taom oldi.
#choy = True # mijoz choy ham oldi.(Choy narxi 5000 edi.)
#salat = False # mijoz salat olmadi.(salat narxi 5000 edi)
#if choy and salat:# agar mijoz choy ham salat ham olgan bo'lsa...
 #   narh = narh + 10000 # narhga 10000 qoshamiz.
#elif choy or salat:# agar mijoz choy yoki salat olgan bolsa...
#    narh = narh + 5000# narxga 5000 qo'shamiz.
#print(f"Jami {narh} so'm.") #yakuniy narxni chiqaramiz.

#Boolean o'zgaruvchilarni saqlashda TRUE va FALSE qiymatlari o'rniga 
# 1 va 0 sonlarini ham ishlatish mumkin.
#shoes = 2000 # mijoz 2000 ga oyoq kiyim oldi.
#shirt = 1 # mijoz ko'ylak ham oldi.(narhi 1000 edi)
#trouser = 0 # mijoz ko'ylak olmadi. (narhi 1000 edi)
#tie = 1 # mijoz ko'ylak ham oldi. (narhi 1000 edi)
#suit = 0 # mijoz ko'ylak olmadi.(narhi 1000 edi)
#if shirt and trouser and tie and suit:
#    total = shoes + 4000
#elif shirt and tie:
#    total = shoes + 2000
#print(f"Sizning umumiy haridingiz {total} ni tashkil etadi.")

# if-elif-else zanjirining kamchiligidan biri, shartlardan biri bajarilishi bilan,
# qolgan shartlar tekshirilmaydi. Shung uchun ba'zida shartlarni ketma ket 
# tekshirish uchun, har bir shartni alohida if bilan ajratish talab qilinishi 
# mumkin.
#price = 25 # 25 dhs for potato 
#onion = 1 # 10 dhs
#garlic = 1 # 10 dhs
#black_papper = 0 #10 dhs
#cucumber = 0 # 10 dhs
#carrot = 1 #10 dhs
#if onion:
#    print("Customer bought onion")
#    price = price + 10
#if garlic:
#    print("Customer bought garlic")
#    price = price + 10
#if black_papper:
#    print("Customer bought black papper.")
 #   price = price + 10
#if cucumber:
 #   print("Customer bought cucumber.")
 #  price = price + 10
#if carrot:
#    print("Customer bought carrot.")
#    price = price + 10
#print(f"Total price is {price}. Thank you for shopping with us!")

# in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin.

#menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
#"manti" in menu # menu da manti bormi?
# natija : False
#"shashlik" in menu # menu da shashlik bormi
# natija: True
#ovqat = input("Nima ovqat yeysiz? \n> ")
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi.")
#else:
#    print("Kechirasiz, bizda bunday ovqat yo'q.")

# not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.

#menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
#"manti" not in menu # menu da manti yo'qmi?
## natija : True
#"shashlik" in menu # menu da shashlik yo'qmi?
## natija: False
#ovqat = input("Nima ovqat yeysiz? \n> ")
#if ovqat.lower() not in menu:
#    print("Kechirasiz, bizda bunday ovqat yo'q.")
#else:
#    print("Buyurtma qabul qilindi.")

# Ikki ro'yxatning tarkibi quyidagicha tekshiriladi:

#menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
#buyurtmalar = ["osh", "mastava", "shashlik", "somsa", "manti"]
#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor.")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo'q.")

#ombor = ["kartoshka", "sabzi", "piyoz", "pomidor", "bodring"]
#ombor_yoq = ["kartoshka", "baqlajon", "qalampir", "piyoz", "sabzi"]
#for sabzavot in ombor_yoq:
#    if sabzavot in ombor:
#        print(f"Omborda {sabzavot} bor.")
#    else:
#        print(f"Omborda {sabzavot} yo'q.")

# RO'YXAT BO'SH EMASLIGINI TEKSHIRISH:
    
#menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
#buyurtmalar = ["osh","somsa","manti", "shashlik"]
#if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor.")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
#else:# agar ro'yxat bo'sh bo'lsa
#    print("Kechirasiz, savatchangiz bo'sh")

# agar ro'yxat bo'sh bo'lsa:
#menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
#buyurtmalar = []# ro'yxat bo'sh.
#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor.")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
#else:
 #   print("Kechirasiz, savatchangiz bo'sh")
# Demak if royxat_nomi: ifodasi agar ro'yxatda bir dona element bo'lsa ham TRUE 
# qiymat qaytaradi, aks holda FALSE qiymatini qaytaradi.

cars = ["Chevrolet", "Mercedes", "BMW", "Audi", "Wolkswagen", "Lamborghini", "Ferrari"]
order = ["BMW", "Chevrolet", "Audi", "Lamborghini"]
if order:
    for car in order:
        if car in cars:
            print(f"{car} is available to buy.")
        else:
            print(f"Sorry, {car} is not available temporarily.")
else:
    print("Basket is empty.")

















































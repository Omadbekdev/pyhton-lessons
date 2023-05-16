#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:01:31 2023

@author: pc
"""
# Quyidagi kodda 3 ta qo'shtirnoq yoki birtirnoq yordamida matnni istalgan joyidan
# keyingi qatorga surish ko'rsatilgan.
#print('''Odami ersang,
#Demagil odami,
#Oniki, yo\'q,
#Xalq g\'amidin g\'ami''')

# Yoki(backslash+n) \n yordamida ham matnni istalgan joyidan pastki qatorga yozish mumkin.
#print("Yurtim ado bo'lmas armonlaring bor,\nToshlarni yig'latgan dostonlaring bor.")

# Agar matn tarkibidagi so'zlarda tutuq belgisi qatnashgan bo'lsa (') va matn bir
# tirnoq bilan yopilgan bo'lsa, tutuq belgisidan oldin \ (backslash) qo'yamiz:
#print('Yurtimizda ulkan o\'zgarishlar ko\'p')

#Arifmetik amallar. Pythonda arifmetik amallar matematika qoidalariga asosida ishlaydi
#print(5+5*2/2)
# Agar / bo'lish ni bajarsak, natijasi o'nlik son ko'rinishida ekranga chiqadi. 
# Agar butun son ko'rinishida chiqarmoqchi bo'lsak // ni yozishimiz kerak.
#print(25//5)

#print() yordamida matn va ifodalarni jamlab chiqarish mumkin. Buning uchun matn va ifoda
# o'rtasiga vergul , belgisini qo'yamiz.
#print("Agar beshni o'nga ko'paytirsak", 5*10, "hosil bo'ladi.")
#print("Men",1000+996,"yilda tug'ilganman.")
#print("5+30/15*8 =",5+30//15*8,)

#print('"Nexia" "Tico" "Damas", ko\'rganlar qilar havas.')
# 5 ning 4-darajasi nechiga teng?
#print("5 ning 4-darajasi", 5**4, "ga teng.")
# 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
#print("22 ni 4 ga bo'lganda", 22/4, "qoldiq qoladi.")

# Variables - O'zgaruvchilar - komputer xotirasida malum turdagi ma'lumotlarni 
# saqlash uchun ajratilgan joy bo'lib, istalgan vaqtda uni o'zgartirish mumkin 
# bo'lgani uchun uni shunday nomlanadi.

#ism = "Omadbek"# O'zgaruvchi tarkibidagi matn "" yoki '' bilan yoziladi.
#familiya = "Abdurakhmonov"
#tugilgan_yil = 1996# raqamlar uchun '' yoki "" ishlatilmaydi.
#tugilgan_shahar = "Namangan"
#print(f"Men {ism} {familiya}. {tugilgan_yil}-yilda {tugilgan_shahar} shahrida tavallud topganman.")

#ism = "Diyorbek"
#familiya = 'Abdurakhmonov'
#tugilgan_yil = 1993
#tugilgan_shahar = 'Namangan'
#print("Bu",ism, familiya,". U", 1993, "yilda", tugilgan_shahar,"shahrida tavallud topgan.")

#String ya'ni matn Pythonda eng ko'p qo'llaniladigan malumot turlaridan biridir.
# Unicode jadavalidagi barcha belgilar, jumladan, o'zbek,arab,hind,xitoy alifbosidagi
# harflar va turli emoji/stickerlar string(matn) sifatida qo'llanishi mumkin.
#birinchi = "Kalimai shahodat 📿"
#ikkinchi = "Namoz o'qish 👳"
#uchinchi = "Ro'za tutish 🍲"
#tortinchi = "Zakot berish 💰"
#beshinchi = "Haj qilish 🕋 "
#print(f"Islom dini 5 ustundan iboratdir va ular quyidagilar: \n{birinchi} \
#      \n{ikkinchi} \n{uchinchi} \n{tortinchi} \n{beshinchi}")

# Matnlarni qo'shish uchun + operatoridan foydalanamiz.
#phone = "Iphone 6 S"
#old_phone = "Iphone XR"
#print("Men hozigi kunda" +' '+ phone +' '+ "telefonidan foydalanaman. Bundan avval menda " +
#      old_phone + " telefoni bor edi ammo u telefon buzilib qoldi.")# ikki matn
# yoki o'zgaruvchi bir-biriga yopishib qolmasligi uchun ' ' belgisidan foydalanamiz.

#work_days = "Dushanbadan Jumagacha"
#off_days = "Shanba va Yakshanba"
#print("Odatda Dubaida" + ' ' + work_days +' '+ "ish kunlaridir. " + off_days + \
#      ' ' + "esa dam olish kunlari hisoblanadi.")

# f-string yani f"{}" yordamida ikki va undan ortiq matn ko'rinishidagi 
# o'zgaruvchilarni qo'shishimiz mumkin.

#airline_1 = "Emirates Airways"
#airline_2 = "Fly Dubai"
#airline_3 = "Uzbekistan Airways"
#print(f"O'zbekiston va BAA o'rtasida" + ' ' + airline_1 + ', ' +airline_2 +', '\
#      + airline_3 + ' ' + "kabi kompaniyalarning havo parvozlari yo'lga qo'yilgan.")

# Matnga bo'shliq qoshish uchun \t belgisidan, yangi qatordan boshlash uchun esa
# \n belgisidan foydalanamiz:
    
#print("Hozirgi kunda rivojlanayotgan sohalardan biri\tbu IT sohasidir.")
#print("Eng ko'p foydalanadigan dasturlash tillariga namunalar: \nPython\t\nC++ \
#      \nSwift")

#Metodlar - string(matn)lar ustida amalga oshiriladigan tayyor amallar to'plamidir.
# bularga - .lower(), .upper(), .title(), .capitalize(), .lstrip(), .rstrip(), 
# .strip()
#ism = "omadbek"
#familiya = "abdurakhmonov"
#ism_sharif = f"{ism} {familiya}"
#print("Mening ismim " + ism_sharif.upper())#matndagi har bir harfni katta harfga o'zgartiradi. 
#print("Mening ismim "+ ism_sharif.lower())#har bir harfni kichik harfga o'zgartiradi.
#print("Mening ismim "+ ism_sharif.title())#matndagi har bir so'zning birinchi harfini katta harf bilan yozadi. 
#print("Mening ismim "+ ism_sharif.capitalize())#faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.

#Quyidagi metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
#car = "  Mercedes Benz  "
#print("Mening eng sevimli mashinam bu " + car.lstrip() + " hisoblanadi.") # boshidagi
#print("Dubaidagi eng ko'p tarqalgan mashina " + car.rstrip()+" hisoblanadi.")# oxiridagi
#print("Eng qimmat mashinalardan biri "+car.strip()+" hisoblanadi.")#har ikkala tomondan

#ism = input("Ismingiz nima? \n>")
#print("Assalomu alaykum, "+ism.title() + "\nYaxshimisiz?")
#savol = input("Sizga ayrim savollarni beramiz. Iltimos, savollarimizga javob bering. \
# Tug'ilgan yilingizni yozing. \n> ")
#print(savol + " yilda tavallud topgansiz.")

#savol_2 = "Tugilgan shahringiz manzilini kiriting. "
#print(savol_2.title() + " shahrida tug'ilgansiz.")

#savol_3 = "Qayerda tahsil olgansiz? \n> "
#print(savol_3.title() + "da tahsil olgansiz.")

#savol_4 = "Qaysi fanlarga qiziqasiz? \n> "
#print(savol_4 + " kabi fanlarga qiziqasiz.")

#savol_5 = "Hobbingiz nima? \n> "
#print(savol_5 + "Sizning hobbingiz ekan.")

#Lists - Ro'yxatlar
#fruits = ["apple","peach","lemon", "lime"]
#print(fruits[1].title())
#print(fruits[0].upper())
#print(fruits[2].lower())
#print(fruits[3].capitalize())

#digits = [333, 444, 555, 666, 777]
#print(digits[1] + digits[0])
#print(digits[-1] - digits[-3])#Listning oxirgi elementiga -1 deb murojaat 
#qilish mumkin. Bu usul Listning uzunligini aniq bilmaganimzda foyda beradi.

# Elementlarni o'zgartirish, o'chirish, qo'shish:
#sonlar = [2200, 3300, 4400, 5500, 6600]
#sonlar[0] = 2500
#sonlar[1] = 3500
#sonlar [2] = sonlar[2] + sonlar[0]
#sonlar[3] = sonlar[3] - sonlar[1]
#sonlar[4] = sonlar[4] + sonlar[0]
#print(sonlar)

#stuff = []
#stuff.append("pen")# .append() metodi yordamida istalgan ro'yxatga element qo'shish mumkin.
#stuff.append("notebook")
#stuff.append("bag")
#stuff.insert(3, "charger") # .insert() yordamida ham ro'yxatga element qo'shish mumkin
#stuff.insert(1, "laptop")
#print(stuff)
#.append va .insert ning farqi:
#.append() metodi orqali faqat ro'yxat oxiriga element qo'sha olamiz.
#.insert.() metodi orqali indexni ko'rsatish orqali ro'yxatning istalgan joyiga
# element qo'shishimiz mumkin.

# del operatori yordamida index ko'rsatish orqali ro'yxat tarkibidagi 
# elementlarni o'chirishimiz mumkin.

phones = ["iphone","samsung","siemens", "nokia","huawei"]
del phones[2]
del phones[2]
phones.remove("samsung")# .remove() metodi yordamida qiymatni ko'rsatish orqali ro'yxat ichidagi elementlarni
# o'chirishimiz mumkin.
phones.remove("huawei")
print(phones)
phones.append("one plus")
print(phones)
phones.insert(1, "xiaomi")
print(phones)

cloths = ["shoes","cap", "socks", "shirt", "t-shirt"]
done = cloths.pop(3)
print(cloths)
print("I bought " + done + "\ta lot today.")
print("But I did not buy these: " , cloths)
























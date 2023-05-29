#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:11:40 2023

@author: OmadbekDev
"""
## Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
  # Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida
   # chiroyli qilib konsolga chiqaring.
#print("Pythondagi kerakli atamalar:")
codes = {
    "string" : "matn",
    "float" : "o'nlik son",
    "integer" : "butun son",
    "boolean" : "mantiqiy qiymat",
    "dictionary" : "lug'at",
    "tuple" : "o'zgarmas ro'yxat",
    "list" : "ro'yxat",
    "for" : "takroriy operator",
    "del" : "elemetlarni o'chiruvchi operator",
    "if" : "agar"
    }
#for code in  sorted(codes): # 1-usul:
#    print(f"{code.title()} - {codes[code].capitalize()}")
#for key, value in sorted(codes.items()): # 2-usul:
#    print(f"{key.title()} - {value.title()}")

## Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
  # keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 

countries = {
    "uzbekistan" : "tashkent",
    "russia" : "moscow",
    "united arab emirates" : "abu dhabi",
    "united states america" : "washington",
    "germany" : "berlin",
    "italy" : 'rome',
    "great britain" : "london"
    }
#print("Dunyo davlatlari:")
#for key in sorted(countries.keys()):
#    print(key.upper())
      
#print("Davlatlarning poytaxtlari:")
#for value in sorted(countries.values()):
#  print(value.title())

## Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini
 # konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
 # "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
 
 
#country = input("Qaysi davlatning poytaxtini bilishni istaysiz? \n> ").lower()
#capital = countries.get(country)
#if capital == None:
#    print("not available")
#else:
#    print(f"{country}ning poytaxti {capital} shahri.")


## Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
# taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, 
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

meals = {
    "buratta" : 120,
    "veal tonnato" : 110,
    "octopus" : 100,
    "tenderloin" : 200,
    "beef cheek" : 220,
    "seabream crust" : 350,
    "baby chicken" : 250,
    "pacceri" : 150,
    "spaghetti" : 170,
    "lasagna" : 80
    }

print("Iltimos, yoqtirgan 3 ta taomingizni buyurtma bering va narxini biling.\n> ")
orders = []
for n in range(3):
    orders.append(input(f"{n+1}-yoqtirgan taomingizni kiriting.\n> ").lower())

for order in orders:
    if order in meals:
        print(f"{order.title()}ning narxi {meals[order]} dirham.")
    else:
        print(f"Kechirasiz,  bizda {order} yo'q")







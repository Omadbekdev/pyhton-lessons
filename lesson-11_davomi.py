#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:28:11 2023

@author: OmadbekDev
"""

talaba_0 = {
            "ism" : "laziz", 
            "familiya" : "nematjonov",
            "yosh" : 27, 
            "manzil" : "norin", }
#print(talaba_0.items())# .items() metodi yordamida lug;at tarkibidagi key va 
    # value pair ni konsolga chiqarishimiz mumkin.

## for sikli yordamida .items() metodidan foydalansak tushunarli ko'rinishga keladi.
#for key, value_pair in talaba_0.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value_pair}")

telefonlar = {
            "laziz" : "samsung", 
            "aziz" : "iphone x", 
            "qudrat" : "xiaomi", 
            "jamshid" : "oppo"
            }   
#for k, v in telefonlar.items():
#    print(f"{k.title()}ning telefoni {v}")
  
## Agar faqatgina keys(kalit so'zlar)ni konsolga chiqarmoqchi bo'lsak, .keys() metodidan
   #foydalanamiz.  
mahsulotlar = {
               "olma" : 10000, 
               "uzum" : 15000,
               "xurmo" : 20000,
               "anjir" : 25000
                }
#print(mahsulotlar.keys())

#print("Do'kondagi mahsulotlar:")
#for mahsulot in mahsulotlar.keys():
 #   print(mahsulot.title())

bozorlik = ["anjir", "o'rik", "mayiz", "olma"]
#for mahsulot in  mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()}ning narxi {mahsulotlar[mahsulot]} so'm.")

#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos do'koningizga {buyum}dan ham olib keling.")

## Agar lug'at elementlarini lug'at tartibida konsolga chiqarish talab qilinsa,
  # sorted() funksiyasidan foydalanamiz: 
cities = {
    "dubai" : "united arab emirates",
    "madina" : "saudi arabia",
    "quddus" : "palestine",
    "damascus" : "iraq",
    "tashkent" : "uzbekistan",
    "istanbul" : "turkey"
    }
#for city in sorted(cities):
#    print(city.title())
    
## Agar konsolga faqatgina value pair(qiymat) ni chiqarish talab qilinsa,
 ## .values() metodidan foydalanamiz.

clubs = {
    "barcelona" : "spotify",
    "real madrid" : "fly emirates",
    "arsenal" : "fly emirates",
    " manchester city" : "etihad",
    "benfica" : "fly emirates"
    }
#print(clubs.values())
#for club in clubs.values():
    #print(club.title())
    
## Agar lug'at tarkibida bir nechta bir xil value pair bo'lsa, qachonki ularni konsolga
  ## chiqarganimizda ham ular shundayligicha chiqadi. Agar takror chiqishini oldini
  ## olishni istasak, set() funksiyasidan foydalanamiz.
#for club in set(clubs.values()):
#    print(club.title())



















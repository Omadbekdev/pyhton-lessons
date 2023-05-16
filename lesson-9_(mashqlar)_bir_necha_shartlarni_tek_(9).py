#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:52:34 2023

@author: pc
"""
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
# "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

son = float(input("Juft son kiriting. \n> "))
if son%2:
    print("Bu juft son emas.")
else:
    print("Rahmat.")
 
#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini chiqaring:
#yosh = int(input("Iltimos, yoshingizni kiriting. \n> "))
#if yosh <= 4 or yosh >= 60:
#    print("Sizga muzeyga kirish bepul. Marhamat!")
#elif yosh <= 18:
#    print("Muzeyga kirish bileti narxi 10000 so'm")
#else:
#    print("Muzeyga kirish bileti narxi 20000 so'm")
    
# yoki:
#yosh = int(input("Yoshingiz nechida?"))

#if yosh<=4 or yosh>=60:
#    narh = 0;
#elif yosh < 18:
#    narh = 10000
#else:
#    narh = 20000
#print(f"Chipta {narh} so'm") 
    
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning
# teng yoki katta/kichikligi haqida xabarni chiqaring:
    
#son_1 = float(input("Istalgan sonni kiriting. \n> "))
#son_2 = float(input("Istalgan yana bir sonni kiriting. \n> "))
#if son_1 > son_2:
#    print(f"{son_1} > {son_2}")
#elif son_1 < son_2:
#    print(f"{son_1} < {son_2}")
#else:
#    print(f"{son_1} = {son_2}")
    
#  
#mahsulotlar = ["kartoshka", "piyoz", "sabzi", "anor", "anjir", "o'rik", "uzum",
 #              "shaftoli", "tarvuz", "qovun"]
#savat = []
#for meva in range(5):
#    savat.append(input(f"Savatga {meva+1}-mahsulotni kiriting. \n> "))
#for meva in savat:
#    if meva in mahsulotlar:
#        print(f"Do'konimizda {meva} bor")
#    else:
#       print(f"Do'konimizda {meva} yo'q")

#iphone = ["Iphone XS", "Iphone X", "Iphone 12", "Iphone 12 Pro", "Iphone 13 Pro Max,",
#          "Iphone 7", "Iphone 8", "Iphone 14 Pro Max"]
#order = []
#for model in range(6):
#    order.append(input(f"Harid qilmoqchi bo'lgan {model+1}-telefon modelini kiriting.\n> "))
#for model in order:
#    if model in iphone:
#        print(f"Bizda {model} modeli mavjud.")
#    else:
#        print(f"Bizda {model} modeli mavjud emas.")
 
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
#Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni
# foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda 
#bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda 
#"Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar = ["omadbek","alisher", "elmurod","laziz","qudrat","nuriddin"]
yangi_foydalanuvchi = []
yangi_foydalanuvchi.append(input("Iltimos yangi login kiriting. \n> "))
for new in yangi_foydalanuvchi:
    if new in foydalanuvchilar:
        print("Kechirasiz, login band. Yangi login tanlang.")
    else:
        print("Hush kelibsiz!")

# Boshqa bir usul:

users = ["omadbek", "javlon", "alisher", "bunyod"]
login = input("Iltimos, yangi login tanlang. \n> ")
if login in users:
    print("Login band. Iltimos boshqa login tanlang.")
else:
    print("Hush kelibsiz!")






#mahsulotlar = ["kartoshka", "piyoz", "sabzi", "anor", "anjir", "o'rik", "uzum",
#              "shaftoli", "tarvuz", "qovun"]
#buyurtma = []
#for meva in range(5):
#if buyurtma:
    
    
    
    
    
    
      

    
    
  
    
  
    
  
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
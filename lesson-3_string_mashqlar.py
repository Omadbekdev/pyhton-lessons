#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:02:57 2023

@author: pc
"""

# Amaliyot uchun mashqlar

#kocha = "Bog'bon"
#mahalla = "Sog'bon"
#tuman = "Bodomzor"
#viloyat = "Samarqand"
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \ 
     # tuman + " tumani, " + viloyat + " viloyati")

#kocha = "Bog'bon"
#mahalla = "Sog'bon"
#tuman = "Bodomzor"
#viloyat = "Samarqand"    
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
 #     tuman + " tumani, " + viloyat + " viloyati")

#kocha = input("Ko'changizning nomi nima?")
#print("Demak sizning ko'changiz " + kocha.title())
#mahalla = input("Mahallangizning nomi nima? \n>")
#print("Demak sizning mahallangiz " + mahalla.title())
#tuman = input("Qaysi tumandansiz? \n>")
#print("Demak, siz " + tuman.upper() + " tumanidansiz")
#viloyat = input("Qaysi viloyatdansiz? \n>")
#print("Demak, siz " + viloyat.lower() + " viloyatidansiz")

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + tuman + " tumani,\n" \
      + viloyat + " viloyati\n")
manzil = f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati"
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
print(manzil.title())

print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")  
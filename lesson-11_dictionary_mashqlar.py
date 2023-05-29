#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:24:24 2023

@author: OmadbekDev
"""

father = {"name" : "umidjon", "b_date" : 1971, "from" : "namangan region"}
#print(f"My father is {father['name'].title()}.\
#      He was born in {father['from'].title()} in {father['b_date']}")
mother = {"name" : "muhayyo", "b_date" : 1975, "from" : "namangan region"}
#print(f"My mother name is {mother['name'].title()}. \
#      She was born in {mother['b_date']} in {mother['from'].title()}")
brother = {"name" : "diyorbek", "b_date" : 1993, "from" : "namangan region"}
#print(f"My brother name is {brother['name'].title()}.\
#      He was born in {brother['b_date']} in {brother['from'].title()}")

friend = {"laziz" : "lavash", "qudrat" : "shashlik", "asilbek" : "palov",
          "bunyod" : "somsa", "javlon" : "mastava" }
#print(f"Lazizning eng sevimli taomi bu {friend['laziz']}dir. \
#      Asilbekning sevimli taomi esa {friend['asilbek']}dir.\
#      Bunyodning eng yoqtirgan taomi bu {friend['bunyod']}dir.")

pyhton = {"string" : "matn", 
          "integer" : "butun son",
          "floating number" : "o'nlik son", 
          "boolean" : "mantiqiy qiymat",
          "if" : "agar", 
          "else" : "aks holda", 
          "for" : "uchun",
          "del" : "o'chirish", 
          "append" : "qiymat qo'shish",
          "title" : "bosh harf bilan yozish"
          }
word = input("Pythonga oid atamalarning tarjimasini bilishni istaysizmi? \
            \nUnda istalgan atamani yozing. \n> ").lower()
#print(pyhton.get(word,"Bunday termin mavjud emas"))

tarjima = pyhton.get(word)
if tarjima == None:
    print("Bunday termin mavjud emas.")
else:
    print(f"{word.title()} so'zi {tarjima} deb tarjima qilinadi. ")






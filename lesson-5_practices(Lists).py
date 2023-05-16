#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 00:17:20 2023

@author: pc
"""

#age = int(input("How old are you?\n"))
#if age <= 4:
#    price = 0
#elif age <= 10:
#    price = 20
#else:
#    price = 35
#print(f"Ticket price is {price} aed.")

#items = ["laptop", "cap", "prayer matt", "cloths"]
#print(items[-1])
#print(items[-3])
#items[1] = "pilow"
#tems [-1] = "blanket"
#print(items)
#items.append(12)
#items.append("charger")
#items.insert(1, "pen")
#del items[-3]
#del items[-2]
#items.remove("pen")
#items.remove("pilow")
#items.append("bed")
#items.insert(-1, "notebook")
#items.insert(-1,"towel")
#del items[-1]
#items.remove("towel")
#items.append("money")
#items.insert(2, "money")
#items.remove("money")
#need = items.pop(-1)
#print(f"I have already these items: {items}. \nBut I do not have {need}")
#gift = items.pop(0)
#print(f"I can give you {gift} as a gift.")

#friends = ["Laziz", "Nuriddin", "Asilbek"]
#print("Salom", friends[0], "bugun choyxona bormi?")
#print("Salom", friends[1], "bugun ishing bormi?")
#print("Salom", friends[2], "nima qilyapsn hozir?")

#digits = [22, 33, 65]
#print(digits[0] + digits[-1] * digits[1])

#cities = ["Dubai", "Tashkent", "Namangan", "Andijon", "Sharjah", "Jiddah"]
#print(len(cities))
#cities.sort()
#print(cities)
#cities.sort(reverse=True)
#print(cities)
#print(sorted(cities))
#print(sorted(cities, reverse=True))
#print(cities.reverse())
#books = ["religious", 'drammatic', "tragedic", 'romantic', 'comedic']
#books.reverse()
#print(books)
#print(len(books))

#odd_numbers = list(range(10,30,2))
#even_numbers = list(range(10,30,2))
#print(f"These are odd numbers from 10 to 30 : \n{odd_numbers}")
#print(f"These are even numbers from 10 to 30 : \n{even_numbers}")

#some_num = [4242, 5451, 7716,1121]
#max_ = max(some_num)
#min_ = min(some_num)
#sum_ = sum(some_num)
#print(f"Highest digit in the list is : {max_}. \nLowest is: {min_}. \nTotal is: {sum_}.")

#starters = ["Burrata", "Octopus", "Beef Carpachio", "Fried Calamari"]
#chef_sp_str = starters[:]
#chef_sp_str.append("Vitello Tonnato")
#chef_sp_str.insert(1, "Betroot salad")
#chef_sp_str.remove("Octopus")
#del chef_sp_str[2]
#chef_sp_str[2]= "Stuffed Calamari"
#print(f"Here is old starters which on A la carte menu: {starters}" 
 #     f" \nHere is new Chef Special Starters menu :{chef_sp_str}")

#buildings = ("Burj Khalifa", "Address Sky View", "Address Hotel")
#buildings = list(buildings)
#buildings.append("Alghader")
#buildings.insert(4, "Toyota")
#del buildings[1]
#buildings.remove("Address Hotel")
#buildings[0] = "Burj Daman"
#buildings = tuple(buildings)
#print(buildings)

#villages = ("To'lqin", "Bo'ritepa", "Lellabod", "Toshqin")
#villages = list(villages)
#villages [2] = "Xo'jaobod"
#villages.insert(0, "Toshloq")
#villages.append("Do'mar")
#del villages[1]
#villages.remove("Toshqin")
#villages.reverse()
#print(villages)
#villages.sort()
#print(villages)
#numbers = list(range(11,20, 2))
#print(numbers)

#guests = ["Laziz", "Qudrat", "Asilbek", "Bunyod"]
#for guest in guests:
#    print(f"Salom {guest}, Sog'liging yaxshimi?")
#numbers = list(range(1,11))
#for digit in numbers:
#    print(f"{digit} ning kvadrati {digit**2} ga teng.")
 
#numbers = list(range(11))
#new_numbers = []    
#for number in numbers:
#    new_numbers.append(number * 2)
#print(new_numbers)

#people = []
#print("Eng yaqin 5 ta do'stingizni yozing")
#for friend in range(4):
#    people.append(input(f"{friend+1}-do'stingizni yozing.\n>"))
#print(people)

#cities = []
#print("Sevimli shaharlaringizni yozing.")
#for city in range(3):
#    cities.append(input(f"Siz yoqtirgan {city+1}-shaharni yozing. \n> "))
#print(f"Sizning tanlovingiz quyidagilar : \n{cities}")

#clubs = []
#print("Which clubs you wish to play on Europe Champions League?")
#for club in range(6):
#    clubs.append(input(f"Please enter your {club+1}-choice. \n> "))
#print(f"Your options are below : \n{clubs}")

#autos = ["audi", "mercedes", "bmw", "tesla"]
#for auto in autos:
#    if auto == "bmw":
#        print(auto.upper())
#    else:
#        print(auto.title())
  
#week_days = ["monday","tuesday", "wednesday","thursday", "friday", "saturday","sunday"]
#for day in week_days:
#    if day == "friday":
#       print(f"These {day} off days")
#    else:
#       print(f"These {day} working days")

#person = input("Qaysi qishloq fuqarosi bolasiz? \n > ")
#if person.lower() != "toshloq" or "toshloq mfy":
#    print(f"Uzr {person.capitalize()}lik fuqaro, bu tizim faqat Toshloq MFY aholisi uchun. ")
#else:
#    print("Hush kelibsiz!")

#age = int(input("Qaysi yilda tug'ilgansiz? \n> "))
#if 2023-age < 18:
#    print(f"Siz {2023-age} yoshda ekansiz. \nUzr, kirish mumkin emas!")
#else:
#    print("Hush kelibsiz!")
  
#book, pen = 12, 33
#print("book<pen") if book < pen  else print("book>pen")  

#login = input("Iltimos login kiriting. \n> ")
#if len(login)<=6:
#    print("Login 6 ta belgidan ko'p bo'lishi kerak.")#
#else:
#    print("Ma'qullandi!")

#cars = ["toyota", "mercedes", "hyundai", "gm"]
#for car in cars:
#    if car == "gm":
#        print(car.upper())
#    else:
#        print(car.title())


#cars = ["toyota", "mercedes", "hyundai", "gm"]
#for car in cars:
#    if car != "gm":
#        print(car.title())
#   else:
#        print(car.upper())


#login = input("Iltimos login kiriting. \n> ")
#if login.lower() == "admin":
#    print("Hush kelibsiz, Admin. Foydalanauvchilar ro'yxatini ko'rasizmi?")
#else:
#    print(f"Hush kelibsiz, {login.title()}!")


#son = float(input("Istalgan sonni yozing. \n> "))
#if son < 0:
#    print("Manfiy son")
#else:
#    print("Musbat son")

#age = int(input("How old are you? \n> "))
#if age <= 5:
#    price = 0
#elif age <= 12:
#    price = 10
#elif age <= 18:
#    price = 20
#elif age <= 55:
#    price = 40
#else:
#    price = 30
#print(f"Entrence ticket price for you - {price} AED")

#phone = input("Men telefon sotib olmoqchiman. Sizda qanday tanlovlar mavjud? \n> ")
#price = float(input("Ushbu telefonning narxi qancha? \n> "))
#if phone.lower() == "iphone" and price <= 1500:
#    print("Men shu telefonni harid qilmoqchiman.")
#else:
#    print("Menga bu telefon ma'qul emas ekan. Rahmat!")
    
#date = (input("Sizlarda bu hafta qaysi kunlarga parvoz mavjud? \n> "))
#company = input("Qaysi kompaniya parvozlari mavjud? \n> ")
#price = float(input("Ushbu parvozning bilet narxi qancha? \n> "))
#if date.lower() == "chorshanba" or "payshanba" and company.lower() == "uzairways" \
#    and price <=1000:
#        print("Men shu biletni harid qilmoqchiman.")
#elif date.lower() == "chorshanba" or "payshanba" and company.lower() == "fly dubai"\
 #   and price <=900:
#        print("Bu menga maqul. Sotib olaman.")
#else:
 #   print("Menga bu tanlovlar maqul kelmadi. Uzr.")

#price = 2000
#keyboard = True #500
#mouse = False#500
#if keyboard and mouse:
##    price = price + 1000
#elif keyboard or mouse:
#    price = price + 500
#print(f"Total price is {price} aed")

#price = 2000
#bottle = True
#cable = True
#bag = False
#headphone = False
#if bottle:
#    print("You bought bottle.")
#    price = price + 500
#if cable:
#    print("You bought cable.")
#    price = price + 500
#if bag:
#    print("You bought bag.")
#    price = price + 500
#if headphone:
#    print("You bought headphone.")
#    price = price + 500
#print(f"Your total shopping is {price} aed. ")

#total = 1000
#blanket = False
#carpet = True
#bed = True
#if blanket:
#    print("You purchased blanket.")
#    total = total + 200
#if carpet:
#    print("You purchased carpet.")
#    total = total + 250
#if bed:
#    print("You purchased bed.")
#    total = total + 150
#print(f"Your total purchase is {total} aed.")

#meal = ["spagetti","buratta", "milanesa"]
#user = input("Which  food you want to eat? ")
#if user.lower() in meal:
#    print("Sure")
#elif user.lower() not in meal:
#    print("Not available")

#meals = ["osh", "manti", "mastava", "baliq"]
#zakaz = ["osh", "kfc", "pizza", "manti"]
#for buyurtma in zakaz:
#    if buyurtma in meals:
#        print(f"{buyurtma} mavjud.")
#    else:
#        print(f"{buyurtma} mavjud emas.")

#store = ["iphone", "samsung", "redmi", "huawei"]
#require = ["iphone", "realmi", "oppo", "samsung"]
#for mobile in require:
#    if mobile in store:
#        print(f"{mobile} is available with us.")
#   else:
#       print(f"{mobile} is not available with us. Sorry.")

#cities = ["Dubai", "Istanbul", "Paris", "Milan", "Maldives"]
#tourist = ["Dubai", "Antalia", "Istanbul", "Maldives", "Madrid"]
#if tourist:
 #   for city in tourist:
 #       if city in cities:
#            print(f"Ticket is available for {city}")
#        else:
#            print(f"Ticket is not available for {city} temporarily")
#else:
#    print("List is empty")

#son = float((input("Istalgan juft sonni kiriting. \n> ")))
#if son%2: #toq bo'lsa
#    print("Juft son emas")
#else:
#    print("Rahmat")

#ticket = int(input("Iltimos yoshingizni yozing. \n> "))   
#if ticket <= 4 or ticket >= 60:
#    ticket = 0
#elif ticket < 18:
#    ticket = 10000
#elif ticket > 18:
#    ticket = 20000
#print(f"Muzeyga kirish {ticket} so'm. ")

#son1 = float(input("Birinchi sonni kiriting.\n> "))
#son2 = float(input("Ikkinchi sooni kiriting. \n>  "))
#if son1 > son2:
#    print(f"{son1} > {son2}")
#elif son1 < son2:
#    print(f"{son1} < {son2}")
#else:
#    print(f"{son1} = {son2}")







#users = ["omar", "omad", "bobur", "laziz", "qudrat"]
#login = input("Iltimos login tanlang.\n> ")
#if login in users:
#    print("Login band. Boshqa login tanglang.")
#else:
#    print("Hush kelibsiz.")











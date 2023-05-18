# 17.05.2023
# Mavzu: Lug'at-Dictionary
# Muallif: OmadbekDev


car_0 = {"model" : "mercedes", "rang":"qora", "yili": 2023}
#print(car_0["model"])
#print(car_0["yili"])

en_uz = {"apple":"olma", "apricot":"o'rik",
         "bag":"sumka", "blanket": "yopinchiq",
         "cloth" : "kiyim"}
#print(en_uz["apple"])
#print(en_uz["blanket"])
#print(en_uz["cloth "])

student_0 = {"ism":"bobur sharipov", "yosh": 21, "joy":"namangan viloyati"}
#print(f"{student_0['ism'].title()}, {student_0['yosh']} yoshda va u {student_0['joy'].capitalize()}da tug'ilgan")
student_0['kurs'] = 3
student_0['o_joy'] = "namdu"
#print(student_0)
#print(f"Talaba {student_0['ism'].title()} {student_0['yosh']}da.\
#      U {student_0['joy'].capitalize()}da yashaydi. {student_0['ism'].title()}\
 #         {student_0['o_joy'].upper()}da {student_0['kurs']}-kurs talabasidir.")
student_1 = {}# bo'sh lug'at yaratib, unga kalit so'z va qiymatlar qo'shamiz.
student_1['name'] = "abdulloh"    
student_1['address'] = "namangan city"
student_1["age"] = 27
student_1['profession'] = "python developer"
#print(f"Bu {student_1['name'].title()}. U {student_1['address'].title()}da yashaydi.\
 #     {student_1['name'].title()} {student_1['age']} yoshda va\
  #        u {student_1['profession'].title()}. ")
student_1['name'] = "Muhammad"#kalit so'zning qiymatini shunday o'zgartiramiz.
student_1['age'] = 28        
#print(f"Bu {student_1['name'].title()}. U {student_1['address'].title()}da yashaydi.\
#       {student_1['name'].title()} {student_1['age']} yoshda va\
#           u {student_1['profession'].title()}. ")         

# Kalit so'z va qiymatni o'chirish.
#del student_1['age']
#print(student_1)
         
#Lug'atlarni bir nechta qatorda yozish mumkin.
telefonlar = {
    "ali":"iphone x",
    "jasur" : "samsung s10",
    "bobur" : "xiaomi 10",
    "jobir" : "oppo 6"
    }
print(f"Guruhda hammaning telefoni bor. Masalan, Alining telefoni {telefonlar['ali'].title()}")
#print(telefonlar)
          
## .get() metodi 

#phone = telefonlar.get("alisher", "uning telefoni yo'q")
#print(phone)

        
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
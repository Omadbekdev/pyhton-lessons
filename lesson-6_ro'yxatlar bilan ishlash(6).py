#6- Dars: Ro'yxatlar bilan ishlash
# Muallif : Omadbek
# Sana: 31/03/2023

# ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash
# uchun .sort() metodidan foydalanamiz.
#cars = ["bmw", "mercedes", "audi", "volvo", "aston martin", "lamborghini", "tesla"]
#cars.sort()
#print(cars)

# Agar ro'yxatdagi biror element katta harf bilan boshlangan bo'lsa, u 
# ro'yxatning boshidan joy oladi.
#cars = ["bmw", "mercedes", "audi", "volvo", "aston martin", "Lamborghini", "Tesla"]
#cars.sort()
#print(cars)

# Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True 
# argumentini ham kiritamiz.
#cars.sort(reverse=True)
#print(cars)

#  Asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda 
# ro'yxatni tartiblashda sorted() funktsiyasidan foydalanamiz:
#mehmonlar = ["Jamshid", "Akbar", "Hoshimjon", "Laziz", "Zohid"]
#print(sorted(mehmonlar))
 
# Teskari tartiblash uchun sorted() funktsiyasiga reverse=True argumentini beramiz:
#print(sorted(mehmonlar, reverse=True))

# sorted() va .sort() yordamida sonlarni ham tartiblash mumkin:
#ages = [11, 76, 43, 88, 21, 7, 37]
#ages.sort()
#ages.sort(reverse=True)
#print(ages)
#print(ages)
#print(sorted(ages))
#print(sorted(ages, reverse=True))

# Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi
# mumkin. Buning uchun .reverse() metodidan foydalanamiz.
#fruits = ["apple", "peach", "lime", "watermelon", "lemon", "banana"]
#fruits.reverse()
#print(fruits)

# Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun 
 # len() funktsiyasidan foydalanamiz:
#fruits = ["apple", "peach", "lime", "watermelon", "lemon", "banana"]   
#print( "Ro'yxatdagi mevalarning soning uzunligi :", len(fruits), " ga teng")

# range() yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. 
 # list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
#sonlar = list(range(0,13))
#print(sonlar)
#sonlar_2 = list(range(88,99))
#print(sonlar_2) #Diqqat! E'tibor qiling range() funktsiyasi ikkinchi indeksdan 
# bitta avval to'xtaydi

# range() yordamida qadamni ham berishimiz mumkin:
#juft_sonlar = list(range(20,41,2))
#print("Juft sonlar : " , juft_sonlar)
#toq_sonlar = list(range(21, 52, 2))
#print("Toq sonlar : " , toq_sonlar)

# Agar sonlar ketma-ketligi 0 dan boshlansa, range() funktsiyasida yakuniy 
 # indeksni ko'rsatish kifoya. Misol uchun range(0,10) emas range(10) deb 
  # yozsak ham bo'laveradi.
#juft_sonlar_2 = list(range(15))
#print("15 gacha bo'lgan juft sonlar : " , juft_sonlar_2)

# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. 
# Misol uchun ro'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, 
# eng katta sonni topish uchun esa max() funktsiyasidan, sonlarning yig'indisini 
# topish uchun esa sum() funktsyasidan foydalansak bo'ladi:

#narxlar = [6500, 9000, 893, 1440, 552, 909]
#arzon = min(narxlar)
#qimmat = max(narxlar)
#jami = sum(narxlar)
#print("Bozordagi eng qimmat mevaning narxi - ", arzon, ", eng qimmati - ", 
 #     qimmat, "ularning umumiy narxlari - ", jami)

#yosh = [12, 8, 34, 56, 70]
#eng_yosh = min(yosh)
#katta_yosh = max(yosh)
#umumiy = sum(yosh)
#print("Tadbirda qatnashuvchilarning yoshi kamida ", eng_yosh, 
 #     " va maksimum yosh chegarasi ", katta_yosh, "bo'lishi kerak.", 
  #    "Tadbirda qatnashuvchilarning umumiy soni ", umumiy," ni tashkil etadi" )

# Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin,
 # buning uchun biz boshlang'ich va oxirgi indekslarni beramiz:
#uae = ["Abu Dhabi", "Dubai", "Sharjah", "Umm ul Quwain", "Ajman", "Ras al Khaimah"]
#developed = uae[0:3]
#print(developed)
#undeveloped = uae[3:5]
#print(undeveloped)
#uae_center = uae[2:5]
#print(uae_center)

#uae_main = uae[:3] #Agar boshlang'ich indeksni bermasangiz, Python avtomat
 # ravishda 0 indeksdan boshlab kesadi.
#print(uae_main)
#uae_12 = uae[3:] #Agar 2-indeksni kiritmasangiz, ro'yxat oxirigacha kesadi:
#print(uae_12)

# Agar biz sonlar2=sonlar deb ikki o'zgaruvchini = yordamida nusxa olishga 
# harakat qilsak, yozgan komandamiz yangi ro'yxat yaratish o'rniga,
#  ikkala o'zgaruvchini ham bitta ro'yxatga bog'lab (yo'naltirib) qo'yadi. 
#sonlar = [1,2,3,4,5]
#sonlar2 = sonlar
#sonlar2.append(6)
#sonlar2.append(7)
#del sonlar2[2]
#print(sonlar2)

# Nuxsa olish uchun yuqoridagi ka'bi ro'yxatni kesish usulidan foydalanamiz.
#Faqatgina, kvadrat qavs ichida ikkala indeksni ham ko'rsatmasdan, bo'sh qoldiramiz:
#sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
#sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
#sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
#sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
#print("Bu sonlar ro'yxati:", sonlar)
#print("Bu sonlar2 ro'yxati:", sonlar2)

#men = [12, 13, 14, 15]
#sen = men[:]
#sen.append(16)
#sen.append(17)    
#print(men)
#print(sen)

# Tuple ozgarmas ro'yxat bo'lib, ichidagi qiymatlarni bir marta, dastur boshida 
#beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda, Tuple 
#e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
#tomonlar = (20, 30, 40)
#print(tomonlar)
#tomonlar[1] = 35 #bu operatsiya xatolikka olib keldi. Shu kabi ro'yxatdan biror 
#elementni o'chirish yoki yangi element qo'shish ham mumkin emas.
#print(tomonlar)

#Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni 
#list() funktsiyasi yordamida List (oddiy ro'yxat) ko'rinishiga keltirib olish,
# o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi yordamida o'zgarmas 
#ro'yxatga o'tkazish mumkin:
city = ("Namangan","Tashkent","Andijan","Fergana", "Samarkand")#o'zgarmas ro'yxat
city = list(city) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
#Ro'yxatga o'zgartirishlar kiritamiz
city.append("Bukhara")
city.append("Khiva")
city.remove("Andijan")
city[3] = "Gulistan"
city = tuple(city) #Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(city)















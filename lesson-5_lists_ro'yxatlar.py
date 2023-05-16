# 5-Dars: Lists(Ro'yxatlar)
# Muallif: Omadbek
# Sana: 28.03.2023

# Listlar quyidagicha yaratiladi:
#mevalar = ['olma', 'anor', 'uzum', 'anjir'] #mevalar ro'yxati(matnlar)
#narxlar = [1200, 1500, 2000, -1000, 1.5] # narxlar ro'yxati (sonlar)
#sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxati 
#ismlar =[] #bo'sh ro'yxat

#print("Birinchi meva", mevalar[0])
#print("Ikkinchi meva", mevalar[1])
#print("Ikkinchi meva", mevalar[2])
#print("Ikkinchi meva", mevalar[3])

#Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string metodlarni
# qo'llashimiz mumkin:
#print("Birinchi meva", mevalar[0].upper())
#print("Ikkinchi meva", mevalar[1].lower())
#print("Ikkinchi meva", mevalar[2].capitalize())
#print("Ikkinchi meva", mevalar[3].title())

#List elementlari ustida arifmetik amallarni bajaramiz:
#narxlar = [1200, 1500, 3000, 4500]
#print(narxlar[0] + narxlar[2])
#print(narxlar[3] - narxlar[1])
#print(narxlar[2] / narxlar[1])
#print(narxlar[0] * narxlar[3])

# Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish 
 # mumkin. Bu usul Listning uzunligini bilmaganda juda asqotadi.
#cars_models = ["BMW", "Mercedes", "Audi", "Chevrolet", "Toyota"]
#print(cars_models[-2])
#print(cars_models[-4])

# Ro'yxatdagi biror elementning qiymatini o'zgartirish uchun, o'sha elementga 
 # indeksi bo'yicha murojat qilamiz va yangi qiymat yuklaymiz:
#narxlar = [2200, 3000, 4000, 6000]
#narxlar[1] = 2900
#narxlar[0] = 2100
#narxlar[2] = 4200
#narxlar[3] = 5500
#print(narxlar)

# Ro'yxatga yangi element qo'shishning oson usuli bu .append() metodi yordamida
  # ro'yxatning oxiriga qiymat qo'shish:

#mevalar = ["olma", "o'rik", "anjir"]
#mevalar.append("tarvuz")
#mevalar.append("qovun")
#print(mevalar)

# .append() metodi bo'sh ro'yxatni to'ldrisihda juda qulay usul. Odatda dastur 
  # boshida bo'sh ro'yxat yaratilib, dastur davomida ro'yxat foydalanuvchi 
  # tomonidan to'ldirib borilishi odatiy hol.

#jamoalar = []
#jamoalar.append("Barcelona")
#jamoalar.append("Juventus")
#jamoalar.append("Liverpool")
#jamoalar.append("Ajax")

#print(jamoalar)

# Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan
 # foydalanamiz. .insert() metodi ichida yangi elementning indeksi va qiymati 
  # beriladi:

#davlatlar = ["England", "Marocco", "Argentina"]
#davlatlar.insert(0, "Germany")
#davlatlar.insert(2, "Italy")
#print(davlatlar)

# Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini 
  # bilishimiz lozim.
  # Indeks yordamida olib tashlash uchun del operatoridan foydalanamiz:
#davlatlar = ["England", "Marocco", "Argentina", "Germany"]
#del davlatlar[1]
#del davlatlar[2]
#print(davlatlar)

# Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan 
 # foydalanamiz. Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan 
  # qiymatni yozamiz

#regions = ["Namangan", "Andijon", "Farg'ona", "Toshkent"]
#regions.remove("Andijon")
#regions.remove("Farg'ona")
#print(regions)

#books = ["Dunyoning ishlari", "Tohir va Zuhra", "O'tgan kunlar", "Hamza"]
#print(books)
#del books[3]
#print(books)
#books.append("She'rlar")
#print(books)

# Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan 
 # sug'urib olish va undan foydalanish talab qilinishi mumkin. Buning uchun 
  # Pythonda .pop(indeks) metodidan foydalanmiz.

#bozorlik = ["yog'", "un", "piyoz", "kartoshka", "sabzi"]
#mahsulot = bozorlik.pop(2)
#print("Men " + mahsulot + " sotib oldim")
#print("Endi " , bozorlik , "sotib olishim kerak")


















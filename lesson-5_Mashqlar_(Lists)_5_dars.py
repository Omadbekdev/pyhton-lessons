# Mashqlar(Lists_ Ro'yxatlar)
# Muallif: Omadbek
# Sana: 28.03.2023

#ismlar = ["Nuriddin", "Salimjon", "Yusufxon"]
#print(ismlar[1], ", bugun choyxonaga boramizmi?")
#print(ismlar[2], ", ishlarningiz yaxshimi?")
#print("Sizlar ya'ni " f"{ismlar[1]} va {ismlar[2]} to'yga kelasizlarmi?")

# Sonlar bilan amallar
#sonlar = [35000, 12000, 10000, 50000]
#print(sonlar[0] + sonlar[2])
#print(sonlar[1] / sonlar[2])
#print(sonlar[3] * sonlar[2])

# Sonlarning qiymatini o'zgartirish
#sonlar[1] = 1111
#print(sonlar)
#sonlar[3] = 5500
#sonlar[2] = 1100
#print(sonlar)

# .pop() bilan ishlash
#t_shaxslar = ["Abu Bakr", "Umar ibn Xattob", "Usmon ibn Affon", "Imom Buxoriy", "Imom Termiziy"]
#z_shaxslar = ["Shayx Usmon", "Zakir Naik", "No'mon Alixon", "Yusuf Estes"]
#t_f_shaxs = t_shaxslar.pop(0)
#z_f_shaxs = z_shaxslar.pop(0)
#davatchi = z_shaxslar.pop(0)
#hadis = t_shaxslar.pop(3)
#print("Men tarixiy shaxslardan ", t_f_shaxs , "va zamonaviy shaxlardan " , z_f_shaxs, " bilan yuzma yuz ko'rishishni istardim")
#print(hadis, "hadis ilmining sultoni desak mubolag'a bo'lmaydi .", davatchi, "zamonamizning eng kuchli da'vatchi olimlaridan biridir")

# .append(), .remove(), .insert() bilan ishlash
friends = []
friends.append("Nuriddin")
friends.append("Bobur")
friends.append("Javohir")
friends.append("Javlon")
print(friends)
friends.remove("Javlon")
friends.remove("Javohir")
print(friends)
friends.insert(0,"Sardor")
friends.insert(2,"Qudrat")
friends.insert(3, "Laziz")
print(friends)

mehmonlar = []
#n_f = friends.pop(1)
#n_c = friends.pop(0)
#n_d = friends.pop(-1)
#mehmonlar.append(n_f)
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(0))
print(mehmonlar)









# 3-dars: String(Matn)
# Sana: 22/03/2023
# Muallif: Omadbek
smayl = "😅"
print(smayl)

shahar = "Namangan"
matn = "ga bordim"
sticker = "✅"
print(shahar + matn + sticker)

matn = "Men uchun eng yaxshi kompyuter brand bu"
laptop = "Macbook Pro"
sticker = "💻."#shu kabi sticker yoki emojilar https://symbl.cc/en/ saytidan copy qilinadi.
keyingi_matn = "Chunki u juda ham qulay va tezkor"
print(matn + ' ' + laptop + sticker + ' ' + keyingi_matn)

ism = "Omadbek"
familiya = "Abdurahmonov"
sharif = "Umid o'g'li"
kesim = " men bo'laman"
print(ism + ' ' + familiya + ' ' + sharif + ' ' + kesim)#ikki o'zgaruvchi orasiga bo'sh joy qo'shish uchun ' ' dan foydalanamiz.
# f-string usuli:
ism = "Omadbek"
familiya = "Abdurahmonov"
ism_familiya = f"{ism} {familiya}"
print(ism_familiya)
print(f"Assalomu alaykum. Men {ism_familiya}man. {ism} {familiya}!")

# Matnga bo'shliq qo'shish uchun \t va yangi qatordan boshlash uchun \n belgisidan foydalanamiz
print("Salom Dunyo!")
print("Salom \tDunyo!")
print("Salom \nDunyo!")

# Metodlar. 
ism = "Omadbek"
familiya = "Abdurahmonov"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())# .upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. 

print(ism_sharif.lower()) # .lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.

davlat = "Birlashgan Arab Amirliklari"
poytaxt = "Abu Dhabi shahri"
info = f"{davlat} {poytaxt}"
print(info.title()) # .title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.

print(info.capitalize()) # .capitalize() metodi faqatgina eng birinchi so'zning bosh harfini katta bilan yozadi.

# Metodlarni faqat o'zgaruvchilarga emas, balki to'g'ridan-to'g'ri matnga ham qo'llash mumkin (aslida o'zgaruvchi ham matnning (yoki boshqa ma'lumotning) manzili xolos)
print('Abu Dhabi shahri'.upper())
print('Ramazon oyi muborak bo\'lsin'.lower())
print('Bugun Ramazonning birinchi kuni'.title())
print('ro\'za islom dinining arkonlaridan biridir'.capitalize())

# strip(), rstrip() va lstrip() metodlari
dastur = "   IOS dasturlash tili   "
print("Men uchun eng yaxshisi " + dastur + "dir")
print("Men uchun eng yaxshisi "+ dastur.rstrip() + "dir") # .rstrip() metodi  matn oxiridagi bo'shliqni olib tashlaydi.
print("Men uchun eng yaxshisi " + dastur.lstrip() + 'dir') # .lstrip() metodi  matn boshidagi bo'shliqni olib tashlaydi.
print("Men uchunn eng yaxshisi " + dastur.strip() + 'dir') # .strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi

# input - foydalanuvchi bilan muloqot.
ism = input("Ismingiz nima?")
print("Assalomu alaykum, " + ism.title()) # input() funksiyasi o'zgaruvchilarning qiymatini foydalanuvchi tomonidan kiritish imkonini beradi. Ya'ni avval 1-qatorda foydalanuvchining ismini so'raydi. Foydalanuvchi ismini kiritib, Enter tugmasini bosgach, foydalanuvchi kiritgan matnism degan o'zgaruvchiga yuklanadi va dasturining 2-qatori bajaradi:
raqam = input("Iltimos, o'rindiq nomini kiriting.\n>>> ")
print("Marhamat, sizning joyingiz " + raqam)


















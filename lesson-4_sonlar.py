# 4-Dars: Sonlar
# Muallif: Omadbek
#Sana: 27/03/2023

a = 20
b = -10
c = a + b
print(c)

u = 46
p = 74
r = 71
a = (u+p)-r
print(a)

a = 80
b = 8
d = a/b
print(d)

n = 10
m = 1.5
l = n + m
j = n - m
k = n * m
h = n / m
print(l, j, k, h)

#Uzun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq (_) 
# yordamida guruhlash mumkin. Python - son tarkibidagi pastki chiziqlarni (_) 
#inobatga olmasdan, uzun sonligicha qabul qiladi.
p_miqdori = 1_200_333_456
od_soni = 132
print("Bizning universitetda ", od_soni,  "nafar o'quvchi" ,p_miqdori, "so'm mukofot qabul qildi")

#Birdaniga bir nechta o'zgaruvchiga qiymat berish uchun o'zgaruvchilar va ularga mos qiymatlar vergul (,) bilan ajratiladi:
c, b, d, f = 10, 20, 30, 40
print(c, b, d, f)

ism = "Jobir"
yosh = 22
xabar = ism + ' ' + str(yosh) + " yoshda" 
print(xabar)

# o'zgaruvchilarni adashtirib, xatolar qilmaslik uchun ba'zida o'zgaruvchinig turini tekshrish talab qilinadi. Buning uchun type() funktsiyasidan foydalanamiz:
ism = "Jobir"
yosh = 22
print(type(ism))
print(type(yosh))


t_yil = int(input("Tug'ilgan yilingizni kiriting \n>>>"))
yosh = 2023 - t_yil
print("Siz " + str(yosh) + " yoshdasiz")

t_raqam = int(input("Biletdagi tartib raqamingizni kiriting \n> "))
joy = 20 + t_raqam
print("Sizning joyingiz " + str(joy) + " o'rindiqda. Marhamat!")

t_yil = int(input("Tug'ilgan yilingizni kiriting \n>"))
yil = 2023 - t_yil
print("Siz " + str(yil) + " yilda tug'ilgansiz")

birinchi = int(input("Birinchi sonni kiriting "))
ikkinchi = int(input("Ikkinchi sonni kiriting "))
jami = birinchi + ikkinchi
print(jami)

#Mashqlar






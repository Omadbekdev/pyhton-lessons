# mashqlar
davlatlar = ["England","UAE","USA","Germany","Italy"]
#print(davlatlar)
#print(len(davlatlar))# ro'yxatning uzunligini aniqlash
#print(sorted(davlatlar)) # sorted()  funksiyasi yordamida ro'yxatni tartiblash
#print(sorted(davlatlar,reverse=True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)
sonlar = list(range(12,1200,2))
#print(sonlar)
#sonlar_jami = sum(sonlar)
#print(sonlar_jami)
#katta_son = max(sonlar)
#kichik_sonlar = min(sonlar)
#print(katta_son - kichik_sonlar)
#print(len(sonlar))
sonlar_20 = sonlar[:20]
sonlar_orta = sonlar[530:550]
sonlar_oxiri = sonlar[-20:]
print("Avvalgi sonlar :", sonlar_20, " \nO'rtadagi sonlar :", sonlar_orta, 
      " \nOxiridagi sonlar :", sonlar_oxiri)

taomlar = ["Pizza", "Pasta", "Buratta", "Calamari", "Bruschetta"]
nonushta = taomlar[:]
nonushta.remove("Pizza")
nonushta.remove("Pasta")
nonushta.append("Pastichotta")
nonushta.append("Betroot salad")
print(taomlar, nonushta)
nonushta = tuple(nonushta)






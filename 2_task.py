#2'. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

xp = [True,False]
yp = [True,False]
zp = [True,False]
for i in range(2):
    xp[i]
for x in xp:
    for y in yp:
        for z in zp:
            print(x,y,z)
            res1 = not (x or y or z)
            res2 = (not x) and (not y) and (not z)
            print (res1 == res2) 
sayac = 0
for i in range(10000, 100000):
           
    i=str(i)
    
    if i[0] == i[3] and i[1] == i[4] :
        sayac = sayac + 1


print("İlk iki basamağı ile son iki basamağı birbirine eşit olan 5 basamaklı şu kadar sayı vardır:" , sayac)

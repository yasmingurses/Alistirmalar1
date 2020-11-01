x = input("Bir sayı giriniz:")

if len(x) == 3 :
    if x[0] == x[2]:
        print("Bu sayı palindromiktir" , x)
    else :
        print("Bu sayı palindromik değildir" , x)

if len(x) == 4 :
    if x[0] == x[3] and x[1] == x[2] :
        print ("Bu sayı palindromiktir" , x)
    else :
        print("Bu sayı palindromik değildir" , x)


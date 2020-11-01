for i in range(1,999):
           
    i=str(i)
    
    if 1 <= int(i) <= 9 :
        print( i , end=" ")

    elif 10 <= int(i) <= 99 :
        if int(i[0]) + int(i[1]) < 9 :
            print( i , end=" ")

    elif 100 <= int(i) <= 999 :
        if int(i[0]) + int(i[1]) + int(i[2]) < 9 :
            print( i , end=" ")

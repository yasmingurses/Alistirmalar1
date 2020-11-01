for year in range(1000,2005) :
    year = str(year)

    if  int(year[0]) + int(year[1]) + int(year[2]) + int(year[3]) == 2005 - int(year) :
        print("Bu kişi şu yılda doğmuştur:" , year)


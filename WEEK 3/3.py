if __name__ == "__main__":
    n,m = map(int,input().split())
    chefs = []
    country = {}
    for _ in range(n):
        chef,c = map(str,input().split())
        chefs.append([chef,c,0])
        if(c not in country):
            country[c] = 0
    for _ in range(m):
        s = input()
        for i in range(n):
            if(chefs[i][0] == s):
                chefs[i][2]+=1
                country[chefs[i][1]]+=1
                break
    maxval = 0
    countryname = ""
    for i in country.keys():
        if(country[i] > maxval):
            maxval = country[i]
            countryname = i
        elif(country[i] == maxval):
            if(i < countryname):
                maxval = country[i]
                countryname = i
    maxval = 0
    chefname = ""
    for i in range(n):
        if(chefs[i][2] > maxval):
            maxval = chefs[i][2]
            chefname = chefs[i][0]
        elif(chefs[i][2] == maxval):
            if(chefs[i][0] < chefname):
                maxval = chefs[i][2]
                chefname = chefs[i][0]
    print(countryname)
    print(chefname)

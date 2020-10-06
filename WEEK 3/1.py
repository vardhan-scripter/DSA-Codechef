if __name__ == "__main__":
    m,n = map(int,input().split())
    l = list(map(int,input().split()))
    s = list(map(int,input().split()))
    costs = []
    indices = []
    r = 0
    for i in range(m):
        for j in range(n):
            if(l[i]+s[j] not in costs):
                costs.append(l[i]+s[j])
                indices.append([i,j])
                r+=1
            if(r >= n+m-1):
                break
        if(r >= n+m-1):
            break
    for i in range(0,n+m-1):
        print(indices[i][0],indices[i][1])

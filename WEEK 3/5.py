if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        l = list(map(int,input().split()))
        c = 0
        for i in range(n):
            for j in range(i+1,n+1):
                r = l[i:j]
                p = r[k%(j-i)]*(k//(j-i))
                if(p in r):
                    c+=1
                    print(r)
        print(c)

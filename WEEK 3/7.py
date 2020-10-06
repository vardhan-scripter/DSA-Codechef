if __name__ == "__main__":
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    c = 0
    l.sort()
    for i in range(n):
        for j in range(i+1,n):
            if(abs(l[i]-l[j]) >= k):
                c+=1
            else:
                break
    print(c)

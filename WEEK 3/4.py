if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,z = map(int,input().split())
        l = list(map(int,input().split()))
        c = 0
        while(len(l) > 0):
            c+=1
            m = max(l)
            l.remove(m)
            if(m > 1):
                l.append(m//2)
            z-=m
            if(z <= 0):
                break
        if(z > 0):
            print("Evacuate")
        else:
            print(c)

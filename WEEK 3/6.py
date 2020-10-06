if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(int(input()))
    l.sort()
    m = 0
    for i in range(n):
        if((n-i)*l[i] > m):
            m = (n-i)*l[i]
    print(m)

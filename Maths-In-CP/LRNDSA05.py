import math
for _ in range(int(input())):
    m,n=map(int,input().split())
    x=math.gcd(m,n)
    print(x)
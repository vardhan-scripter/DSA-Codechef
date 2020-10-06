# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.

# Input:
# First line of input contains a single integer T, the number of test cases.
# Each test is a single line containing a string S composed of only lowercase English alphabet.
# Output:
# For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.
# Constraints:
# 1 ≤ T ≤ 100
# 2 ≤ |S| ≤ 1000, where |S| denotes the length of S
# Example:
# Input:
# 6
# gaga
# abcde
# rotor
# xyzxy
# abbaab
# ababc


# Output:
# YES
# NO
# YES
# YES
# NO
# NO

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        r = input()
        k = len(r)
        k1 = k//2
        if(k%2 == 0):
            k2 = k1
        else:
            k2 = k1+1
        l1 = [r[x] for x in range(0,k1)]
        l2 = [r[x] for x in range(k2,k)]
        l1.sort()
        l2.sort()
        if(l1 == l2):
            print("YES")
        else:
            print("NO")
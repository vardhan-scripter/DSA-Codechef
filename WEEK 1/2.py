# If an Integer N, write a program to reverse the given number.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# Display the reverse of the given number N.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000000
# Example
# Input
# 4
# 12345
# 31203
# 2123
# 2300
# Output
# 54321
# 30213
# 3212
# 32

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        r = input()
        print(int(r[::-1]))

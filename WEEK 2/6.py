# You are given an infix expression S of length N. You need to convert the given expression S to its postfix equivalent using stack.
# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains a single integer N denoting the length of S.
# The second line contains a string S, the infix expression.
# Output
# For each test case print a single line containing the postfix equivalent for the given infix expression.

# Constraints
# 1≤T≤10
# 1≤N≤102
# S contains only uppercase English letters (A...Z), and these characters - (,),+,−,∗,/,^. S is a valid infix expression.
# Example Input
# 2
# 15
# ((A+B)*D)^(E-F)
# 19
# A+(B*C-(D/E^F)*G)*H
# Example Output
# AB+D*EF-^
# ABC*DEF^/G*-H*+
# Explanation
# Example case 1: The postfix equivalent for ((A+B)∗D)^(E−F) is AB+D∗EF−^.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        l = []
        op = []
        operators = "+-*/^"
        precedence = {"+":1,"-":1,"*":2,"/":2,"^":3}
        for i in s:
            if(i.isalpha()):
                l.append(i)
            elif(i in operators):
                while(len(op) >0 and op[-1] != "("):
                    if(precedence[op[-1]] >= precedence[i]):
                        l.append(op[-1])
                        op.pop(-1)
                    else:
                        break
                op.append(i)
            elif(i == "("):
                op.append(i)
            elif(i == ")"):
                while(len(op) >0):
                    if(op[-1] != "("):
                        l.append(op[-1])
                        op.pop(-1)
                    else:
                        op.pop(-1)
                        break
        while(len(op) > 0):
            if(op[-1] != "("):
                l.append(op[-1])
            op.pop(-1)
        print(''.join(l))
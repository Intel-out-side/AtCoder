import math
A, B = input().split()

#多少強引でも整数演算に持っていったほうがいい

A = int(A)
B = int(B.replace(".", ""))

print(A*B//100)

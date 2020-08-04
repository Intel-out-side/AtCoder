import sys
A = input()

for i in range(len(A)):

    if "a" < A[i]:
        A = A[0:i] + chr(ord(A[i])-1) + A[i+1:]
        print(A)
        sys.exit()

if len(A) > 1:
    print(A[0:len(A)-1])
    sys.exit()

print(-1)

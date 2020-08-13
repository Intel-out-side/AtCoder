N = int(input())

if N == 1:
    print(0)
    exit()

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

candidates = factorization(N)
# print(candidates)
li = []

for item in candidates:

    for i in range(item[1]):
        li.append(item[0]**(i+1))

li.sort()
# print(li)

cnt = 0
for i in range(len(li)):
    if N % li[i] == 0:
        N /= li[i]
        cnt += 1

print(cnt)

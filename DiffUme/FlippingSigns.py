N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    ans = sum(map(abs, A))
    print(ans)
    exit()
else:
    negs = 0
    for a in A:
        if a < 0:
            negs += 1

    if negs % 2 == 1:
        A = list(map(abs, A))
        A.sort()
        # print(A, sum(A))
        ans = sum(A) - 2 *A[0]
        print(ans)
    else:
        ans = sum(map(abs, A))
        print(ans)

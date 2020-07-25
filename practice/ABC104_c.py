D, G = list(map(int, input().split()))

P = [0]*D
C = [0]*D

ans_num = 10*100 + 1

for i in range(D):
    p, c = list(map(int, input().split()))
    P[i] = p
    C[i] = c


for i in range(2**D):
    score_li = list(range(1, D+1))
    ans_li = []
    ans_n = 0
    for j in range(D):
        if ((i >> j) & 1):
            ans_li.append(P[j] * score_li[j]*100 + C[j])
            score_li[j] = -1
            ans_n += P[j]

    if (sum(ans_li) < G):
        s = sum(ans_li)
        score_li.sort(reverse=True)

        for k in score_li:
            for l in range(P[k-1]):
                s += k * 100
                ans_n += 1
                if s >= G:
                    ans_num = min(ans_num, ans_n)
    else:
        ans_num = min(ans_num, ans_n)

print(ans_num)

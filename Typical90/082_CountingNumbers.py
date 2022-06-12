L, R = map(int, input().split())

MOD = 7 + 10**9

L_digit = len(str(L))
R_digit = len(str(R))

# 最初の処理
# L ~ 99..9(Lの桁数)の合計 * Lの桁数
start = L
end = int("9"*L_digit) if R > int("9"*L_digit) else R
n = end - start + 1 
s = n * (2*start + (n-1)*1)//2
ans = L_digit * s % MOD

if L_digit == R_digit:
    print(ans)
    exit()

for digit in range(L_digit+1, R_digit):
    
    start = int("1" + "0"*(digit - 1))
    end   = int("9"*digit)
    
    n = (end - start + 1)
    s = (n*(2*start + (n-1)*1))//2
    ans += digit * s % MOD

# 最後の処理
start = int("1" + "0"*(R_digit-1))
end = R
n = end - start + 1
s = n*(2*start + (n-1)*1)//2

ans += R_digit * s % MOD
ans %= MOD

print(ans)
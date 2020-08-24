S = input()

if (S[0] =='R' and S[1] == 'R') and (S[1] == 'R' and S[2] == 'R'):
    print(3)
elif (S[0] == 'R' and S[1] == 'R') or (S[1] == 'R' and S[2] == 'R'):
    print(2)
else:
    if 'R' in list(S):
        print(1)
    else:
        print(0)

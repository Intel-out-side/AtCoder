from collections import Counter
import itertools
S = input()
N = len(S)

if N <= 9:
    for st in list(itertools.permutations(S)):
        num = int("".join(st))

        if num % 8 == 0:
            print("Yes")
            exit()
    print("No")
    exit()


eights = [i*8 for i in range(13, 125)]

digits = list(Counter(S).items())
digits.sort(key = lambda x:int(x[0]))

for e in eights:

    digits_in_e = list(Counter(str(e)).items())
    digits_in_e.sort(key = lambda x:int(x[0]))
    isOkay = True
    counter = 0
    for ds, ks in digits:
        for de, ke in digits_in_e:
            if ds == de and ks >= ke:
                counter += 1
                isOkay = False


    if counter == len(digits_in_e):
        print("Yes")
        exit()

print("No")

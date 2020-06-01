def strings(cs, n, s):
    if n == 0:
        return [s]
    else:
        return [s] + [x for c in cs for x in strings(cs, n-1, s+c)]

def isSameType(a, b):
    if len(a) != len(b):
        return false

    res = False
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j] and b[i] != b[j]:
                res = False
            if a[i] != a[j] and b[i] == b[j]:
                res = False
            if (a[i] == a[j] and b[i] == b[j]) and (a[i] != a[j] and b[i] != b[j]):
                res = False

    return res

if __name__ == "__main__":
    N = int(input())
    alphabets = [chr(i) for i in range(65, 65+26)]
    all_str = strings(alphabets, N, "")

    ans = []
    for item in all_str:

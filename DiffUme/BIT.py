N = 100
bit = [0] * N

def sum(i:int) -> int:
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i

    return s

def add(i:int, x:int) -> void:
    while i <= N:
        bit[i] += x
        i += i & -i


if __name__ == "__main__":
    

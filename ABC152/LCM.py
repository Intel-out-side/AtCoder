import fractions
#import math

def LCM(*args):
    def lcm(a, b):
        gcd = fractions.gcd(a, b)
        # gcd = math.gcd(a, b)
        return a * b // gcd

    ans = lcm(args[0], args[1])
    for i in range(len(args)):
        ans = lcm(LCM, args[i])

    return ans

if __name__ == "__main__":
    print(LCM(2, 3, 4))

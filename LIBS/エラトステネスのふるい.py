class Sieve:
    """
    N以下の素数を列挙するエラトステネスのふるいです。
    O(NloglogN)でできます。

    Attributes
    sieveList : その数の素因数のうち最小のものの配列
    primes : N以下の素因数のリスト
    """
    def __init__(self, N):
        self.sieveList = [-1 for _ in range(N+1)]
        self.sieveList[1] = 1
        self.primes = []

        for i in range(2, N+1):
            #すでに何らかの数で割られていたらcontinue
            if self.sieveList[i] != -1:
                continue
            self.primes.append(i)
            for j in range(i, N+1, i):
                if self.sieveList[j] != -1:
                    continue
                self.sieveList[j] = i

    def getPrimes(self):
        return self.primes

    def getSieveList(self):
        return self.sieveList

if __name__ == "__main__":
    N = int(input())
    test = Sieve(N)
    print(test.getPrimes())
    print(test.getSieveList())

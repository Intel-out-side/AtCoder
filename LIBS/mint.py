class ModInt:
    MOD = 10**9 + 7
    def __init__(self, x):
        self.x = x % ModInt.MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, ModInt.MOD - 2, ModInt.MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, ModInt.MOD - 2, ModInt.MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, ModInt.MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, ModInt.MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, ModInt.MOD - 2, ModInt.MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, ModInt.MOD - 2, ModInt.MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, ModInt.MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, ModInt.MOD))
        )

if __name__ == "__main__":
    A = ModInt(100)
    B = ModInt(3)

    print(A / B)

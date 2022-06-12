def repetitive_pow(x, n, mod=1):
    """繰り返し二乗法

    Args:
        x (int): x^n　のx
        n (int): x^n のn
        mod (int, optional): MODが与えられている場合は指定する

    Returns:
        _type_: _description_
    """
    ans = 1
    while n:
        if n % 2:
            ans *= x
            ans %= mod
        x *= x
        x %= mod
        n = n>>1
    return ans

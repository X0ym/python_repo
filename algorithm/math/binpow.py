def binpow(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a
        a = a * a
        b >>= 1
    return res


def binpow2(a, b, m):
    a = a % m
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

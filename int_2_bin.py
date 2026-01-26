def int2bin(n: int) -> str:
    res = ""
    nve = False

    if n < 0:
        nve = True
        n = abs(n) - 1

    while n > 0:
        r = n % 2
        n = n // 2
        res = str(r) + res

    if nve:
        rev_res = ""
        for i in range(len(res)):
            if res[i] == "0":
                rev_res += "1"
            else:
                rev_res += "0"
        res = rev_res

    return res if not nve else "1" + res


print(int2bin(5))
print(int2bin(-5))
print(int2bin(-125))
print(int2bin(0))

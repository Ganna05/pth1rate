def power(a, n):
    if a == 0:
        return 0
    else:
        if n >= 0:
            if n == 0:
                return 1
            return a * power(a, n - 1)
        else:
            if n == 0:
                return 1
            return 1 / a * power(a, n + 1)


a = float(input())
n = int(input())
print(power(a, n))

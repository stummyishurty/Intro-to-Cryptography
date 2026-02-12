# ==============================
# Exercise 3
# ==============================
def exercise3_algorithm(a, b):
    u = 1
    g = a
    x = 0
    y = b

    while True:
        if y == 0:
            if b != 0:
                v = (g - a * u) // b
            else:
                v = 0
            return g, u, v

        q = g // y
        t = g - q * y
        s = u - q * x

        u, g = x, y
        x, y = s, t


# ==============================
# Exercise 4
# ==============================
def fast_power_mod(g, A, n):
    a = g % n
    b = 1

    while A > 0:
        if A % 2 == 1:
            b = (b * a) % n

        a = (a * a) % n
        A = A // 2

    return b


print(exercise3_algorithm(17, 83))
print(fast_power_mod(17, 83, 256))

import decimal


decimal.getcontext().prec = 1000
eps = 10 ** (-7)
n = 1
fact = 1

while True:
    n2 = n + 1
    if n == 1:
        x1 = n / (fact ** decimal.Decimal(1 / n))
    else:
        x1 = x2
    fact = fact * n2
    x2 = n2 / ((fact) ** decimal.Decimal(1 / n2))
    n += 1
    print((x2 - x1))
    if (x2 - x1) <= eps:
        print(n)
        break

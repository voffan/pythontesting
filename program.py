def nod(n, m):
    if n < 0 or m < 0:
        raise Exception('n<=0 or m<=0! n and m should be positive numbers!')
    elif n == 0 or m == 0:
        raise ZeroDivisionError()
    while n > 0 and m > 0:
        r = n % m
        n = m
        m = r
    return n + m


def main():
    n = int(input())
    m = int(input())
    print(nok(n,m))


if __name__ == '__main__':
    main()
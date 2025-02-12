def upper(n):
    for row in range(1, n + 1):
        print(" " * (n - row) + "* " * row)


def lower(n):
    for row in range(1, n):
        print(" " * row + "* " * (n - row))


n = int(input())
upper(n)
lower(n)

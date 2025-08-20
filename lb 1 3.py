def main():
    n = int(input().strip())
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))
    a = a[:n]

    even_vals = sorted(a[1::2])

    res = a[:]
    res[1::2] = even_vals

    print(*res)


if __name__ == "__main__":
    main()

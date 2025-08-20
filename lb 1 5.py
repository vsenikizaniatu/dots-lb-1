def main():
    n = int(input().strip())
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))
    a = a[:n]

    if n <= 1:
        print("YES")
        print(0)
        return

    a.sort()
    d = a[1] - a[0]
    ok = all(a[i] - a[i - 1] == d for i in range(2, n))

    if ok:
        print("YES")
        print(d)
    else:
        print("NO")
        print(a[-1] - a[0])


if __name__ == "__main__":
    main()

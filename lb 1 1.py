def main():
    n = int(input().strip())
    a = list(map(int, input().split()))
    while len(a) < n:
        a += list(map(int, input().split()))
    a = a[:n]

    if n <= 1:
        print(n)
        return

    inc_len = 1
    for i in range(n - 2, -1, -1):
        if a[i] <= a[i + 1]:
            inc_len += 1
        else:
            break

    dec_len = 1
    for i in range(n - 2, -1, -1):
        if a[i] >= a[i + 1]:
            dec_len += 1
        else:
            break

    print(max(inc_len, dec_len))

if __name__ == "__main__":
    main()

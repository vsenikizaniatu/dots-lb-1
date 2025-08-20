def main():
    n = int(input().strip())
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))
    a = a[:n]

    pos = sorted([x for x in a if x > 0])
    neg = sorted([x for x in a if x < 0], reverse=True)
    zeros = [0] * a.count(0)

    res = pos + neg + zeros
    print(*res)

if __name__ == "__main__":
    main()

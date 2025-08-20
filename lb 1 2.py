def main():
    n = int(input().strip())
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))
    a = a[:n]

    left, right = 0, n - 1

    while True:
        swapped = False

        for i in range(left, right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        right -= 1

        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                swapped = True
        left += 1

        print(*a)

        if not swapped or left >= right:
            break


if __name__ == "__main__":
    main()

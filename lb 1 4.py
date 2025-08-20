def main():
    digits = list(map(int, input().split()))

    if 0 in digits:
        digits = digits[:digits.index(0)]

    counts = [digits.count(i) for i in range(1, 10)]
    print(*counts)

    print(len(digits))

    print(*sorted(digits))


if __name__ == "__main__":
    main()

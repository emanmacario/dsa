from bisect import bisect_left


def binary_search(a, v, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, v, lo, hi)
    return pos if pos != hi and a[pos] == v else -1


def main():
    print(binary_search([1, 2, 3, 4, 5], 5))
    print(binary_search([1, 2, 3, 4, 5], 6))


if __name__ == "__main__":
    main()

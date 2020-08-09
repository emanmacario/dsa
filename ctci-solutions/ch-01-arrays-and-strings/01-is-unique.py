# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def is_unique(string):
    #
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)

    return True


def main():
    s1 = 'hello'
    s2 = 'world'
    print(is_unique(s1))
    print(is_unique(s2))


if __name__ == "__main__":
    main()

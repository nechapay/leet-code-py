
def reverse(x):
    res = int(str(x)[::-1]) if x >= 0 else -1 * \
        int(str(x)[1:len(str(x))][::-1])
    return res if -2**31 <= res <= 2**31 - 1 else 0


if __name__ == '__main__':
    print(reverse(-123))

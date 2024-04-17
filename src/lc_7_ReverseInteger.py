# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers(signed or unsigned).

def reverse(x):
    res = int(str(x)[::-1]) if x >= 0 else -1 * \
        int(str(x)[1:len(str(x))][::-1])
    return res if -2**31 <= res <= 2**31 - 1 else 0


if __name__ == '__main__':
    print(reverse(-123))

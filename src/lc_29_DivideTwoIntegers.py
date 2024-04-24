# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to - 2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers
# within the 32-bit signed integer range: [−231, 231 − 1]. For this problem,
# if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient
# is strictly less than - 231, then return -231.

def divide3(dividend, divisor):
    if (dividend == divisor):
        return 1

    is_positive = (divisor < 0) == (dividend < 0)
    a = dividend if dividend > 0 else -dividend
    b = divisor if divisor > 0 else -divisor
    quotient = 0

    while a >= b:
        q = 0
        while a > (b << (q+1)):
            q += 1
        quotient += 1 << q
        a = a - (b << q)
    quotient = quotient if is_positive else -quotient

    quotient = 2**31 - 1 if quotient > 2**31 - 1 else quotient
    quotient = -2**31 if quotient < -2**31 else quotient

    return quotient


def divide2(dividend, divisor):
    quotient = 1

    sign = -1 if (divisor < 0 and dividend > 0) or (
        divisor > 0 and dividend < 0) else 1

    temp_dividend = dividend if dividend > 0 else -dividend
    temp_divisor = divisor if divisor > 0 else -divisor
    if (temp_dividend == temp_divisor):
        return 1*sign
    elif temp_dividend < temp_divisor:
        return 0

    while temp_divisor << 1 <= temp_dividend:
        temp_divisor = temp_divisor << 1
        quotient = quotient << 1

    if (dividend < 0):
        quotient = quotient*sign + \
            divide(-(temp_dividend - temp_divisor), divisor)
    else:
        quotient = quotient*sign + \
            divide(temp_dividend - temp_divisor, divisor)

    quotient = 2**31 - 1 if quotient > 2**31 - 1 else quotient
    quotient = -2**31 if quotient < -2**31 else quotient

    return quotient


def divide(dividend, divisor):
    if (dividend == divisor):
        return 1
    a = dividend if dividend > 0 else -dividend
    b = divisor if divisor > 0 else -divisor
    quotient = 0
    is_positive = (divisor < 0) == (dividend < 0)

    while a >= b:
        counter = 1
        decrement = b
        while a >= decrement:
            a -= decrement
            quotient += counter
            counter += counter
            decrement += decrement

    quotient = quotient if is_positive else -quotient
    quotient = 2**31 - 1 if quotient > 2**31 - 1 else quotient
    quotient = -2**31 if quotient < -2**31 else quotient

    return quotient


if __name__ == '__main__':
    print(divide(2147483647, 2))

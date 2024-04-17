# Given an integer, convert it to a roman numeral.
def intToRoman(num):
    if num <= 0:
        return ''
    t = num
    roman = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    result = ''
    n = len(str(num)) - 1
    i = 10**n
    while i > 0:
        d = t - (t % i)
        j = t // i
        if d in roman:
            result += roman[d]
        else:
            m = j % 5
            if m != 0:
                o = (j-m)*i
                if o >= 5:
                    result += roman[o]
                for k in range((d-o)//i):
                    result += roman[i]
            else:
                for k in range(j):
                    result += roman[d//j]
        t = t % i
        i = i // 10

    return result


if __name__ == '__main__':
    print(intToRoman(3))
    print(intToRoman(1994))

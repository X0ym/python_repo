"""

"""
from string import ascii_lowercase


def char():
    # Python提供了ord和chr两个内置的函数，用于字符与ASCII码之间的转换。
    """
    ord()
        Return the Unicode code point for a one-character string.
    chr()
        Return a Unicode string of one character with ordinal i.
    """
    print(ord('a'))
    print(chr(ord('a') + 2))

    print('abc'.isalpha())
    print('a12'.isalnum())
    print('1'.isdigit())
    print('a'.islower())
    print('A'.isupper())


def str_func():
    s = "helloaa"
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - ord('a')] += 1
    print(cnt)

    print('s' * 3)

    l = []
    l.append('s')
    # l.append()
    print(chr(ord('a') + 1) * 3)
    print(ascii_lowercase[1] * 3)
    l.append(ascii_lowercase[1] * 3)

    print("".join(l))  # sbbb


if __name__ == '__main__':
    str_func()
    # char()

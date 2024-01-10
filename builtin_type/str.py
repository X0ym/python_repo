"""

"""


def str_op():
    s = "this is str template"
    print("s length: ", len(s))  # s length:  20

    # prefix and suffix
    if s.startswith("this"):
        print("s startswith this")
    else:
        print("s not startswith this")

    if s.endswith("str"):
        print("s endswith str")
    else:
        print("s not endswith str")


if __name__ == '__main__':
    str_op()

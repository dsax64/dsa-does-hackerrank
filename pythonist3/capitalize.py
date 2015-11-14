def capitalize(string):
    capitalized_string = string[0].upper()
    for i in range(1, len(string)):
        capitalized_string += string[i].upper() if string[i - 1] == " " else string[i]
    return capitalized_string


def solve():
    print capitalize(raw_input())

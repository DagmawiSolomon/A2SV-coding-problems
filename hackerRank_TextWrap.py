import textwrap


def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        if i < len(string) - max_width:
            print(string[i:i+max_width])
        elif i > len(string) - max_width:
            return string[i:len(string)]


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

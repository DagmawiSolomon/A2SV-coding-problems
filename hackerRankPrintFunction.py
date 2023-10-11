if __name__ == '__main__':
    n = int(input())
    result = []
    for i in range(n-(n-1), n+1):

        result.append(str(i))

    print("".join(result))
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(n-(n-1), n+1):
        print(i, end="")

"""

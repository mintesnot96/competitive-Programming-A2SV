def solution():
    first = input().upper()
    second = input().upper()

    result = 0
    for i, c in enumerate(first):
        if c < second[i]:
            result = -1
            break

        if c > second[i]:
            result = 1
            break

    print(result)


if __name__ == "__main__":
    solution()




# https://codeforces.com/problemset/problem/112/A

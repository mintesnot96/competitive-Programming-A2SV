input_str = input()
count_1 = count_2 = count_3 = 0
for i in range(0, len(input_str), 2):
    if input_str[i] == '1':
        count_1 += 1
    elif input_str[i] == '2':
        count_2 += 1
    else:
        count_3 += 1
result = "1+" * count_1 + "2+" * count_2 + "3+" * count_3
print(result[:-1])


# https://codeforces.com/problemset/problem/339/A

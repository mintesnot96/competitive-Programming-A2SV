k=int(input())
string=input()
char_counts = {}
b=True;
for char in string:
    char_counts[char] = char_counts.get(char, 0) + 1
# Build the first segment of the k-string
first_segment = []
for char, count in char_counts.items():
    if count % k != 0:
        # If any character has a count that is not divisible by k,
        # it is not possible to form a k-string
        b=False
        break
    first_segment.extend([char] * (count // k))

# Build the whole k-string by repeating the first segment k times
print("".join(first_segment * k)) if b else print("-1")

# question link
# https://codeforces.com/problemset/problem/219/A

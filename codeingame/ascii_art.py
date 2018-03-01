import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
t = t.upper()
t = t.replace('@', 'A')

chars = {}
for i in range(h):
    row = input()
    row_list = [row[j:j+l] for j in range(0, len(row), l)]
    for j in range(ord('A'), ord('Z') + 1):
        if not isinstance(chars.get(chr(j)), list):
            chars[chr(j)] = []
        chars[chr(j)].append(row_list[j - ord('A')])

    if not isinstance(chars.get('?'), list):
        chars['?'] = []
    chars['?'].append(row_list[-1])

text = ''
for i in range(h):
    for char in t:
        text += ''.join(chars.get(char)[i])
    text += '\n'

print(text)

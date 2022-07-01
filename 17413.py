"""
Method 3

"""
import sys
input = sys.stdin.readline
l = list(input().rstrip())

word = ''
res = ''
flag = False

for c in l:
    if c == '<':
        flag = True
        res += word
        word = c
    elif c == '>':
        flag = False
        res += word + '>'
        word = ''
    elif c == ' ':
        res += word + c
        word = ''
    elif flag:
        word += c
    else:
        word = c + word

print(res+word)


"""
Method 2

"""
import sys
input = sys.stdin.readline
l = list(input().rstrip())
flag = False
word = ''
res = ''

for i in l:
    if flag == False:
        if i == '<':
            flag = True
            word += i
        elif i == ' ':
            word += i
            res += word
            word = ''
        else:
            word = i + word

    elif flag:
        word += i
        if i == '>':
            flag = False
            res += word
            word = ''

print(res+word)


"""
Method 1

"""

import sys
input = sys.stdin.readline
l = list(input().rstrip())
res = []
flag = False
tmp = ''
for i in range(len(l)):
    if l[i] == '<':
        if tmp not in '':
            res.append(tmp[::-1])
            tmp = ''
        res.append(l[i])
        flag = True
        continue

    if l[i] == '>':
        res.append(l[i])
        flag = False
        continue

    if flag:
        res.append(l[i])
        continue

    if l[i] == ' ':
        res.append(tmp[::-1]+l[i])
        tmp = ''
        continue

    if i == len(l)-1:
        tmp += l[i]
        res.append(tmp[::-1])
        break

    tmp += l[i]

print(''.join(res))

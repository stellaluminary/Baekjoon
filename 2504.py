"""
Method 2

"""

s = list(input())
stack = []
ans = 0
tmp = 1

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        tmp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        tmp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if s[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2
    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if s[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)


"""
Method 1

개인 시도 - 실패
"""

s = list(input())
print(s)

flag = False
print(s.count('('), s.count(')'), s.count('['), s.count(']'))
if s.count('(') != s.count(')') or s.count('[') != s.count(']'):
    print(0)
else:
    while s:
        tmp = []
        for i in range(len(s)):
            tmp.append(s[i])
            print('tmp init', i, tmp)
            if s[i] == ')':
                if s[i-1] == '(':
                    del tmp[-2:]
                    tmp.append(str(2))
                elif s[i-2] == '(':
                    if s[i-1].isnumeric():
                        num = int(s[i-1]) * 2
                        del tmp[-3:]
                        tmp.append(str(num))
                    elif not s[i-1].isnumeric():
                        flag = True
                        break

            if s[i] == ']':
                if s[i-1] == '[':
                    del tmp[-2:]
                    tmp.append(str(3))
                elif s[i-2] == '[':
                    if s[i-1].isnumeric():
                        num = int(s[i-1]) * 3
                        del tmp[-3:]
                        tmp.append(str(num))
                    elif not s[i-1].isnumeric():
                        print(s[i-1])
                        flag = True
                        break

            if i > 0 and s[i].isnumeric() and s[i-1].isnumeric():
                num = int(s[i-1]) + int(s[i])
                del tmp[-2:]
                tmp.append(str(num))

        s = tmp
        print('tmp after', tmp)

        if flag:
            print(0)
            break

        if len(tmp) == 1 and ''.join(tmp).isnumeric():
            print(tmp[-1])
            break

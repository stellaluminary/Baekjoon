"""
Method 2

"""

s = input()
alpha_n = [0] * 26
for i in s:
    alpha_n[ord(i)-ord('A')] += 1

odd = 0
odd_tmp = ''
strt = ''

for i in range(len(alpha_n)):
    if alpha_n[i] % 2 == 1:
        odd += 1
        odd_tmp += chr(i+ord('A'))
    strt += chr(i+ord('A')) * (alpha_n[i] // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(strt + odd_tmp + strt[::-1])

"""
Method 1

"""

def palindrome():
    even_tmp = ''
    odd_tmp = ''

    if len(odd):
        odd_tmp += odd[0][0]
        even_tmp += odd[0][0] * ((odd[0][1] - 1)//2)

    for i in range(len(even)):
        even_tmp += even[i][0] * (even[i][1]//2)

    srts = sorted(even_tmp)
    res = ''.join(srts) + odd_tmp + ''.join(srts[::-1])
    print(res)

s = input()
alpha = [0] * 26
for i in s:
    alpha[ord(i)-ord('A')] += 1

odd = []
even = []
for i in range(len(alpha)):
    if alpha[i]:
        if alpha[i] % 2 == 0:
            even.append((chr(i + ord('A')), alpha[i]))
        else:
            odd.append((chr(i + ord('A')), alpha[i]))

if len(odd) > 1:
    print('I\'m Sorry Hansoo')
else:
    palindrome()

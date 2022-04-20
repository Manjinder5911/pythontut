# pattern of alphabets
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print(s)
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print(L)
print('\n'.join(L[:0:-1]+L))

# Minion game
vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        print(s[i])
        kevsc += (len(s) - i)
    else:
        stusc += (len(s) - i)

if kevsc > stusc:
    print("Kevin", kevsc)
elif kevsc < stusc:
    print("Stuart", stusc)
else:
    print("Draw")



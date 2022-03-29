# Eduardo Zanetta - 20203087

'''
a = 2
b = 22
c = 222
d = 3
e = 33
f = 333
'''

n = int(input())

def substitute(char, number, text_arg):
    if char in text_arg:
        new_text = text_arg.replace(char, number)
        return new_text

for i in range(0, n):
    text = input()
    substitute('a', '2', text)
    substitute('b', '22', text)

print(text)

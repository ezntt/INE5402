# -*- coding: utf-8 -*-

# input do usuário
a = int(input())
b = int(input())

# condicionais conforme o problema solicita
if (a >= 14) and (b >= 14):
    print("YES")
elif (6 <= a <= 13) and (b >= 18):
    print("YES")
elif (6 <= b <= 13) and (a >= 18):
    print("YES")
else:
    print("NO")
# -*- coding: utf-8 -*-

# input do tipo split (na mesma linha, separados por espaço)
h, e, a, o, w, x = input().split()

h = int(h) # humanos
e = int(e) # elfos
a = int(a) # anões
o = int(o) # orcs
w = int(w) # wargs
x = int(x) # águias

# middle-earth ganha a guerra
if (h + e + a > o + w):
    print("Middle-earth is safe.") 
elif (h + e + a <= o + w):
    # middle-earth ganha a guerra
    if (h + e + a + x >= o + w):
        print("Middle-earth is safe.")
    # middle-earth perde a guerra
    else:
        print("Sauron has returned.")
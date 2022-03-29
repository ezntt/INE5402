# Eduardo Zanetta - 20203087

# input terreno a
ax1, ay1 = [int(x) for x in input().split()]
ax2, ay2 = [int(x) for x in input().split()]
ax3, ay3 = [int(x) for x in input().split()]
ax4, ay4 = [int(x) for x in input().split()]
# input terreno b
bx1, by1 = [int(x) for x in input().split()]
bx2, by2 = [int(x) for x in input().split()]
bx3, by3 = [int(x) for x in input().split()]
bx4, by4 = [int(x) for x in input().split()]

# cálculo da área sabendo os vértices
a = abs((((ay1 * ax2) + (ay2 * ax3) + (ay3 * ax4) + (ay4 * ax1)) - ((ax1 * ay2) + (ax2 * ay3) + (ax3 * ay4) + (ax4 * ay1))) / 2)
b = abs((((by1 * bx2) + (by2 * bx3) + (by3 * bx4) + (by4 * bx1)) - ((bx1 * by2) + (bx2 * by3) + (bx3 * by4) + (bx4 * by1))) / 2)


# output
if a > b:
    print('terreno A')
else:
    print('terreno B')

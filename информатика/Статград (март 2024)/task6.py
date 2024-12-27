


pos = [0, 0]
dir = [0, 1]

picture = { tuple(pos): 1 }

def fd(n):
    for _ in range(n):
        for i in range(2): pos[i] += dir[i]
        if tuple(pos) not in picture: picture[tuple(pos)] = 0
        picture[tuple(pos)] += 1

def rt():
    dir[0], dir[1] = dir[1], -dir[0]


for _ in range(4):
    for _ in range(4):
        fd(7)
        rt()
    fd(10)
    rt()
    fd(4)

print(len([pos for pos in picture if picture[pos] == 2]))



def b(n):
    return f"{n:b}".rjust(8, "0")

print(f"{b(200)}.{b(60)}.{b(130)}.{b(4)}")
print(f"{b(200)}.{b(60)}.{b(140)}.{b(44)}")
print(f"{b(200)}.{b(60)}.{b(150)}.{b(48)}")

from itertools import product

c = 0
for part in product("01", repeat=12):
    st = "11001000001111001000"
    
    if (st + ''.join(part)).count("1") == 10:
        c += 1
print(c)
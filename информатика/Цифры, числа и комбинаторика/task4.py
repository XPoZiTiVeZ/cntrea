from itertools import product

c = 0
for num in product("012345678", repeat=5):
    num = ''.join(num)
    if num != str(int(num)): continue
    if num.count("5") != 1:  continue
    if num.find("5") == 4 or int(num[num.find("5")+1]) % 2 == 0: continue
    
    print(num)
    c += 1
print(c)
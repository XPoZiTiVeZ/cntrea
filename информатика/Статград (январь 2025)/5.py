def encode(n):
    res = ""
    
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    
    return res

def change(s):
    res = ""
    for l in s:
        if l == "0": res += "2"
        elif l == "2": res += "0"
        else: res += l
    return res

for i in range(1, 10_864_246):
    N = i
    Nt = encode(N)
    Nc = change(Nt)
    Nd = int(Nc, 3)
    R = abs(Nd - N)
    
    if R == 1_864_246:
        print(N)
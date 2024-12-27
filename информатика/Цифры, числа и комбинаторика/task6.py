ip = "0" + bin(94)[2:] + bin(253)[2:] + bin(128)[2:] + "0" * 8
mask = "1" * 17 + "0" * 15

print(ip)
print(mask)
# 15 - 12
# 15 - 3
# 24 - 9
# 30 - 15
# print(120 + 10)
ip = "01011110111111011"
c = 0
for i in range(2**12):
    new_ip = ip + f"{bin(i)[2:]:0>12}101"
    if new_ip.count("1") % 6 == 0: continue
    
    c += 1
print(c)
" 2416?9"
"1000000000"

# n1 = product(range(10), repeat=3)
# n2 = product(product(range(10), repeat=2), range(10))
# n3 = product(range(10), product(range(10), repeat=2))
# n4

# from itertools import product
# for p1 in product(range(10), repeat=3):
#     for p2 in product(range(10), repeat=3):
#         for x in range(10):
#             s1 = ''.join([str(n) for n in p1])
#             s2 = ''.join([str(n) for n in p2])
#             s = str(x)
            
#             if len(f"2{s1}41{s2}6{s}9") > 9: continue
            
#             print(int(f"2{s1}41{s2}6{s}9"))
#             if int(f"2{s1}41{s2}6{s}9") % 9517 == 0:
#                 print(int(f"2{s1}41{s2}6{s}9"))



for n in range(0, 10**9, 9517):
    sn = str(n)
    if sn[0] != "2": continue
    if sn[-3] != "6": continue
    if sn[-1] != "9": continue
    if sn[1:-3].find("41") == -1: continue
    
    print(sn)
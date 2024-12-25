s = "01" + "2" * 176 + "3" * 21 + "0"
print(sum([int(n) for n in s]))
while s.find("00") == -1:
    s = s.replace("011", "201",   1) # +y2    | -x1
    s = s.replace("03",  "220",   1) # +2y2 | -z1
    s = s.replace("02",  "210",   1) # +y2 +x2 | -y1
    s = s.replace("012", "2101",  1) # +y2 +x2 | -y1
    s = s.replace("013", "12101", 1) # +2x2 +y2 | -z1
    s = s.replace("010", "1100",  1) # +2x2 | -x1

print(s, s.count("1"), s.count("2"), s.count("3"))

# 1 - x1
# 2 - y1
# 3 - z1
# 
# x1 + y1 + z1 = 200
# 
# x2 = 220
# y2 = 197
# z2 = 0

# y + 2x = 220
# y + x = 197
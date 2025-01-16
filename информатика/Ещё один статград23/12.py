s = ""
while s.find("00") == -1:
    s = s.replace("02", "101")
    s = s.replace("11", "2")
    s = s.replace("012", "30")
    s = s.replace("010", "00")
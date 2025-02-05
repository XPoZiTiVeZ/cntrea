def gs(s, tones):
    print(s, tones)
    if len(s) == 0:
        return gs(s + "1", tones - 1) + gs(s + "2", tones)
    else:
        if s[-2:] != "11" and tones > 0 and s[-1] != "2":
            return gs(s + "1", tones - 1) + gs(s + "2", tones)
        elif s[-1] != "2":
            return gs(s + "2", tones)
        elif s[-2:] != "11" and tones > 0:
            return gs(s + "1", tones - 1)
        return [s]
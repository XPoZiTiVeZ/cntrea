def hash(i: int, word: str):
    l = word[i]
    lu = l.upper()
    if i == -1: return 17
    return (hash(i - 1, word) * ord(lu) + 7) % 113

word = "YjYtLjktntkf"
print(hash(len(word)-1, word))
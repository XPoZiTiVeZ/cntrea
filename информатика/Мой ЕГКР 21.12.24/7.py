res_bits = 3840 * 2160
col_bits = 24
photo_w = res_bits * col_bits
gb16 = 2 ** 37

photo_c = 0
for i in range(3742):
    if photo_c * photo_w >= gb16: photo_c = 1
    else: photo_c += 1

print(photo_c)
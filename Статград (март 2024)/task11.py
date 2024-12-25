# 5880 * 2 ** 10 / 2048 = 2940
# N * (6 * 7 + log_2(N - 1)) = 2940
# N * (42 + log_2(N) = 2940

from math import log2, ceil
for i in range(1, 2940):
    if i * ceil((42 + ceil(log2(i))) / 8) == 2940:
        print(i)
c = 0
for row in open("9.txt").read().splitlines():
    nums = [int(n) for n in row.split()]
    max_n = max(nums)
    
    if nums.count(max_n) != 1: continue
    if nums[:4].count(max_n) != 1: continue
    if sum(nums[:4]) / 4 >= sum(nums[4:]) / 4: continue
    
    c += 1
print(c)
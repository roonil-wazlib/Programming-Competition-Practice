from functools import lru_cache

info = input().split(" ")
size = int(info[0])
rug = int(info[1])

room = []

for i in range(size):
    room.append(input())
    
        
def count_dirty(i, j, rug):
    count = 0
    a = i
    r = rug
    while True:
        count += count_dirty_down(a, j)
        if rug == 1:
            break
        a += 1
        rug -= 1
    return count

@lru_cache(None)
def count_dirty_down(i, j):
    count = 0
    b = j
    r = rug
    while True:
        if room[i][b] == "D":
            count += 1
        if r == 1:
            break
        
        b += 1
        r -= 1
    return count

num_ways = {}
    
for i in range(size - rug + 1):
    for j in range(size - rug + 1):
        num = count_dirty(i, j, rug)
        if num in num_ways:
            num_ways[num] += 1
        else:
            num_ways[num] = 1
            
            
output = []
for key, value in sorted(num_ways.items()):
    print("{} {}".format(key, value))
    
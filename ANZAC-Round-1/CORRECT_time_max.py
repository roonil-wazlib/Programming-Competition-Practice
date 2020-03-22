import math

info = input().split(" ")

s = int(info[1])

times = input().split(" ")

max_time = int(max(times, key=lambda x : int(x)))

print(math.ceil(max_time * s / 1000))
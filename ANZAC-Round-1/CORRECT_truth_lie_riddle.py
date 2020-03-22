people = int(input())
ranges = []
for i in range(people):
    domain = input().split(" ")
    ranges.append((int(domain[0]), int(domain[1])))
    
max_true = -1
for i in range(people):
    true = 0
    for item in ranges:
        if i >= item[0] and i <= item[1]:
            true += 1
            
    if true == i:
        max_true = i
        
        
        
print(max_true)
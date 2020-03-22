correct = int(input())
friend = input()
you = input()
n = len(friend)


same = 0
diff = 0
for i in range(n):
    if you[i] == friend[i]:
        same += 1
        
    else:
        diff += 1
        
        
print(min(n - correct, diff) + min(correct, same))
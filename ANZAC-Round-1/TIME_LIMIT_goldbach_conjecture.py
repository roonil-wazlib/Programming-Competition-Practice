import math

primes = []

value = int(input())

for i in range(value + 1):
    primes.append(i)
   
    
for i in range(2, int(math.sqrt(value))):

    if primes[i] != -1:
        j = 2 * i
        while True:
            if j >= len(primes):
                break
            else:
                primes[j] = -1
            j += i
            
primes = [x for x in primes if x >= 2]

def binary_search(ls, x, start, end):
    if start > end:
        return None
    
    if end == start + 1:
        if ls[start] == x:
            return x
        else:
            return None
        
    midpoint = int((start + end) / 2)
    if x == ls[midpoint]:
        return x
    elif ls[midpoint] > x:
        end = midpoint
    else:
        start = midpoint
        
    return binary_search(ls, x, start, end)


def goldbach(value):
    count = 0
    while True:
        if value < 3:
            break
        
        max_diff = 0
        for i in primes:
            val2 = binary_search(primes, value - i, 0, len(primes))
            if val2 is not None:
                max_diff = abs(i - val2)
                break

        count += 1
        value = max_diff
    return count

    
print(goldbach(value))
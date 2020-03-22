info = input().split(" ")
max_index = int(info[0])
rotation = int(info[1])

vector1 = set([int(x) for x in input().split(" ")[1:]])
vector2 = set([int(x) for x in input().split(" ")[1:]])

union = vector1.union(vector2)
intersection = vector1.intersection(vector2)

sum_vector = set()
multiplication_vector = set()
for value in union:
    if value in intersection:
        sum_vector.add(value)
        multiplication_vector.add(abs(value))
    elif value in vector1 and -1 * value in vector2 or value in vector2 and -1*value in vector1:
        multiplication_vector.add(-abs(value))
    else:
        sum_vector.add(value)
        
        
vector1_rotation = set()
vector2_rotation = set()

for value in vector1:
    index = abs(value)
    new_index = (index - rotation) % max_index
    new_value = new_index
    if new_value == 0:
        new_value = max_index    
    if value < 0:
        new_value *= -1
    vector1_rotation.add(new_value)
    
for value in vector2:
    index = abs(value)
    new_index = (index - rotation) % max_index
    new_value = new_index
    if new_value == 0:
        new_value = max_index    
    if value < 0:
        new_value *= -1
    vector2_rotation.add(new_value)
    
        
print(len(sum_vector), " ".join(str(x) for x in sorted(sum_vector, key=abs)))
print(len(multiplication_vector), " ".join(str(x) for x in sorted(multiplication_vector, key=abs)))
print(len(vector1_rotation), " ".join(str(x) for x in sorted(vector1_rotation, key=abs)))
print(len(vector2_rotation), " ".join(str(x) for x in sorted(vector2_rotation, key=abs)))
    


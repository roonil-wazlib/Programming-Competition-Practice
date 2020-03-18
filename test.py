

def find_hori(crossword):
    hori_words = []
    hori_indices = []
    for index, x in enumerate(crossword):
        current_word = ""
        for y_index, y in enumerate(x):
            if y != "@":
                current_word += y
                if len(current_word) == 1:
                    hori_indices.append((index, y_index))
            else:
                if len(current_word) > 2:
                    hori_words.append(current_word)
                elif len(current_word) != 0:
                    hori_indices.pop()
                current_word = ""
        if len(current_word) > 2:
            hori_words.append(current_word)
        elif len(current_word) != 0:
            hori_indices.pop()
                
    return hori_words, hori_indices



def find_vert(crossword):
    vert_words = []
    vert_indices = []
    for x in range(len(crossword[-1])):
        current_word = ""
        for y in range(len(crossword)):
            if crossword[y][x] != "@":
                current_word += crossword[y][x]
                if len(current_word) == 1:
                    vert_indices.append((y, x))                
            else:
                if len(current_word) > 2:
                    vert_words.append(current_word)
                elif len(current_word) != 0:
                    vert_indices.pop()
                current_word = ""
        if len(current_word) > 2:
            vert_words.append(current_word)
        elif len(current_word) != 0:
            vert_indices.pop()
        current_word = ""        
                
    return vert_words, vert_indices
                
                
                
def print_crossword(hori, vert, hori_i, vert_i, count):
    print("Crossword puzzle {}".format(count))
    print("Across")
    sorted_indices = sorted(list(set(hori_i + vert_i)))
    accross_output = []
    for index, item in enumerate(hori):
        for index2, item2 in enumerate(sorted_indices):
            if item2 == hori_i[index]:
                accross_output.append(("{}.  ({})".format(index2+1, len(item))))
                
    for item in sorted(accross_output, key=sort):
        print(item)

    print("Down")
    down_output = []
    for index, item in enumerate(vert):
        for index2, item2 in enumerate(sorted_indices):
            if item2 == vert_i[index]:
                down_output.append("{}.  ({})".format(index2+1, len(item)))
                
    down_output.reverse()
    for item in sorted(down_output, key=sort):
        print(item)
                
                
def sort(item):
    num = ""
    for i in item:
        if i != ".":
            num += i
        else:
            break
    return int(num)
                
count = 1
going = True
while going:
    info = input()
    if info == "0 0":
        going = False
    else:
        info = info.split(" ")
        
        if count != 1:
            print()
            
        depth = int(info[0])
        width = int(info[1])
        
        crossword = []
        for i in range(depth):
            row = list(input())
            crossword.append(row)
        
        
        hori, hori_i = find_hori(crossword)
        vert, vert_i = find_vert(crossword)
        print_crossword(hori, vert, hori_i, vert_i, count)
        
        count += 1
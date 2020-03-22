dim = input().split(" ")
rows, cols = int(dim[0]), int(dim[1])


plan = []

for _ in range(rows):
    plan.append([int(x) for x in input().split(" ")])
    


output = []
output.append(['0'] * cols)

for i in range(1, rows - 1):
    output_row = ['0']
    for j in range(cols - 2):
        cell = plan[i][j+1]
        if cell > plan[i][j]:
            output_row.append('0')
        else:
            if cell < plan[i-1][j+1] and cell < plan[i+1][j+1] and cell < plan[i][j+2]:
                output_row.append('1')
            else:
                output_row.append('0')
            
            
    output_row.append('0')
    output.append(output_row)
    
    
output.append(['0'] * cols)


for row in output:
    print(" ".join(row))
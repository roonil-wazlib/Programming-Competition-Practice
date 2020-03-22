info = input().split(" ")

x, y = int(info[0]), int(info[1])

x1, y1 = int(info[2]), int(info[3])
x2, y2 = int(info[4]), int(info[5])


if x <= x2 and x >= x1:
    distance = min(abs(y-y1), abs(y-y2))
    
elif y <= y2 and y>= y1:
    distance = min(abs(x-x1), abs(x-x2))
    
else:
    #need diagonal to nearest corner
    y_dist = min(abs(y-y1), abs(y-y2))
    x_dist = min(abs(x-x1), abs(x-x2))
    distance = (x_dist**2 + y_dist**2)**(0.5)
    
    
print("{:.3f}".format(distance))
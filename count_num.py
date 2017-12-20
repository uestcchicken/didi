import numpy as np 

file_movement = open('movement.txt', 'r')
lines_movement = file_movement.readlines()
file_movement.close()

lines_movement = [l.split() for l in lines_movement]
for l in lines_movement:
    l[1] = int(l[1])
    if l[3] == '东':
        l[3] = 0
    elif l[3] == '南':
        l[3] = 1
    elif l[3] == '西':
        l[3] = 2
    elif l[3] == '北':
        l[3] = 3
    else:
        print('wrong!!!')
        break
    
    if l[4] == '东':
        l[4] = 0
    elif l[4] == '南':
        l[4] = 1
    elif l[4] == '西':
        l[4] = 2
    elif l[4] == '北':
        l[4] = 3
    else:
        print('wrong!!!')
        break
    
print(lines_movement[:5])

counter = np.zeros((7, 4, 4), dtype = 'uint32')

for l in lines_movement:
    crossing = l[1] - 1
    counter[crossing][l[3]][l[4]] += 1
print(counter)
    
    
    
    
    
    
    
    
    
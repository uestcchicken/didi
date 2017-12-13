file_direction = open('direction.txt', 'r')
lines_direction = file_direction.readlines()
file_direction.close()

lines_direction = [l.split() for l in lines_direction]
print(len(lines_direction))
print(lines_direction[0])

last2 = ''
last1 = ''
found1 = 0
res = []
for i in range(len(lines_direction)):
    
    if found1 == 1 and lines_direction[i][0] == last2:
        res.append(i)
        res.append(i - 1)
        found1 = 0
    elif lines_direction[i][0] == last2:
        found1 = 1
    else:
        found1 = 0
    last2 = last1
    last1 = lines_direction[i][0]

out = []
for i in range(len(lines_direction)):
    if not (i in res):
        out.append(lines_direction[i])

    
    
print(len(lines_direction))
print(len(out))
print(len(res))


file_direction = open('direction_fined.txt', 'w')
for l in out:
    line = ''
    for j in l:
        line += j + ' '
    line += '\n'


    file_direction.writelines(line)
file_direction.close()















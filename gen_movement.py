import numpy as np

DIRECTION_FILE = 'direction_fined.txt'
OUT_FILE = 'movement.txt'

file_direction = open(DIRECTION_FILE, 'r')
lines_direction = file_direction.readlines()
lines_direction = [l.split() for l in lines_direction]


def findturn(car, start, end, file_out):
    if start == 0 and end == 0:
        return 0
    if start == end:
        return 0
    
    #if start < 37200:
        #return 0
    #print('###############', car, start, end)
    #for i in range(start, end):
        #print(lines_direction[i])
    
    last_crossing = lines_direction[start][1]
    if last_crossing != '0':
        #print('in')
        cross_in = start
        cross_num = last_crossing
    for i in range(start + 1, end):
        line = lines_direction[i]
        
        if last_crossing == '0' and line[1] != '0':
            #print('in')
            cross_in = i
            cross_num = line[1]
        elif line[2] == '*****':
            #print('out1')
            cross_out = i
            #print(car, cross_num, cross_in, cross_out)
            get_movement(car, cross_num, cross_in, cross_out, file_out)
            findturn(car, i + 1, end, file_out)
            break
        elif last_crossing != '0' and line[1] == '0':
            #print('out2')
            cross_out = i
            #print(car, cross_num, cross_in, cross_out)
            get_movement(car, cross_num, cross_in, cross_out, file_out)
        
        elif last_crossing != '0' and i == end - 1:
            #print('out3')
            cross_out = i + 1
            #print(car, cross_num, cross_in, cross_out)
            get_movement(car, cross_num, cross_in, cross_out, file_out)
        else:
            pass
        last_crossing = line[1]
        
def get_movement(car, num, lin, lout, file_out):
    time = lines_direction[lin][0]
    for i in range(lin, lout):
        if lines_direction[i][2] != '停' and lines_direction[i][2] != '*****':
            start = lines_direction[i][2]
            break
        return 0
    for i in range(lout - 1, lin - 1, -1):
        if lines_direction[i][2] != '停' and lines_direction[i][2] != '*****':
            end = lines_direction[i][2]
            break
        return 0
    file_out.writelines(car + ' ' + str(num) + ' ' + time + ' ' + start + ' ' + end + '\n')
    
        
file_out = open(OUT_FILE, 'w')
car = ''
start = 0
end = 0

for i in range(len(lines_direction)):
    line = lines_direction[i]
    if len(line) == 1:
        end = i
        findturn(car, start, end, file_out)
        start = i + 1
        car = line[0]
    
    
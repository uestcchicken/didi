import numpy as np 
import math

TRAIL_FILE = 'trail.txt'
OUT_FILE = 'direction.txt'

def incrossing(x, y):
    x_crossing = [521677, 521580, 521520, 521452, 521433, 521411, 521400]
    y_crossing = [58109, 57466, 57059, 56668, 55855, 54822, 53998]

    for i in range(7):
        #if (x - x_crossing[i]) ** 2 <= 8100 and (y - y_crossing[i]) ** 2 <= 8100:
        if (x - x_crossing[i]) ** 2 + (y - y_crossing[i]) ** 2 <= 10000:
            return i + 1
    return 0

file_trail = open(TRAIL_FILE, 'r')
lines_trail = file_trail.readlines()
data_trail = [l[:-2].split(',') for l in lines_trail[1:]]

file_out = open(OUT_FILE, 'w')

cars = []
formal = ''
for line in data_trail:
    if formal != line[0]:
        formal = line[0]
        cars.append(formal)
print('cars num: ' + str(len(cars)))  

for car in cars:
    print(car)
    file_out.writelines(car + '\n')
    x = 0.0
    y = 0.0
    for line in data_trail:
        if line[0] == car:
            if x == 0.0:
                x = float(line[2])
                y = float(line[3])
                t = float(line[1])
            else:
                x_ = float(line[2])
                y_ = float(line[3])
                t_ = float(line[1])
                crossing = incrossing(x_, y_)
                
                if t_ - t > 10 or t_ - t < 0:
                    file_out.writelines(line[1] + ' ' + str(crossing) + ' ' + '*****\n')
                    x = float(line[2])
                    y = float(line[3])
                    t = float(line[1])
                    continue
                
                if x == x_ and y == y_:
                    file_out.writelines(line[1] + ' ' + str(crossing) + ' ' + '停\n')
                    t = float(line[1])
                    continue
                
                if y_ > y and x == x_:
                    file_out.writelines(line[1] + ' ' + str(crossing) + ' ' + '北' + ' ' + line[4] + '\n')
                    y = float(line[3])
                    t = float(line[1])
                    continue
                if y_ < y and x == x_:
                    file_out.writelines(line[1] + ' ' + str(crossing) + ' ' + '南' + ' ' + line[4] + '\n')
                    y = float(line[3])
                    t = float(line[1])
                    continue
                k = (y_ - y) / (x_ - x)
                angle = math.atan(k)
                 
                if x_ < x:
                    direction = 180 + angle / 3.1416 * 180
                else:
                    direction = angle / 3.1416 * 180
                
                if direction > 180:
                    direction = direction - 360
                    
                if direction > -45 and direction < 45:
                    d = '东'
                elif direction >= 45 and direction < 135:
                    d = '北'
                elif direction >= 135 or direction < -135:
                    d = '西'
                else:
                    d = '南'

                file_out.writelines(line[1] + ' ' + str(crossing) + ' ' + d + ' ' + line[4] + ' ' + '\n')
                x = float(line[2])
                y = float(line[3])
                t = float(line[1])
file_out.close()
            

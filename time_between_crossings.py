MOVEMENT_FILE = 'movement.txt'

file_movement = open(MOVEMENT_FILE, 'r')
lines_movement = file_movement.readlines()
file_movement.close()

lines_movement = [l.split() for l in lines_movement]
#print(len(lines_movement))

time12 = []
time23 = []
time34 = []
time45 = []
time56 = []
time67 = []


for i in range(1, len(lines_movement)):
    if lines_movement[i - 1][0] == lines_movement[i][0]:
        if (int(lines_movement[i][1]) - int(lines_movement[i - 1][1]) == 1) and (lines_movement[i - 1][4] == '南'):
            crossing1 = int(lines_movement[i - 1][1])
            crossing2 = int(lines_movement[i][1])
            time = int(lines_movement[i][2]) - int(lines_movement[i - 1][2])
            #print(crossing1, crossing2, time)
            crossing = crossing1
            if crossing == 1:
                time12.append(time)
            elif crossing == 2:
                time23.append(time)
            elif crossing == 3:
                time34.append(time)
            elif crossing == 4:
                time45.append(time)
            elif crossing == 5:
                time56.append(time)
            elif crossing == 6:
                time67.append(time)
            else:
                print('wrong!!!!')
        if (int(lines_movement[i][1]) - int(lines_movement[i - 1][1]) == -1) and (lines_movement[i - 1][4] == '北'):
            crossing1 = int(lines_movement[i - 1][1])
            crossing2 = int(lines_movement[i][1])
            time = int(lines_movement[i][2]) - int(lines_movement[i - 1][2])
            #print(crossing1, crossing2, time)
            crossing = crossing2
            if crossing == 1:
                time12.append(time)
            elif crossing == 2:
                time23.append(time)
            elif crossing == 3:
                time34.append(time)
            elif crossing == 4:
                time45.append(time)
            elif crossing == 5:
                time56.append(time)
            elif crossing == 6:
                time67.append(time)
            else:
                print('wrong!!!!')

for time_using in [time12, time23, time34, time45, time56, time67]:        
    '''
    for i in range(len(time_using)):
        if time_using[i] < 0:
            #print(time12[i])
            time_using[i] = 0
        if time_using[i] > 100:
            #print(time12[i])
            time_using[i] = 0

    counter = 0  
    s = 0  
    for i in time_using:
        if i != 0:
            counter += 1
            s += i
    print(s / counter)
    '''
    for i in range(len(time_using)):
        if time_using[i] < 0:
            #print(time12[i])
            time_using[i] = 10000
    print(min(time_using))



import math

def direct(din, dout):
    return din * 4 + dout

distance = []
distance.append(math.sqrt(97 ** 2 + (1109 - 466) ** 2))
distance.append(math.sqrt(60 ** 2 + 407 ** 2))
distance.append(math.sqrt(68 ** 2 + (1059 - 668) ** 2))
distance.append(math.sqrt(19 ** 2 + (1668 - 855) ** 2))
distance.append(math.sqrt(22 ** 2 + (1855 - 822) ** 2))
distance.append(math.sqrt(11 ** 2 + (1822 - 998) ** 2))

file_movement = open('movement.txt', 'r')
lines_movement = file_movement.readlines()
file_movement.close()

lines_movement = [l.split() for l in lines_movement]
#print(lines_movement[:3])

times = [int(l[2]) for l in lines_movement]
time_start = min(times)

for l in lines_movement:
    l[2] = int(l[2]) - time_start
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
#print(lines_movement[:3])


plans = []
d = [10]

for i in range(1, len(lines_movement)):
    lnow = lines_movement[i]
    llast = lines_movement[i - 1]
    
    if lnow[0] == llast[0] and lnow[1] == llast[1] + 1 and llast[4] == 1 and lnow[2] - llast[2] < 300:
        d.append(direct(lnow[3], lnow[4]))
    elif lnow[0] == llast[0] and lnow[1] == llast[1] - 1 and llast[4] == 3 and lnow[2] - llast[2] < 300:
        d.append(direct(lnow[3], lnow[4]))
    else:
        lstart = lines_movement[i - len(d)]
        plans.append([lstart[0], lstart[1], lstart[2], d])
        d = [direct(lnow[3], lnow[4])]

plans.sort(key = lambda k: (k[2]))

for p in plans[-20:]:
    print(p)

print('################################################')


####################################################

def get_light(time, c, direction):
    crossing = c - 1
    
    
    bias = [0, 27, 42, 56, 95, 143, 179]
    term = [200, 200, 200, 200, 200, 200, 200]
    sch = [[111, 9, 43, 37], \
        [28, 121, 13, 38], \
        [28, 134, 38], \
        [34, 75, 31, 19, 41], \
        [48, 89, 63], \
        [35, 67, 52, 46], \
        [30, 96, 74]]
    
    cross_time = (time - bias[crossing]) % term[crossing]
    cross_sch = sch[crossing]
    #for i in range(cross_sch):
        
    
        
        
    


    return (time + crossing + direction) % 2




def next_crossing(now, d):
    if now >= 1 and now <= 6 and d == 5:
        return now + 1
    elif now >= 2 and now <= 7 and d == 15:
        return now - 1
    else:
        return 0



####################################################
running = []
loss = 0

pointer = 0
maxpointer = len(plans)
for time in range(1150000):
    while(plans[pointer][2] == time):
        p = plans[pointer]
        running.append([p[0], p[1], 5, 0, p[3]])
        
        if pointer == maxpointer - 1:
            pointer = 0
        else:
            pointer += 1
        
        
    for r in running:

        if r[2] == -1:
            light = get_light(time, r[1], r[4][0])
            if light == 0:
                r[3] += 1
            else:
                r[1] = next_crossing(r[1], r[4][0])
                r[2] = 20
                loss += r[3]
                r[3] = 0

                r[4] = r[4][1:]
                if r[4] == []:
                    r[0] = ' '
                
        else:
            #print('kkkkkkkkkkkkkkk')
            r[2] = r[2] - 1
            if r[2] == 0:
                light = get_light(time, r[1], r[4][0])
                if light == 0:
                    #print('k00000000')
                    loss += 10
                    r[2] = -1
                    r[3] += 1
                else:
                    #print('k11111111')
                    r[1] = next_crossing(r[1], r[4][0])
                    r[2] = 20
                    r[3] = 0
                    r[4] = r[4][1:]
                    if r[4] == []:
                        #print('ooooooooooo')
                        r[0] = ' '
                        #print(r)
    
    i = 0
    while(i < len(running)):
        #print('lllllllllllll', i)
        r = running[i]
        
        if r[0] == ' ':
            running.remove(running[i])
            #print(i)
            i -= 1  
            #print(i)  
        i += 1

            
    #for r in running:
        #print(r)
    #print(time, '################################################')

print(loss)    














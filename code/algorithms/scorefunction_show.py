from code.constraints.capacity import capacity
from code.constraints.overlap_simulated import overlapping
from code.constraints.order import order
import time
from code.constraints.distribution import distribution

def scorefunction_show(schedule, courses, rooms, overlap_dict):

    malus = 0;

    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            for k in range(len(schedule[i][j])):
                if schedule[i][j][k] != None:
                    if j == 4:
                        malus = malus + 20
                        # print('malus 20 points')
                capacity_show = capacity(schedule[i][j][k], rooms[k], courses)
                # if capacity_show!= 0:
                    # print(f'capacity: ', schedule[i][j][k], capacity_show)

                malus = malus + capacity(schedule[i][j][k], rooms[k], courses)
                if overlapping(schedule[i][j][k], schedule[i][j], overlap_dict, k) == False:
                    # print(f'overlapping', schedule[i][j][k])
                    malus = malus + 800
                if order(schedule, schedule[i][j][k], i, j) == False:
                    # print(f'order', schedule[i][j][k])
                    malus = malus + 600


    print(f'points ditribution: ',distribution(schedule, courses))
    malus = malus + distribution(schedule, courses)

    return malus

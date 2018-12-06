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
                print(f"capacity", capacity(schedule[i][j][k], rooms[k], courses))
                malus = malus + capacity(schedule[i][j][k], rooms[k], courses)
                print(f"overlapping", overlapping(schedule[i][j][k], schedule[i][j], overlap_dict, k))
                if overlapping(schedule[i][j][k], schedule[i][j], overlap_dict, k) == False:
                    malus = malus + 800
                print(f"order", order(schedule, schedule[i][j][k], i, j))
                if order(schedule, schedule[i][j][k], i, j) == False:
                    malus = malus + 600

    # print(f"distribution", distribution(schedule,coureses))
    # malus = malus + distribution(schedule, courses)

    return malus

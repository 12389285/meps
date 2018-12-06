from code.constraints.capacity import capacity
from code.constraints.overlap_simulated import overlapping
from code.constraints.order import order
import time

def scorefunction2(schedule, courses, rooms, overlap_dict):

    malus = 0;

    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            for k in range(len(schedule[i][j])):
                if schedule[i][j][k] != None:
                    if j == 4:
                        malus = malus + 20
                dict[schedule[i][j][k]] = int(dict[schedule[i][j][k]]) + int(1)
                malus = malus + capacity(schedule[i][j][k], rooms[k], courses)
                if overlapping(schedule[i][j][k], schedule[i][j], overlap_dict) == False:
                    malus = malus + 800
                if order(schedule, schedule[i][j][k], i, j) == False:
                    malus = malus + 600

    return malus

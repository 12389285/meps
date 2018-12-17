from code.constraints.capacity import capacity
from code.constraints.overlap_simulated import overlapping
from code.constraints.order import order
import time
from code.constraints.distribution import distribution

def scorefunction_deterministic(schedule, courses, rooms, overlap_dict):
    """
    this scorefunction calculates the malus points for a schedule,
    where the hard constraints are not necessarily satisfied
    """

    malus = 0;

    # loop over days
    for i in range(len(schedule)):
        # loop over timelocksin day
        for j in range(len(schedule[i])):
            # loop over roomlock in timelock
            for k in range(len(schedule[i][j])):
                # only malus points can be calculated if roomlock is not zero
                if schedule[i][j][k] != None:
                    # 20 malus points are calculated if roomlock is the last (17-19h)
                    if j == 4:
                        malus = malus + 20
                # add maluspoints for not enough capacity in the rooms
                malus = malus + capacity(schedule[i][j][k], rooms[k], courses)
                # check if there is a overlapping part subject in same timelock
                if overlapping(schedule[i][j][k], schedule[i][j], overlap_dict, k) == False:
                    # if so, add 800 maluspoints
                    malus = malus + 800
                # check if order of the activities of subject is ok
                if order(schedule, schedule[i][j][k], i, j) == False:
                    # if not, add 600 maluspoints
                    malus = malus + 600

    malus = malus + distribution(schedule, courses)

    return malus

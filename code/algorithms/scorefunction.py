from code.constraints.capacity import capacity
from code.constraints.distribution import distribution

def scorefunction(schedule, rooms, courses):
    """
    this scorefunction calculates the malus points for a schedule,
    where the hard constraints are satisfied
    """

    # check if queue is not empy
    malus = 0

    # loop over days
    for i in range(len(schedule)):
        # loop over timlocks in day
        for j in range(len(schedule[i])):
            # loop over roomlocks in timelock
            for k in range(len(schedule[i][j])):
                # only malus points can be calculated if roomlock is not zero
                if schedule[i][j][k] is not None:
                    # add maluspoints for not enough capacity in the rooms
                    malus = malus + capacity(schedule[i][j][k], rooms[k], courses)
                    # 20 malus points are calculated if roomlock is the last (17-19h)
                    if j == 4:
                        malus = malus + 20;
                else:
                    continue

    malus = malus + distribution(schedule, courses)

    return malus

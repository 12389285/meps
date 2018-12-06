from code.constraints.capacity import capacity
from code.constraints.distribution import distribution

def scorefunction(schedule, rooms, courses):
    i = 0
    # check if queue is not empy
    malus = 0

    # select day i
    for i in range(len(schedule)):
        # select timelock j
        for j in range(len(schedule[i])):
            # select room lock k
            for k in range(len(schedule[i][j])):
                if schedule[i][j][k] is not None:
                    malus = malus + capacity(schedule[i][j][k], rooms[k], courses)
                    if j == 4:
                        malus = malus + 20;
                else:
                    continue

    # malus = malus + distribution(schedule, courses)

    return malus

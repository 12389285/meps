#
#   Algorithm for create schedule by queue
#
from code.constraints.overlap import overlapping
from code.constraints.capacity import capacity
from code.constraints.queue import alphabetic_queue
from code.constraints.queue import lecfirst_queue
from code.constraints.queue import length_queue
from code.constraints.queue import random_queue
from code.constraints.queue import lecfirst_random_queue
from code.constraints.order import order
from .scorefunction import scorefunction

def create_start_schedule(courses, schedule, rooms, overlap_dict):

    queue = lecfirst_random_queue(courses)

    i = 0
    # check if queue is not empy
    malus = 0

    while queue != []:
            # select day i
            for i in range(len(schedule)):
                # select timelock j
                for j in range(len(schedule[i])):
                    # select room lock k
                    for k in range(len(schedule[i][j])):
                        if schedule[i][j][k] is None:
                            for l in range(len(queue)):
                                if overlapping(queue[l],schedule[i][j], overlap_dict):
                                    if order(schedule, queue[l], i, j):
                                        schedule[i][j][k] = queue[l]
                                        queue.remove(queue[l])
                                        break
                                    else:
                                        continue
                                else:
                                    continue

    print(scorefunction(schedule, rooms, courses))
    print(schedule)
    return(schedule)

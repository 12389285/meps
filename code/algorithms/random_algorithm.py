from code.constraints.overlap import overlapping
from code.constraints.capacity import capacity

def list(list, schedule, rooms, overlap_dict):
    # create a queue
    activities_queue = []

    for course in list:
        for i in range(len(course.activities)):
            print(course.activities[i])
            activities_queue.append(course.activities[i])

    return(create_schedule(activities_queue, schedule, rooms, overlap_dict, list))

def create_schedule(activities_queue, schedule, rooms, overlap_dict, list):
    i = 0
    # check if queue is not empy
    while activities_queue != []:
            # select day i
            for i in range(len(schedule)):
                # select timelock j
                for j in range(len(schedule[i])):
                    # select room lock k
                    for k in range(len(schedule[i][j])):
                        if schedule[i][j][k] is None:
                            for l in range(len(activities_queue)):
                                if overlapping(activities_queue[l],schedule[i][j], overlap_dict) == True:
                                    if capacity(activities_queue[l], rooms[k], list):
                                        schedule[i][j][k] = activities_queue[l]
                                        activities_queue.remove(activities_queue[l])
                                        break
                                    else:
                                        continue
                                else:
                                    continue

    print(schedule)
    return(schedule)

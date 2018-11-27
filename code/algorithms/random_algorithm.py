def list(list, schedule, dict):
    # create a queue
    act_5 = []
    act_4 = []
    act_3 = []
    act_2 = []
    act_1 = []
    activities_queue = []
    for course in list:
        if len(course.activities) == 5:
            for activity in course.activities:
                act_5.append(activity)
        elif len(course.activities) == 4:
            for activity in course.activities:
                act_4.append(activity)
        elif len(course.activities) == 3:
            for activity in course.activities:
                act_3.append(activity)
        elif len(course.activities) == 2:
            for activity in course.activities:
                act_2.append(activity)
        elif len(course.activities) == 1:
            for activity in course.activities:
                act_1.append(activity)


    for activity in act_5:
        activities_queue.append(activity)
    for activity in act_4:
        activities_queue.append(activity)
    for activity in act_3:
        activities_queue.append(activity)
    for activity in act_2:
        activities_queue.append(activity)
    for activity in act_1:
        activities_queue.append(activity)
    return(create_schedule(activities_queue, schedule, dict))

def create_schedule(activities_queue, schedule, dict):
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
                                # not same course at time lock
                                if activities_queue[l] not in schedule[i][j]:
                                    # not overlapping course at time_lock, loop through time lock courses
                                    for m in range(len(dict[activities_queue[l]])):
                                        if dict[activities_queue[l]][m] not in schedule[i][j]:
                                            if m == (len(dict[activities_queue[l]]) - 1):
                                                schedule[i][j][k] = activities_queue[l]
                                                activities_queue.remove(activities_queue[l])
                                                break

                                        else:
                                            break
                                    if schedule[i][j][k] is not None:
                                        break
                                else:
                                    continue


    print(schedule)

    return(schedule)

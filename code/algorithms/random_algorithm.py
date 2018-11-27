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
<<<<<<< HEAD
            act_1.append(', '.join(str(act) for act in course.activities))

    activities_queue.append(', '.join(str(act) for act in act_5))
    activities_queue.append(', '.join(str(act) for act in act_4))
    activities_queue.append(', '.join(str(act) for act in act_3))
    activities_queue.append(', '.join(str(act) for act in act_2))
    activities_queue.append(', '.join(str(act) for act in act_1))

    # create_schedule(activities_queue)

    return activities_queue

# def create_schedule(activities_queue):
#
#     i = 0
#
#     for day in week:
#         for time_lock in day:
#             for j in range(len(time_lock)):
#                 if time_lock[j] == None:
#                     time_lock[j] = queue[i]
#                     i = i + 1
#                     if i > len(queue) -1 :
#                         break
=======
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
                                                print(schedule)
                                                break
                                        else:
                                            break
                                else:
                                    continue



    print(schedule)

    return(schedule)
>>>>>>> 6d2f38758f6a81bb042b4d6809e81ef1286e23ad

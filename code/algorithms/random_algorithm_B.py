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
                act_5.append(course)
        elif len(course.activities) == 4:
                act_4.append(course)
        elif len(course.activities) == 3:
                act_3.append(course)
        elif len(course.activities) == 2:
                act_2.append(course)
        elif len(course.activities) == 1:
                act_1.append(course)

    for course in act_5:
        activities_queue.append(course)
    for course in act_4:
        activities_queue.append(course)
    for course in act_3:
        activities_queue.append(course)
    for course in act_2:
        activities_queue.append(course)
    for course in act_1:
        activities_queue.append(course)

    for course in activities_queue:
        print(course.course_name ,  len(course.activities))

    return(create_schedule(activities_queue, schedule, dict))

def create_schedule(activities_queue, schedule, dict):

    # go through every course in list
    for l in range(len(activities_queue)):
        # check length of course
        if len(activities_queue[l].activities) == 5:
            # go through every activity of course
            for i in range(5):
                # select time slot of day
                for j in range(len(schedule[i])):
                    # select room lock
                    for k in range(len(schedule[i][j])):
                        # check if room lock is empty
                        if schedule[i][j][k] is None:
                            # not overlapping course at time_lock, loop through time lock courses
                            for m in range(len(dict[activities_queue[l].activities[i]])):
                                    if dict[activities_queue[l].activities[i]][m] not in schedule[i][j]:
                                        if m == (len(dict[activities_queue[l].activities[i]]) - 1):
                                            schedule[i][j][k] = activities_queue[l].activities[i]
                                            break # out of m
                                    else:
                                        break # out of m
                            if schedule[i][j][k] is not None:
                                break # out of k
                        else:
                            continue
                    break

        elif len(activities_queue[l].activities) == 4:
            # go through every activity of course
            for i in range(4):
                # select time slot of day
                for j in range(len(schedule[i])):
                    # select room lock
                    for k in range(len(schedule[i][j])):
                        # check if room lock is empty
                        if schedule[i][j][k] is None:
                            # not overlapping course at time_lock, loop through time lock courses
                            for m in range(len(dict[activities_queue[l].activities[i]])):
                                    if dict[activities_queue[l].activities[i]][m] not in schedule[i][j]:
                                        if m == (len(dict[activities_queue[l].activities[i]]) - 1):
                                            schedule[i][j][k] = activities_queue[l].activities[i]
                                            break # out of m
                                    else:
                                        break # out of m
                            if schedule[i][j][k] is not None:
                                break # out of k
                        else:
                                continue
                    break

        elif len(activities_queue[l].activities) == 3:
            # go through every activity of course
            for i in range(3):
                d = i * 2
                # select time slot of day
                for j in range(len(schedule[d])):
                    # select room lock
                    for k in range(len(schedule[d][j])):
                        # check if room lock is empty
                        if schedule[d][j][k] is None:
                            # not overlapping course at time_lock, loop through time lock courses
                            for m in range(len(dict[activities_queue[l].activities[i]])):
                                    if dict[activities_queue[l].activities[i]][m] not in schedule[d][j]:
                                        if m == (len(dict[activities_queue[l].activities[i]]) - 1):
                                            schedule[d][j][k] = activities_queue[l].activities[i]
                                            break # out of m
                                    else:
                                        break # out of m
                            if schedule[d][j][k] is not None:
                                break # out of k
                        else:
                            continue
                    if None in schedule[d][j] or schedule[d][j][k] == activities_queue[l].activities[i]:
                        break

                    else:
                        continue

        elif len(activities_queue[l].activities) == 2:
            # go through every activity of course
            for i in range(2):
                d = i * 2 + 1
                # select time slot of day
                for j in range(len(schedule[d])):
                    # select room lock
                    for k in range(len(schedule[d][j])):
                        # check if room lock is empty
                        if schedule[d][j][k] is None:
                            # not overlapping course at time_lock, loop through time lock courses
                            for m in range(len(dict[activities_queue[l].activities[i]])):
                                    if dict[activities_queue[l].activities[i]][m] not in schedule[d][j]:
                                        if m == (len(dict[activities_queue[l].activities[i]]) - 1):
                                            schedule[d][j][k] = activities_queue[l].activities[i]
                                            break # out of m
                                    else:
                                        break # out of m
                            if schedule[d][j][k] is not None:
                                break # out of k
                        else:
                            continue
                    if None in schedule[d][j] or schedule[d][j][k] == activities_queue[l].activities[i]:
                        break

                    else:
                        continue

        elif len(activities_queue[l].activities) == 1:
            # go through every activity of course
            for i in range(len(schedule)):
                # select time slot of day
                for j in range(len(schedule[i])):
                    # select room lock
                    for k in range(len(schedule[i][j])):
                        # check if room lock is empty
                        if schedule[i][j][k] is None:
                            # not overlapping course at time_lock, loop through time lock courses
                            for m in range(len(dict[activities_queue[l].activities[0]])):
                                    if dict[activities_queue[l].activities[0]][m] not in schedule[i][j]:
                                        if m == (len(dict[activities_queue[l].activities[0]]) - 1):
                                            schedule[i][j][k] = activities_queue[l].activities[0]
                                            break # out of m
                                    else:
                                        break # out of m

                            if schedule[i][j][k] is not None:
                                break # out of k

                        else:
                            continue

                    if None in schedule[i][j] or schedule[i][j][k] == activities_queue[l].activities[0]:
                        break

                    else:
                        continue
                break


    print(schedule)

    return(schedule)

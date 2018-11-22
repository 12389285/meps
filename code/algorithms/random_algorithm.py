def list(list, schedule):
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
    return(create_schedule(activities_queue, schedule))

def create_schedule(activities_queue, schedule):

    i = 0

    for day in schedule:
        for time_lock in day:
            for i in range(len(time_lock)):
                if activities_queue != []:
                    time_lock[i] = activities_queue[0]
                    activities_queue.remove(activities_queue[0])


    print(schedule[1][2][4])

    return(schedule)

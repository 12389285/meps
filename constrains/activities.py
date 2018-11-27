# function returns list of activities



def activities_list(list, schedule, dict):

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

    return activities_queue

def random(list):
    # create a queue
    act_5 = []
    act_4 = []
    act_3 = []
    act_2 = []
    act_1 = []
    activities_queue = []
    for course in list:
        if len(course.activities) == 5:
            act_5.append(', '.join(str(act) for act in course.activities))
        elif len(course.activities) == 4:
            act_4.append(', '.join(str(act) for act in course.activities))
        elif len(course.activities) == 3:
            act_3.append(', '.join(str(act) for act in course.activities))
        elif len(course.activities) == 2:
            act_2.append(', '.join(str(act) for act in course.activities))
        elif len(course.activities) == 1:
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

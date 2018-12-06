
def overlapping(activity, timelock, overlap_dict, roomlock):
    if activity == None:
        return True
    else:
        activity = activity.split('_')
        for i in range(len(timelock)):
            activity_timelock = timelock[i]
            if activity_timelock != None:
                if i == roomlock:
                    continue

                activity_timelock = timelock[i].split('_')
                activity_timelock = activity_timelock[0]
            if activity_timelock in overlap_dict[activity[0]]:
                if activity_timelock != activity[0]:
                    return False
    return True

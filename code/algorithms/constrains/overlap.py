def overlapping(activity, timelock, dict):
    activity = activity.split('_')
    for i in range(len(timelock)):
        activity_timelock = timelock[i]
        if activity_timelock != None:
            activity_timelock = timelock[i].split('_')
            activity_timelock = activity_timelock[0]
        if activity_timelock in dict[activity[0]]:
            return False
    return True

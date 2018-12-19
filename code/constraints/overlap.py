def overlapping(activity, timelock, overlap_dict):
    """
    This function returns True if the is no overlap with courses given in the
    overlap matrix. Otherwise, it returns False.

    This function takes as input arguments:
        - activity
        - time lock and room lock
        - overlap matrix
    """

    # if None it is always true
    if activity == None:
        return True

    else:
        # # check if two lectures are given in timelock
        # if '_lec' in activity:
        #     if activity in timelock:
        #         return False

        # check if no other overlap-course is given in the same time lock
        activity = activity.split('_')
        for i in range(len(timelock)):
            activity_timelock = timelock[i]
            if activity_timelock != None:
                activity_timelock = timelock[i].split('_')
                activity_timelock = activity_timelock[0]
            if activity_timelock in overlap_dict[activity[0]]:
                return False
    return True

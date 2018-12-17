def order(schedule, activity, daylock, timelock):
    """
    This function returns True if the lectures are given before the tutorials
    and/or practica when activity is switched to day en timelock.
    Otherwise, it returns False.

    This function takes as input arguments:
        - the schedule
        - the activity
        - the exact day lock and time lock

    This function works as follows:
        - if activity is a practica or tutorial: it checks if a lecture is
          given in a timelock after it
        - if activity is lecture: it checks if tutorial or practicum is given
          in an earlier time lock
    """

    # if None, it can always be switched
    if activity == None:
        return True

    else:
        # split to see what kind of activity it is
        course, sort = activity.split("_")

        if 'tut' in sort or 'prac' in sort:
        # search for lecture after new tut/prac porition

            str = course + '_lec'

            for i in range(timelock + 1, 5):
                if str in schedule[daylock][i]:
                    return False

            for j in range(daylock + 1, 5):
                for k in range(0, 5):
                    if str in schedule[j][k]:
                        return False

        elif 'lec' in sort:
        # search for tut or prac before new lecture position

            str1 = course + '_prac'
            str2 = course + '_tut'


            for i in range(0, timelock):
                if str1 in schedule[daylock][i]:
                    return False
                elif str2 in schedule[daylock][i]:
                    return False

            for j in range(0, daylock):
                for k in range(0, 5):
                    if str1 in schedule[j][k]:
                        return False
                    elif str2 in schedule[j][k]:
                        return False

        return True

#
# Checks if the lectures are first
#

def order(schedule, activity, daylock, timelock, queue):

    if activity == None:
        return True

    else:
        course, sort = activity.split("_")

        if 'tut' in sort or 'prac' in sort:

            str = course + '_lec'

            if str not in queue:
                return True

            else:

                for i in range(timelock + 1, 5):
                    if str in schedule[daylock][i]:
                        return False

                for j in range(daylock + 1, 5):
                    for k in range(0, 5):
                        if str in schedule[j][k]:
                            return False

        elif 'lec' in sort:

            str1 = course + '_prac'
            str2 = course + '_tut'

            if str1 not in queue and str2 not in queue:
                return True

            else:
                
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

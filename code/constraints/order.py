#
# Checks if the lectures are first
#

def order(schedule, activity, daylock, timelock):
<<<<<<< HEAD

    print(daylock)
    print(timelock)

=======
>>>>>>> fee251c3d515878a686971146a5690b666425ad5
    if activity == None:
        return True

    else:
        course, sort = activity.split("_")

        if 'tut' in sort or 'prac' in sort:

            str = course + '_lec'

            for i in range(timelock + 1, 5):
                if str in schedule[daylock][i]:
                    print('lec found!')
                    return False

            for j in range(daylock + 1, 5):
                for k in range(0, 5):
                    if str in schedule[j][k]:
                        print('lec found!')
                        return False

        elif 'lec' in sort:

            str1 = course + '_prac'
            str2 = course + '_tut'

            for i in range(0, timelock):
                if str1 in schedule[daylock][i]:
                    print('prac/tut found!')
                    return False
                elif str2 in schedule[daylock][i]:
                    print('prac/tut found!')
                    return False

            for j in range(0, daylock):
                for k in range(0, 5):
                    if str1 in schedule[j][k]:
                        print('prac/tut found!')
                        return False
                    elif str2 in schedule[j][k]:
                        print('prac/tut found!')
                        return False

        return True

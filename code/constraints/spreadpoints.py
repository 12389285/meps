#
#  Returns the malus or bonus points regarding the spread of the course
#  activities over the week
#

def spread_malus(number_activities, diff_days):
    # returns the malus points if not enough spread

    malus = 0

    if len(diff_days) == number_activities - 1:
            malus = malus + 10
    elif len(diff_days) == number_activities - 2:
            malus = malus + 20
    elif len(diff_days) == number_activities - 3:
            malus = malus + 30

    return malus

def spread_bonus(number_activities, diff_days):
    # returns the bonus points if spread perfectly

    malus = 0

    if number_activities == 2:
        if diff_days == [0, 3] or diff_days == [1, 4]:
            malus = malus - 20
    if number_activities == 3:
        if diff_days == [0, 2, 4]:
            malus = malus - 20
    if number_activities == 4:
        if diff_days == [0, 1, 3, 4]:
            malus = malus - 20


    return malus

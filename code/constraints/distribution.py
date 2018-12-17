#
#   Calculates and returns the malus points caused by spreading activities over the week
#


from .couple import couples
from .spreadpoints import spread_malus
from .spreadpoints import spread_bonus

def distribution(schedule, courses):

    # make variable to count malus points
    malus = 0

    # make lists to see on what day the different activities are scheduled
    for i in range(len(courses)):
        name = courses[i].name
        number_activities = courses[i].dif_total
        day_lec_1 = None
        day_lec_2 = None
        day_tut = []
        day_pr = []
        total_days = []
        total_lecs = []
        double_lec = 0
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                for k in range(len(schedule[i][j])):
                    if schedule[i][j][k] != None:
                        course, sort = str(schedule[i][j][k]).split("_")
                        if course == name:
                            if 'lec' in sort:
                                if day_lec_1 == None:
                                    day_lec_1 = i
                                    total_lecs.append(i)
                                    total_days.append(i)
                                else:
                                    day_lec_2 = i
                                    if day_lec_2 != day_lec_1:
                                        total_lecs.append(i)
                                        total_days.append(i)
                                    else:
                                        double_lec = 1
                            elif 'tut' in sort:
                                day_tut.append(i)
                            elif 'pr' in sort:
                                day_pr.append(i)

        # set variable to count double days that cost points
        double = 0

        # in case there are both practica and tutorials
        if day_pr and day_tut:
            points = couples(day_tut, day_pr, total_days, number_activities)
            malus = malus + points

        # in case there are only tutorials and no practica
        elif day_tut and not day_pr:
            # if the lectures are on te same day it costs points
            if double_lec == 1:
                malus = malus + 10
            # count malus points
            for i in range(len(day_tut)):
                total_days.append(day_tut[i])
                if day_tut[i] in total_lecs:
                    double = double + 1
            double_frac = double / len(day_tut)
            malus = malus + double_frac * 10
            # count bonus points
            bonus = 0
            for i in range(len(day_tut)):
                all_days = []
                all_days.extend(total_lecs)
                all_days.append(day_tut[i])
                bonus = bonus + spread_bonus(number_activities, all_days)
            malus = malus + bonus

        # in case there are only practica and no tutorials
        elif day_pr and not day_tut:
            # if the lectures are on te same day it costs points
            if double_lec == 1:
                malus = malus + 10
            day_pr = list(set(day_pr))
            for i in range(len(day_pr)):
                total_days.append(day_pr[i])
                if day_pr[i] in total_lecs:
                    double = double + 1
            double_frac = double / len(day_pr)
            malus = malus + double_frac * 10
            # count bonus points
            bonus = 0
            for i in range(len(day_pr)):
                all_days = []
                all_days.extend(total_lecs)
                all_days.append(day_pr[i])
                bonus = bonus + spread_bonus(number_activities, all_days)
            malus = malus + bonus

    return malus

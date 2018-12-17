from itertools import permutations, repeat
import numpy

def distribution(schedule, courses):
    """
    This function calculates the malus points regarding the spread of course
    activities over the week.

    This function takes as input arguments:
        - the schedule
        - list of courses

    This function works as follows:
        - makes lists with days on which lectures, tutorials and practica
          are given
        - calculates bonus and malus points regarding the best spread
          combinations of tutorials, lectures and practica
    """

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
                                    # add to lecture and total list
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
                                # add to tutorial days list
                                day_tut.append(i)
                            elif 'pr' in sort:
                                # add to practica days list
                                day_pr.append(i)

        # in case there are both practica and tutorials
        if day_pr and day_tut:
            malus = tut_and_prac(day_tut, day_pr, total_days, number_activities)

        # in case there are only tutorials and no practica
        elif day_tut and not day_pr:
            malus = only_tut(day_tut, total_days, total_lecs, double_lec, number_activities)

        # in case there are only practica and no tutorials
        elif day_pr and not day_tut:
            malus = only_prac(day_pr, total_days, total_lecs, double_lec, number_activities)

    return malus

def tut_and_prac(tut, prac, total_days, number_activities):
    """
    This function calculates bonus and malus points regarding the best spread
    combinations of tutorials, lectures and practica.
    """

    # set variables and lists
    malus = 0
    comb_doubles = []
    best_comb = []
    combinations = list(list(zip(r, p)) for (r, p) in zip(repeat(tut), permutations(prac)))

    # calculate combination list without prac and tut on the same day
    for i in range(len(combinations)):
        double = 0
        for j in range(len(combinations[i])):
            num = str(combinations[i][j])
            num1, num2 = num.split(',')
            num1 = num1.replace('(', '')
            if num1 in num2:
                double = double + 1
        comb_doubles.append(double)
    best = numpy.min(comb_doubles)
    best_index =  [i for i,x in enumerate(comb_doubles) if x == best]
    for i in range(len(best_index)):
        ind = best_index[i]
        best_comb.append(combinations[ind])

    # for these combinations, calculate the malus points
    tot = []
    points_list = []
    for i in range(len(best_comb)):
        points_tot = 0
        for j in range(len(best_comb[i])):
            tot = []
            tot.extend(total_days)
            tot.extend(best_comb[i][j])
            tot = list(set(tot))
            points_m = spread_malus(number_activities, tot)
            points_b = spread_bonus(number_activities, tot)
            points_tot = points_tot + (points_m + points_b) / len(best_comb[i])
        points_list.append(points_tot)

    # choose the option with the smallest amount malus points, and calculate points
    best_points = numpy.min(points_list)
    best_points_index = numpy.argmin(points_list)
    couples = best_comb[best_points_index]
    malus = best_points

    return(malus)

def only_tut(day_tut, total_days, total_lecs, double_lec, number_activities):
    """
    This function calculates bonus and malus points regarding the best spread
    combinations of tutorials and lectures.
    """

    malus = 0
    double = 0

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

    # count bonus points for perfectly spread activities
    bonus = 0
    for i in range(len(day_tut)):
        all_days = []
        all_days.extend(total_lecs)
        all_days.append(day_tut[i])
        bonus = bonus + spread_bonus(number_activities, all_days)
    malus = malus + bonus

    return(malus)

def only_prac(day_pr, total_days, total_lecs, double_lec, number_activities):
    """
    This function calculates bonus and malus points regarding the best spread
    combinations of lectures and practica.
    """

    malus = 0
    double = 0

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

    # count bonus points for perfectly spread activities
    bonus = 0
    for i in range(len(day_pr)):
        all_days = []
        all_days.extend(total_lecs)
        all_days.append(day_pr[i])
        bonus = bonus + spread_bonus(number_activities, all_days)
    malus = malus + bonus

    return(malus)

def spread_malus(number_activities, diff_days):
    """
    This function returns malus points if activities are not spread well
    enough.
    """

    malus = 0

    if len(diff_days) == number_activities - 1:
            malus = malus + 10
    elif len(diff_days) == number_activities - 2:
            malus = malus + 20
    elif len(diff_days) == number_activities - 3:
            malus = malus + 30

    return malus

def spread_bonus(number_activities, diff_days):
    """
    This function returns bonus points if activities are perfectly spread.
    """

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

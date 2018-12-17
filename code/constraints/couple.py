#
# Returns malus points concidering best possible combinations of days
#

from itertools import permutations, repeat
from .spreadpoints import spread_malus
from .spreadpoints import spread_bonus
import numpy

def couples(tut, prac, total_days, number_activities):

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
            print(tot)
            points_m = spread_malus(number_activities, tot)
            points_b = spread_bonus(number_activities, tot)
            points_tot = points_tot + (points_m + points_b) / len(best_comb[i])
        points_list.append(points_tot)

    # choose the option with the smallest amount malus points, and calculate points
    best_points = numpy.min(points_list)
    best_points_index = numpy.argmin(points_list)
    couples = best_comb[best_points_index]

    return(malus)

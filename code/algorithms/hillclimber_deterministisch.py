import random
import copy
import time
import math
from code.constraints.queue import alphabetic_queue
from code.algorithms.scorefunction2 import scorefunction2
from code.algorithms.scorefunction_show import scorefunction_show
import matplotlib.pyplot as plt

def hillclimber_determin(courses, schedule, rooms, overlap_dict):

    score_plt = []
    loops_list = []
    loops = 0
    course_list_alphabetic = alphabetic_queue(courses)
    # print(course_list_alphabetic)

    # fill the schedule in random, (don't take hard constraints into account)
    # loop over the days
    for i in range(len(schedule)):
        #loop over the timelocks in day
        for j in range(len(schedule[i])):
            # loop over the roomlocks in timelock
            for k in range(len(schedule[i][j])):
                # while list of alphabetical courses is not empty
                if course_list_alphabetic != []:
                    # determine lenght of alphabetical list
                    length = len(course_list_alphabetic)
                    # find random course index in alphabetical list
                    list_place = random.randint(0, (length - 1))
                    # fill the schedule timelock with the random course
                    schedule[i][j][k] = course_list_alphabetic[list_place]
                    # remove filled course from alphabetical list
                    course_list_alphabetic.remove(course_list_alphabetic[list_place])

    # determine score is maluspoints of the random filled in schedule, (hard constraints are not satisfied, so given a lot of malus points to)
    score = scorefunction2(schedule, courses, rooms, overlap_dict)
    # make a copy of the random schedule
    schedule_save = copy.deepcopy(schedule)


    # start hillclimber
    # determine how many times the bigloop is runned
    for bigloop in range(4):
        # loop over days in schedule
        for i in range(len(schedule)):
            # loop over timelock in days
            for j in range(len(schedule[i])):
                # loop over roomlocks in timelock
                for k in range(len(schedule[i][j])):
                    # make a list of scores
                    list_scores = []
                    # make variable new and set to 0
                    new = 0
                    # make lists to save schedule place
                    array_daylock = []
                    array_timelock = []
                    array_roomlock = []

                    # for the current roomlock in schedule, swap with every other roomlock
                    # in the schedule and calculate score (add tot list_scores)

                    # loop over days in schedule
                    for a in range(len(schedule)):
                        # loop over timelocks in day
                        for b in range(len(schedule[a])):
                            # loop over roomlocks in timelock
                            for c in range(len(schedule[a][b])):
                                # make a copy of the current schedule
                                schedule_copy = copy.deepcopy(schedule)
                                # swap roomlock of head schedule (i,j,k) with roomlock schedule (a,b,c)
                                schedule_copy[i][j][k] = schedule[a][b][c]
                                schedule_copy[a][b][c] = schedule[i][j][k]
                                # caluclate score of swapped schedule
                                score = scorefunction2(schedule_copy, courses, rooms, overlap_dict)
                                # append score to list scores
                                list_scores.append(score)
                                # save inex of day, timelock and roomlock in the lists
                                array_daylock.append(a)
                                array_timelock.append(b)
                                array_roomlock.append(c)
                    # determine minimum score in list
                    min_score = min(list_scores)
                    # if minimum_score is lower than score that schedule already has
                    if min_score < score:
                        # find index of minimum_score in list
                        for z in range(len(list_scores)):
                            if list_scores[z] == min_score:
                                # new is index of minimum score
                                new = z
                                break
                        # new score is the minimum score
                        score = min_score
                        # find daylock, timelock and roomlock of minimum_score
                        a = array_daylock[new]
                        b = array_timelock[new]
                        c = array_roomlock[new]
                        # swap the roomlocks with each other
                        temporary = schedule[i][j][k]
                        schedule[i][j][k] = schedule[a][b][c]
                        schedule[a][b][c] = temporary
                        # print so user knows what's going on
                        print(bigloop)
                        print(f"score: ", score )

                        # needed for the plot
                        score_plt.append(score)
                        loops = loops + 1
                        loops_list.append(loops)

    # in the end, know where the malus points come from if you run this function
    scorefunction_show(schedule, courses, rooms, overlap_dict)

    plt.plot(loops_list, score_plt)
    plt.axis([0, max(loops_list), 0, max(score_plt) + 50])
    plt.text(max(loops_list) + 1, min(score_plt), min(score_plt))
    plt.title('Hillclimber deterministisch')
    plt.xlabel('loops')
    plt.ylabel('Malus points')
    plt.show()
    # print(schedule)
    return schedule

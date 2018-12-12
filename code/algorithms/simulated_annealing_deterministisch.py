import random
import copy
import time
import math
from code.constraints.queue import alphabetic_queue
from code.algorithms.scorefunction2 import scorefunction2
import matplotlib.pyplot as plt

def simulated_annealing_deterministisch(courses, schedule, rooms, overlap_dict):

<<<<<<< HEAD
    # make a list of courses in alphabetical order
=======
    score_plt = []
    loops_list = []
    loops = 0

>>>>>>> c9de3e7801093ae8cb13bfd9f0670ad7053f8545
    course_list_alphabetic = alphabetic_queue(courses)
    print(course_list_alphabetic)

    # fill the schedule in random
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


    # determine malus is maluspoints of the random filled in schedule
    malus = scorefunction2(schedule, courses, rooms, overlap_dict)
    print(malus)
    # make a copy of the random schedule
    schedule_save = copy.deepcopy(schedule)
<<<<<<< HEAD
    # save the best score (it starts with the malus points of the random schedule)
    score_save = malus
    # determine temperature for simmulated annealing
    temp = 50

    # start simulated annealing
    # determine how many times the bigloop is runned
    for bigloop in range(3):
        # with every extra bigloop temperature drops with factor 0.75
        temp = temp * 0.5
        # loop over days in schedule
=======
    # print(schedule)
    score_save = 1000000
    temp = 20
    for bigloop in range(10):
        temp = temp * 0.75
>>>>>>> c9de3e7801093ae8cb13bfd9f0670ad7053f8545
        for i in range(len(schedule)):
            # loop over timelock in days
            for j in range(len(schedule[i])):
                # loop over roomlocks in timelock
                for k in range(len(schedule[i][j])):
                    # make a list of scores
                    list_scores = []
                    # set the e_score_sum, new and tmp to 0
                    e_score_sum = 0
                    new = 0
                    tmp2 = 0
                    # make lists to save schedule place
                    array_day = []
                    array_timelock = []
                    array_roomlock = []
                    # for the current roomlock in schedule, swap with every other roomlock
                    # in schedule and calculate score (add tot list_scores)
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
                                array_day.append(a)
                                array_timelock.append(b)
                                array_roomlock.append(c)
                    # find minimum score of the swaps
                    min_score = min(list_scores)
                    # make list for e_scores
                    e_scores = []

                    # loop over every score in list_scores
                    for z in range(len(list_scores)):
                        # lower every score with the minimum scores
                        list_scores[z] = list_scores[z] - min_score
                        # determine the tmp of every score
                        tmp = -list_scores[z]/temp
                        # if python can't take tmp> 100, so that's why this is implemented
                        if tmp > 100:
                            tmp=100
                        # calculate the e_score and add tot list e_scores and calculate sum e_score
                        e_score = math.exp(tmp)
                        e_scores.append(e_score)
                        e_score_sum = e_score_sum + e_score
                    # get probability from uniform distribution
                    probability = random.uniform(0,1)
                    p_sum = 0

                    # loop over every score in e_scores
                    for m in range(len(e_scores)):
                        # determine probability of choosing e_score
                        e_scores[m] = e_scores[m]/ e_score_sum
                        # add the e_scores to each other
                        p_sum = p_sum + e_scores[m]
                        # if total of scores added > probability, that e_score is the one chosen to be swapped with
                        # define index as new
                        if p_sum > probability:
                            new = m
                            break
                    #  find the day, roomlock and timelock of chosen swap e_score
                    a = array_day[new]
                    b = array_timelock[new]
                    c = array_roomlock[new]
                    # swap the roomlocks with each other
                    temporary = schedule[i][j][k]
                    schedule[i][j][k] = schedule[a][b][c]
                    schedule[a][b][c] = temporary
                    score_check = scorefunction2(schedule, courses, rooms, overlap_dict)
                    # if new score is lower than the best-saved-score
                    if score_check < score_save:
                        # save this score as score-save
                        score_save = score_check
                        # save this schedule in schedule_save
                        schedule_save = schedule
                    # print statements to make clear what's going on
                    print(bigloop)
                    print(f"scorecheck: ", score_check)
                    print(f"scoresave: ", score_save)
                    list_scores = []
<<<<<<< HEAD

=======
                    e_scores = []
                    score_plt.append(score_check)
                    loops = loops + 1
                    loops_list.append(loops)

    plt.plot(loops_list, score_plt)
    plt.axis([0, max(loops_list), 0, max(score_plt) + 50])
    plt.text(max(loops_list) + 1, min(score_plt), min(score_plt))
    plt.title('simulated annealing deterministisch')
    plt.xlabel('loops')
    plt.ylabel('Malus points')
    plt.show()
>>>>>>> c9de3e7801093ae8cb13bfd9f0670ad7053f8545

    return schedule_save

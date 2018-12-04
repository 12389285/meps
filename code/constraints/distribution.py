

def distribution(schedule, courses):

    malus = 0
    for i in range(len(courses)):
        name = courses[i].name
        number_activities = courses[i].dif_total
        day_lec_1 = None
        day_lec_2 = None
        day_tut = []
        day_pr = []
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                for k in range(len(schedule[i][j])):
                    course, sort = schedule[i][j][k].split("_")
                    if course == name:
                        if lec in sort:
                            if day_lec_1 == None:
                                day_lec_1 = i
                            else:
                                day_lec_2 = i
                        if tut in sort:
                            day_tut.append(i)
                        if pr in sort:
                            day_pr.append(i)

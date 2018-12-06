def distribution(schedule, courses):

    malus = 0

    for i in range(len(courses)):
        name = courses[i].name
        print(name)
        number_activities = courses[i].dif_total
        day_lec_1 = None
        day_lec_2 = None
        day_tut = []
        day_pr = []
        total_days = []
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                for k in range(len(schedule[i][j])):
                    if schedule[i][j][k] != None:
                        course, sort = str(schedule[i][j][k]).split("_")
                        if course == name:
                            if 'lec' in sort:
                                if day_lec_1 == None:
                                    day_lec_1 = i
                                    total_days.append(i)
                                else:
                                    day_lec_2 = i
                                    if day_lec_2 != day_lec_1:
                                        total_days.append(i)
                            elif 'tut' in sort:
                                day_tut.append(i)
                            elif 'pr' in sort:
                                day_pr.append(i)

        if day_tut:
            day_tut = list(set(day_tut))
            for i in range(len(day_tut)):
                total_days.append(day_tut[i])
        if day_pr:
            day_pr = list(set(day_pr))
            for i in range(len(day_pr)):
                total_days.append(day_pr[i])

        diff_days = list(set(total_days))

        print(diff_days)

        if len(diff_days) == number_activities - 1:
            malus = malus + 10
        elif len(diff_days) == number_activities - 2:
            malus = malus + 20
        elif len(diff_days) == number_activities - 3:
            malus = malus + 30

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

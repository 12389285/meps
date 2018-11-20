class Schedule(object):

    def __init__(self):
        self.empty_schedule = []

    def create(self):
        # create empty schedule
        time_locks = [None] * 5
        for i in range(4):
            time_locks[i] = [None] * 7
        time_locks[4] = [None]

        week = [None] * 5
        for i in range(5):
            week[i] = time_locks

        self.empty_schedule.append(week)

        return self.empty_schedule

    def __str__(self):
        return f"{self.empty_schedule}"

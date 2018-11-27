class Schedule(object):

    def __init__(self):
        self.empty_schedule = self.create()

    def create(self):
        # create empty schedule
        list = []
        for i in range(5):
            time_locks = [None] * 5
            for i in range(4):
                time_locks[i] = [None] * 7
            time_locks[4] = [None]
            list.append(time_locks)

        return list


    def __str__(self):
        return f"{self.empty_schedule}"

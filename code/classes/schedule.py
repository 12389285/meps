# Meps lectures
# Eefje Roelsema – 10993673
# Pascalle Veltman – 11025646
# Max Simons – 12389285
# Classifies a schedule.

class Schedule(object):

    def __init__(self):
        self.empty_schedule = self.create()

    def create(self):

        """
        This function creates an empty schedule. First it creates an empty list
        and fills the list with Nones. For every day it creates 5 time locks within
        the first 4, 7 roomslocks. In the last time lock there is only one room lock.
        """
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

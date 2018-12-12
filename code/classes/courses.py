# Meps lectures
# Eefje Roelsema – 10993673
# Pascalle Veltman – 11025646
# Max Simons – 12389285
# Classifies all courses.

class Courses(object):

    """
    In this class the courses are classified. The courses are divided in Lectures,
    Tutorials and Practials. Also the numbers of different courses are listed.
    """

    def __init__(self, name, lec, tut, prac, tut_tot, prac_tot, max_tut, max_prac, exp_stud, act_tot, dif_total):

        self.name = name
        self.lec = lec
        self.tut = tut
        self.prac = prac
        self.tut_tot = tut_tot
        self.prac_tot = prac_tot
        self.act_tot = act_tot
        self.max_tut = max_tut
        self.max_prac = max_prac
        self.exp_stud = exp_stud
        self.dif_total = dif_total
        self.activities = []

    def add(self, activity):
        """
        Add function to add the activities to a list.
        """
        self.activities.append(activity)

    def __str__(self):
        return f"{self.course_name}, {self.course_lec}, {self.course_tut}, {self.course_prac}, {self.activities} "

#
#   Classifies all courses.
#

class Courses(object):

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
        self.activities.append(activity)


    def __str__(self):
        return f"{self.course_name}, {self.course_lec}, {self.course_tut}, {self.course_prac}, {self.activities} "

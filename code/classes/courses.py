class Courses(object):

    def __init__(self, course_name, course_lec, course_tut, course_prac, course_tuttot, course_practot, course_maxtut, course_maxprac, course_expstud):

        self.course_name = course_name
        self.course_lec = course_lec
        self.course_tut = course_tut
        self.course_prac = course_prac
        self.course_tuttot = course_tuttot
        self.course_practot = course_practot
        self.course_maxtut = course_maxtut
        self.course_maxprac = course_maxprac
        self.course_expstud = course_expstud
        self.activities = []

    def add(self, activity):
        self.activities.append(activity)


    def __str__(self):
        return f"{self.course_name}, {self.course_lec}, {self.course_tut}, {self.course_prac}, {self.activities} "

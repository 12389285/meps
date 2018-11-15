class Courses(object):

    def __init__(self, course_name, course_lec, course_tut, course_prac):

        self.course_name = course_name
        self.course_lec = course_lec
        self.course_tut = course_tut
        self.course_prac = course_prac
        self.activities = []

    def add(self, activity):
        self.activities.append(activity)


    def __str__(self):
        return f"{self.course_name}, {self.course_lec}, {self.course_tut}, {self.course_prac}, {self.activities} "

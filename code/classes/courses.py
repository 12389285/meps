class Courses(object):

    def __init__(self, course_name, course_hc, course_wc, course_pr):

        self.course_name = course_name
        self.course_hc = course_hc
        self.course_wc = course_wc
        self.course_pr = course_pr


    def __str__(self):
        return f"{self.course_name}, {self.course_hc}, {self.course_wc}, {self.course_pr}"

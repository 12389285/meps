

class Vakken(object):

    def __init__(self, vak, vak_hc, vak_wc, vak_pr):

        self.vak = vak
        self.vak_hc = vak_hc
        self.vak_wc = vak_wc
        self.vak_pr = vak_pr


    def __str__(self):
        return f"{self.vak}, {self.vak_hc}, {self.vak_wc}, {self.vak_pr}"

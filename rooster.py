
import csv
from zalen import Zalen
from courses import Courses
from tijd import Tijden


INPUT_COURSES = "data.courses.csv"
INPUT_ZALEN = "zalen.csv"
INPUT_TIJDEN = "tijdslot.csv"
INPUT_OVERLAP = "overlapping.csv"

def open_zalen(INPUT_ZALEN):
    """
    Openen van de informatie van alle zaken. Returns een dictionary.
    """
    # open zalen
    with open(INPUT_ZALEN) as zalen:
        zaal_reader = csv.DictReader(zalen)
        # lijst met alle zalen
        zalen = []
        for row in zaal_reader:
            nummer = row['Zaalnummber']
            aantal = row['Max. capaciteit']
            zaal = Zalen(nummer, aantal)
            zalen.append(zaal)

        for i in range(len(zalen)):
        #     print(zalen[i].naam)
        #     print(zalen[i].capaciteit)
            print(zalen[i])

    return zalen

def open_courses(INPUT_COURSES):
    """
    Openen van de informatie van alle vakken.
    """

    # open Vakken
    with open(INPUT_COURSES) as courses:
        course_reader = csv.DictReader(courses)
        # lijst met alle vakken
        course_list = []
        for row in course_reader:
            course_name = row['Vakken voor periode 4']
            course_hc = row['#Hoorcolleges']
            course_wc = row['#Werkcolleges']
            course_pr = row['#Practica']
            course = Courses(course_name, course_hc, course_wc, course_pr)
            course_list.append(course)

        for i in range(len(course_list)):
            # print(vak_lijst[i].vak)
            # print(vak_lijst[i].vak_hc)
            # print(vak_lijst[i].vak_wc)
            # print(vak_lijst[i].vak_pr)
            print(course_list[i])

    return course_list


def open_overlapping(INPUT_OVERLAP):

    # open overlapping
    with open(INPUT_OVERLAP) as overlap:
        overlap_reader = csv.DictReader(overlap)

        # lijst met alle zalen
        data_dict = {}
        dubbelen = []

        for row in overlap_reader:
            vak = row['0']
            for i in row:
                if not row[i]:
                    continue
                elif row[i] != row['0']:
                    dubbelen.append(row[i])
            data_dict[vak] = dubbelen
            dubbelen = []

        print(data_dict)


    #     for i in range(len(zalen)):
    #     #     print(zalen[i].naam)
    #     #     print(zalen[i].capaciteit)
    #         print(zalen[i])
    #
    return data_dict

def main(INPUT_ZALEN, INPUT_VAKKEN, INPUT_OVERLAP):
    """

    """
    zalen = open_zalen(INPUT_ZALEN)

    vak_lijst = open_vakken(INPUT_VAKKEN)

    data_dict = open_overlapping(INPUT_OVERLAP)




if __name__ == "__main__":
    main(INPUT_ZALEN, INPUT_VAKKEN, INPUT_TIJDEN, INPUT_OVERLAP)

import csv

def csvconverter(schedule):

    """
    This function can convert the 3D list into a clear schedule in excel. The
    input is a 3D list based on one week. The schedule shows the courses per day
    and within the days there are 5 timelocks.
    """

    # add rooms
    headers = ["C0.110", "A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C1.112"]

    with open('results/schedule.csv', 'w', newline='') as fp:

        a = csv.writer(fp)

        # seperate by comma in excel sheet
        a.writerow(["sep=,"])

        # get data per day
        a.writerow(["Maandag"])
        a.writerow(headers)
        a.writerows(schedule[0])
        a.writerow("")

        a.writerow(["Dinsdag"])
        a.writerow(headers)
        a.writerows(schedule[1])
        a.writerow("")

        a.writerow(["Woensdag"])
        a.writerow(headers)
        a.writerows(schedule[2])
        a.writerow("")

        a.writerow(["Donderdag"])
        a.writerow(headers)
        a.writerows(schedule[3])
        a.writerow("")

        a.writerow(["Vrijdag"])
        a.writerow(headers)
        a.writerows(schedule[4])

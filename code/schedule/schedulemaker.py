import csv

def csvconverter(schedule):

    headers = ["C0.110", "A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C1.112"]

    time_locks = ["09:00-11:00", "11:00-13:00", "13:00-15:00", "15:00-17:00"]

    with open('rooster.csv', 'w', newline='') as fp:

        a = csv.writer(fp)
        a.writerow(["sep=,"])
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
        a.writerow("")

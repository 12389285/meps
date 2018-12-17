# Code

## Algorithms

In the folder algorithms you can find all the algorithms we have used to solve the case. Also the score functions to calculate the amount of points and to plot maker are stored in the folder.

* algorithm_deterministic.py
* algorithm.py
* plot.py
* scorefunction_deterministic.py
* scorefunction_show.py
* scorefunction.py
* start_schedule_algorithm.py

## Classes

In this folder you can find the classes to load all the data.

* courses.py
* room.py
* schedule.py

## Constraints

To check if the schedule is valid we have to take into account with the constraints.

* capacity.py: the maximum of every room
* distribution.py: for the distribution of the schedule
* order.py: to order the courses in lectures, tutorials and practicals
* overlap_simulated: overlapping of courses
* overlap.py: overlapping of courses

## Schedule

The algorithms return a 3D list. To get a better and a more clear view we have written a schedule maker. The schedule maker convert the 3D list into a CSV file which can be opened with Microsoft excel to use the schedule.

The schedule can be find in meps/results/schedule.csv

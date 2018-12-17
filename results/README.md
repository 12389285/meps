# Plots

## Hillclimber

* Number of iterations: 100.000
* Start schedule: All hard constraints are satisfied
* start malus point: 460
* Result: 88 malus points
* Run-time: quick

## Hillclimber deterministic

* Number of big loops: 10 (times through whole schedule)
* Start schedule: Completely random (no hard constraints are satisfied)
* Start malus point = 70.000
* Result: 20 malus points
* Run-time: medium slow

## Simulated annealing

* Temperature: 5
* Factor lowering temperature per 100 swaps: 0.75
* Start schedule: All hard constraints are satisfied
* Start malus point = 500
* Result: 10 malus point
* Run-time: slow

## Simulated annealing deterministic

* Temperature: 300
* number of big loops: 10 (times through whole schedulel)
* Factor lowering temperature per big loop: 0.75
* Start schedule: Completely random (no hard constraints are satisfied)
* Start malus point = 500
* Result: 243 malus points
* Run-time: medium slow

# State space:

To get an idea of the valid solutions our problem can solve, we calculated the state space for each section.

### Section A:

* The calculations are weekly based.
* 25 time locks (5 per day, where for the last lock only one room is available).
* per time lock 7 rooms.

Total: 145 rooms available per week.

there are 29 courses per week
Every course has different kind of activities:
 * Lecture
 * Tutorial
 * Practicum

Total of 72 activities per week.

The courses will be put in one for one in a room lock. A room lock can only used for one course.

If we go threw the room locks we start with 145 options and will decrease every time one by one: 145 * 144 * 143 ...

So our upperbound is:

145 - 72 = 73

145!/73! = 1.800e+146

### section B

To calculate the state space in section B it is important to use the amount of students the UvA is expecting per course. Some lectures, tutorials or practicals there applied more students than there is place in a room. In this case we have to schedule another room for the leftover students.

To take into account with the students we have a lot more activities compare to section A. We now have a total of 126 activities we have to schedule.

So our upperbound for section B is:

145 - 126 = 19

145!/19! = 6.615e+234

## Score function

To determine which schedule the best schedule is we have a score function.

* For every student who doesn't fit in the room --> 1 malus point
* For every time we use the 17:00 - 19:00 time lock --> 20 malus malus points
* If a course have 2-4 activities and the courses are distribute over a week --> 20 bonus points
* Distribution of x activities in a week --> 10-30 malus points

### section A

In the worst case:
* All students didn't got a place --> 1410 malus points
* Use of last time lock every day --> 100 malus points

Total of 1510 malus points

best case:
* All students got a place --> 0 malus points
* No use of last time lock --> 0 malus points

### section B

In the worst case:
* All students didn't got a place --> 1410 malus points
* Use of last time lock every day --> 100 malus points
* No bonus points
* Distribute x activities on the same day --> 410 malus points

Total of 1920 points

Best case:
* All students got a place --> 0 malus points
* No use of last time lock --> 0 malus points
* All courses with 2-4 activities distribute over a week --> 400 bonus points
* Distribution of x activities in a week --> 0 malus points

Total of -400 points

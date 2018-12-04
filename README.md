# Lectures & Lesroosters

## Description

Lecture schedules for students are very difficult to fill in because of the many constraints and variables they contain. In this problem we'll look into a small example of a schedule maker using 29 courses, 7 rooms and 600 students of the University of Amsterdam, location Science Park.

Within this problem we will look into and calculate the state space of our problem. When we calculated the state space we will implement algorithms to make the best schedule for the students.

## State space:

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

## Getting started

### Prerequisites

This code is written in Python version 3.7.0. The libraries/packages the user will need to run our code are written in requirements.txt, these packages are easily to install using pip. Execute the following instruction in your terminal

```
pip install -r requirements.txt
```

### Structure

In our Github we have different kind of folders. In the code folder you'll find al our codes including the algorithm and the constrains we used. Also all the classes and the converter to get the schedule are stored in the folder code.

In the data folder you'll find all the CSV files we imported for the data including the rooms, courses and overlapping.

### Testing

To run our code with the default settings (Hillclimber) execute the following instruction in your terminal:

```
python main.py
```

To see the schedule open in the main folder schedule.csv.

## Authors

* Eefje Roelsema (10993673)
* Pascalle Veltman ()
* Max Simons (12389285)

## Acknowledgments

* Bram van de Heuvel
* StackOverflow

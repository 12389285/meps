# Lectures & Lesroosters

## Description

Lecture schedules for students are very difficult to fill in because of the many constraints and variables they contain. In this problem we'll look into a small example of a schedule maker using 29 courses, 7 rooms and 600 students of the University of Amsterdam, location Science Park.

Within this problem we will look into and calculate the state space of our problem. When we calculated the state space we will implement algorithms to make the best schedule for the students.

## Getting started

### Prerequisites

This code is written in Python version 3.7.0. The libraries/packages the user will need to run our code are written in requirements.txt, these packages are easily to install using pip. Execute the following instruction in your terminal

```
pip install -r requirements.txt
```

### Structure

In our Github we have different kind of folders. In the code folder you'll find al our codes including the algorithm and the constrains we used. Also all the classes and the converter to get the schedule are stored in the folder code.

In the data folder you'll find all the CSV files we imported for the data including the rooms, courses and overlapping.

In the result folder you'll find the results of some testing and the state space and score function in the reader.

### Testing

To run our code with the default settings (Hillclimber) execute the following instruction in your terminal:

```
python main.py
```

To see the schedule open in the main folder schedule.csv.

## Authors

* Eefje Roelsema (10993673)
* Pascalle Veltman (11025646)
* Max Simons (12389285)

## Acknowledgments

* Bram van de Heuvel
* StackOverflow

# Lectures & Lesroosters

## Description

Lecture schedules for students are very difficult to fill in because of the many constraints and variables they contain. In this problem we'll look into a small example of a schedule maker using 29 courses, 7 rooms and 600 students of the University of Amsterdam, location Science Park.

Within this problem we will look into and calculate the state space of our problem. When we calculated the state space we will implement algorithms to make the best schedule for the students. To decide which schedule is better, we use a score function calculating the malus and bonus points.

For more information about the case please visit the following page:

```
http://heuristieken.nl/wiki/index.php?title=Lectures_%26_Lesroosters
```

## Getting started

### Prerequisites

This code is written in Python version 3.7.0. The libraries/packages the user will need to run our code are written in requirements.txt, these packages are easily to install using pip. Execute the following instruction in your terminal

```
pip install -r requirements.txt
```

### Structure

#### Code
In the code folder you'll find al our codes including the algorithms and the constraints we used. Also all the classes and the converter to get the schedule are stored in the folder code.

#### Data
In the data folder you'll find all the CSV files we imported for the data including the rooms, courses and overlapping of the courses.

#### Results
In the result folder you'll find the results of some testing, the state space and score function in the readme. The final schedule is also stored in this folder.

### Testing

To run our code with the settings of your choice, execute the following instruction in your terminal. We have set a range for iterations and number of swaps. The run time for the deterministic algorithms takes a lot longer than the hillclimber and simulated annealing.

Hillclimber:
```
python main.py hillclimber [1, inf]
```

Hillclimber deterministic:
```
python main.py hillclimber_deterministic [1, 20]
```

Simulated annealing:
```
python main.py simulated_annealing [1, inf]
```

Simulated annealing deterministic:
```
python main.py simulated_annealing_deterministic [1, 20]
```

### Results

The schedule is stored in the results folder with the name schedule.csv. Matplotlib is making a plot of the number of iterations and the amount of points given for the schedule.

## Authors

* Eefje Roelsema (10993673)
* Pascalle Veltman (11025646)
* Max Simons (12389285)

## Acknowledgments

* Bram van de Heuvel
* StackOverflow

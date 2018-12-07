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

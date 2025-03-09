# Hat Drawing Probability Experiment

## Overview
This project simulates a probability experiment involving drawing balls from a hat. The goal is to estimate the probability of drawing a specific combination of balls given a set of conditions.

## Features
- Create a `Hat` object containing balls of different colors.
- Draw a specified number of balls randomly from the hat.
- Run multiple experiments to estimate the probability of drawing a desired combination of balls.

## Implementation
### Hat Class
The `Hat` class represents a hat containing balls of different colors.

#### Initialization
```python
hat = Hat(red=4, blue=2, green=6)
```
- The `Hat` object is initialized with keyword arguments representing different ball colors and their respective quantities.
- The balls are stored in a list, allowing random selection during drawing.

#### Drawing Balls
```python
drawn_balls = hat.draw(3)
```
- The `draw` method removes a specified number of balls from the hat at random.
- If the requested number of balls exceeds the total available, all remaining balls are drawn.

### Experiment Function
The `experiment` function estimates the probability of drawing a specific combination of balls.

#### Usage
```python
probability = experiment(hat, {"red": 2, "blue": 1}, 4, 1000)
```
- `hat`: A `Hat` object containing balls.
- `expected_balls`: A dictionary specifying the desired number of each ball color.
- `num_balls_drawn`: The number of balls drawn per experiment.
- `num_experiments`: The number of times the experiment is repeated.
- Returns the probability of drawing at least the expected number of each specified ball.

## Example
```python
hat = Hat(yellow=5, red=4, green=2)
probability = experiment(hat, {"red": 2, "green": 1}, 5, 10000)
print("Estimated Probability:", probability)
```
This runs 10,000 experiments and prints the estimated probability of drawing at least 2 red and 1 green ball when drawing 5 balls at a time.

## Dependencies
- Python 3.x
- `random` and `copy` modules (built-in)

## Conclusion
This project provides a simple way to estimate probabilities using random sampling techniques. It can be extended for various probability-based simulations.


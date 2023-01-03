## Puzzle Solver
This code is a puzzle solver that generates a Boolean formula in DIMACS-CNF (Conjunctive Normal Form) format from a puzzle input and uses a SAT (Boolean Satisfiability) solver to find a solution to the puzzle.

## Usage
To use the puzzle solver, define the puzzle input and pass it as an argument to the generate_cnf function, along with the value of n:

# Define the puzzle input
puzzle = {
    "n": 3,
    "black": [(0, 0), (1, 1)],
    "white": [(2, 0)]
}

# Generate the DIMACS-CNF formula for the puzzle
cnf = generate_cnf(puzzle, puzzle["n"])

## Requirements
This code requires Python 3.x and the Pygame module to run. To install Pygame, run the following command:

pip install pygame
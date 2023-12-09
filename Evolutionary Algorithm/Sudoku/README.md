# Sudoko problems

This project implements a Sudoku solver using an evolutionary algorithm. The algorithm generates a Sudoku board, applies an evolutionary approach to evolve and improve the board, and ultimately solves the puzzle.

## Instructions

1. Ensure you have Python installed on your system.
2. Clone the repository
3. Navigate to the project directory: cd Sudoku/
4. Run the script: python sudoku.py

## Project Structure

* sudoku.py: Main script containing the Sudoku solving algorithm.
* README.md: Project documentation.

## Usage

1. The 'filled' list in the script represents the initial filled cells on the Sudoku board. Modify this list to change the initial puzzle configuration.
2. Run the script to start the evolutionary algorithm. The program will print generation information, including the generation number and fitness rate.
3. The algorithm will continue to evolve the Sudoku board through generations until the fittest rank is reached or the maximum number of generations is reached.


## mplementation Details

* The algorithm starts with a partially filled Sudoku board and evolves it through generations.
* The fitness function evaluates the correctness of rows, columns, and squares on the board.
* The evolutionary algorithm involves crossover, mutation, and selection operations to improve the board's fitness.
Sample Filled Sudoku

The script includes a sample filled Sudoku board for testing the algorithm. You can modify the filled list to input your own initial puzzle.

## Note
This project is based on the principles outlined in [this paper](http://micsymposium.org/mics_2009_proceedings/mics2009_submission_66.pdf).

Feel free to experiment with different initial configurations, mutation rates, and generation limits to observe the algorithm's behavior.
# Museum Protection EA

The Museum Protection EA project tackles the Museum Protection Problem, an optimization challenge aiming to strategically deploy security cameras within a museum to maximize coverage while minimizing the number of cameras used. This implementation leverages an Evolutionary Algorithm (EA) to efficiently search for optimal camera placements.

## How to Run

Prerequisites
Ensure the required libraries are installed:

```bash
pip install deap
```

## Configuration
1. Open the main_exp.ipynb notebook.
2. Set the necessary parameters in the code:
    * myinst: Specify the path to the instance file (e.g., myinst="./Instances/WallsTest1_5_cameras.csv").
    * nb_cameras: Set the number of cameras.
    * instance_size: Define the number of cells per dimension.

## Execution
Run the code within the notebook:

```python
# Uncomment and run if necessary
# !pip install deap

# Set the necessary parameters
myinst = "./Instances/WallsTest1_5_cameras.csv"
nb_cameras = 5
instance_size = 100

# ... (rest of the code)

# Run the main function
pop, log, hof = main()
```

## Results
Inspect the output to analyze the results. The best solution found, along with relevant statistics, will be displayed.

## Additional Information

* The code employs an Evolutionary Algorithm using the DEAP library.
* The main_exp.ipynb notebook serves as the main code for solving the Museum Protection Problem.
* The instance file (WallsTest1_5_cameras.csv) provides the layout of the museum, including the locations of walls.


For in-depth insights into the problem, algorithm details, and experimental results, refer to the comprehensive documentation available in the Document.pdf file within the repository. The documentation provides a thorough explanation of the approach, visualizations, and any additional experiments or considerations.
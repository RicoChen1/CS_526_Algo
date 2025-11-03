### Pandemic Simulation Algorithm

The algorithm simulates the spread of a virus across a grid of counties. It determines if any healthy counties remain after the infection has stabilized.

1.  **Initialization**:
    *   A 2D grid is created based on the size specified in the input file.
    *   The grid is populated with initially infected counties from the input coordinates.

2.  **Simulation Loop**:
    *   The simulation runs in daily cycles. In each cycle, it identifies healthy counties that will become infected.
    *   A healthy county becomes infected if it has at least two infected neighbors (up, down, left, or right).
    *   To ensure all decisions for a day are based on the state at the beginning of that day, newly infected counties are recorded in a temporary list.
    *   After checking all healthy counties, the grid is updated with the newly infected ones.
    *   The simulation stops when a full day passes with no new infections.

3.  **Final Result**:
    *   After the simulation ends, the grid is checked for any remaining healthy counties.
    *   The program outputs whether there are any healthy counties left or not.

### How to Run the Simulation

To run the simulation, use the following command in your terminal:

```bash
python pandemic.py <path_to_input_file>
```

Replace `<path_to_input_file>` with the actual path to your input file (e.g., `pandemic_input1.txt`).

**Example:**

```bash
python pandemic.py pandemic_input1.txt
```

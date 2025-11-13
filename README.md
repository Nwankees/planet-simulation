# Planet Simulation

This project is a graphical simulation of planets orbiting a central sun, along with a moon orbiting Earth, implemented using the Pygame library. It visualizes the gravitational interactions and orbital paths of celestial bodies in a 2D environment, allowing users to customize the simulation scale and speed.

## Features

*   Simulates the gravitational interactions and orbital mechanics of multiple celestial bodies.
*   Includes the Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, and Earth's Moon.
*   Visualizes the orbital paths of planets and the moon.
*   Allows interactive zooming in and out of the simulation view.
*   Configurable simulation scale (distance per pixel) and timestep (simulation speed in days per frame).
*   Real-time graphical display of celestial bodies and their movements.

## Technologies Used

*   Python
*   Pygame
*   Python `math` module

## Prerequisites

Before running this simulation, ensure you have the following installed:

*   **Python 3.x**
*   **Pygame library**

## Installation

Follow these steps to get the project up and running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/planet-simulation.git
    cd planet-simulation/Planet\ Simulation
    ```
    (Note: Replace `https://github.com/your-username/planet-simulation.git` with the actual repository URL)

2.  **Install Pygame:**
    ```bash
    pip install pygame
    ```

## Configuration

This project does not use a `.env` file for configuration. The simulation `Scale` and `Timestep` are configured interactively via command-line input when the script is run.

*   **Scale:** Determines how many Astronomical Units (AU) are represented per pixel on the screen. Enter a numeric value or "Default" to use `250`.
*   **Timestep:** Defines how many Earth days each simulation step represents. Enter a numeric value or "Default" to use `0.5` days.

## Usage

To run the planet simulation, navigate to the `Planet Simulation` directory and execute the `planet_sim.py` script:

```bash
python planet_sim.py
```

Upon execution, the program will prompt you to enter the desired `Scale` and `Timestep` values. After providing these inputs, a Pygame window will open displaying the simulation.

**In-simulation Controls:**
*   `+` or `=` : Zoom in
*   `-` or `_` : Zoom out
*   `Q` or close window button: Quit the simulation

## Project Structure

*   `Planet Simulation/`
    *   `planet_sim.py`: The main Python script containing all the simulation logic, `Planet` and `Moon` classes, Pygame window setup, and the main simulation loop.

## License

This project is licensed under the MIT License.
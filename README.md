# Indian States Guessing Game

An interactive educational game designed to test and improve your knowledge of Indian geography. Built with Python using the Turtle library for graphics and Pandas for data manipulation, this application challenges you to name all 28 states of India. Correct guesses are visually plotted directly onto the map.

## Live Demo

![Game Demo](demo.gif)

## Features

-   **Interactive Gameplay:** A simple pop-up dialog prompts the user to guess state names.
-   **Visual Feedback:** Correctly guessed states are written onto their actual geographical location on the map.
-   **Score Tracking:** The title of the input box keeps a running count of correctly identified states.
-   **Data-Driven:** State names and their map coordinates are managed efficiently using the Pandas library, loaded from a `CSV` file.

## Project Setup

To run this project locally, follow these steps.

### Prerequisites

-   Python 3.x
-   `pip` (Python package installer)

### Installation

1.  **Clone the repository to your local machine:**
    ```bash
    git clone https://github.com/dheerajdhami2001-cyber/name_the_states.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd name_the_states
    ```

3.  **Install the required dependency:**
    The project uses the Pandas library to handle the data from the CSV file.
    ```bash
    pip install pandas
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

## Code Structure

The project is organized into the following key files:

-   `main.py`: The main script that initializes the screen, loads the map, and contains the primary game loop for handling user input.
-   `state_name.py`: Contains the `StateName` class responsible for reading the state data, fetching coordinates, and plotting the names on the map.
-   `28_states.csv`: The dataset containing the names of the 28 Indian states and their corresponding x, y coordinates for plotting.
-   `india.gif`: The background map image used by the Turtle graphics screen.

## Acknowledgments

This project was inspired by and completed with the guidance of the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)** by Dr. Angela Yu.


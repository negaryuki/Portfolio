# U.S. States Game

Welcome to the U.S. States Game!
This interactive game helps you learn and memorize the U.S. states by prompting you to name them and then displaying their locations on a map. 
The project was developed using Python's Turtle graphics library and pandas for data manipulation.
This project was developed as part of the 100 Days Of Code challenge.

![U.S. States Game Preview](stateguess.gif)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Feedback and Contributions](#feedback-and-contributions)
- [License](#license)

## Introduction

The U.S. States Game is an educational tool that displays a map of the United States and prompts you to name the states. As you correctly identify each state, it is labeled on the map. The game tracks your progress and creates a list of states you need to learn if you decide to exit before naming all 50 states.

## Key Features

- **Interactive Map**: Displays a map of the United States and prompts you to identify states.
- **Progress Tracking**: Keeps track of the states you have correctly identified.
- **Learning Tool**: Generates a list of states you need to learn based on your progress.
- **User-Friendly Interface**: Simple and intuitive interface created with the Turtle graphics library.

## Installation

To run the U.S. States Game on your local machine, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/us-states-game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd us-states-game
    ```

3. Ensure you have the required dependencies installed. You can install them using:

    ```bash
    pip install pandas
    ```

4. Ensure you have the images `blank_states_img.gif` and the `50_states.csv` file in the project directory.

## Usage

To start the U.S. States Game, run the following command:

```bash
python us_states_game.py
```

This will launch the game window. Enter the names of the U.S. states in the pop-up text box. If you want to stop the game, type "Exit". The game will generate a CSV file named `states_to_learn.csv` with the names of the states you have not yet guessed correctly.

## Feedback and Contributions

I value your feedback and welcome any suggestions for improvement or new features. If you'd like to contribute to this project or report any issues, please don't hesitate to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy learning the U.S. states with the U.S. States Game!

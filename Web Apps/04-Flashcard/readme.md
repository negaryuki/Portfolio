# Flash Card Learner

Welcome to the Flash Card Learner project! 
This application helps you learn French words through an interactive flash card system. 
The project was developed using Python's Tkinter library for the GUI and pandas for data manipulation.
This project was developed as part of the 100 DaysOf Code challenge.

![Flash Card Learner Preview](flashcard.gif)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Feedback and Contributions](#feedback-and-contributions)
- [License](#license)

## Introduction

The Flash Card Learner is an educational tool that displays a French word on a flash card, and after a short delay, it flips to show the English translation. 
Users can mark words as known or unknown, and the application tracks progress by saving the words you still need to learn.

## Key Features

- **Interactive Flash Cards**: Displays French words and their English translations on flash cards.
- **Word Tracking**: Keeps track of words you have learned and those you still need to learn.
- **User-Friendly Interface**: Simple and intuitive interface created with Tkinter.
- **Persistent Progress**: Saves your progress in a CSV file so you can pick up where you left off.

## Installation

To run the Flash Card Learner on your local machine, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/flash-card-learner.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flash-card-learner
    ```

3. Ensure you have the required dependencies installed. You can install them using:

    ```bash
    pip install pandas
    ```

4. Ensure you have the images `card_front.png`, `card_back.png`, `wrong.png`, and `right.png` in an `Images` folder within the project directory.

5. Prepare your CSV files: `french_words.csv` (initial words list) and `words_to_learn.csv` (to track learning progress) in a `data` folder within the project directory.

## Usage

To start the Flash Card Learner application, run the following command:

```bash
python flash_card_learner.py
```

This will launch the application window. Use the buttons to indicate whether you knew the word or not. The flash card will flip to show the English translation after a short delay.

## Feedback and Contributions

I value your feedback and welcome any suggestions for improvement or new features. If you'd like to contribute to this project or report any issues, please don't hesitate to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy learning French with the Flash Card Learner!

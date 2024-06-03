# PDF to Audiobook Converter

Welcome to the PDF to Audiobook Converter! This application converts PDF documents into audiobooks using Google's gTTS (Google Text-to-Speech) API. The project is built using Flask, Python, and SQLite.

![PDF to Audiobook Converter Preview](converter.gif)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The PDF to Audiobook Converter is a web application that allows users to upload PDF files and convert them into audio files. 
This is achieved using the gTTS (Google Text-to-Speech) API. 
The backend is powered by Flask, and the data is stored in an SQLite database.

## Features

- Upload PDF files
- Convert PDF text to audio using gTTS
- Download the generated audio files

## Installation

1. Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/yourusername/pdf-to-audiobook-converter.git
    ```

3. Navigate to the project directory:

    ```bash
    cd pdf-to-audiobook-converter
    ```

4. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the following command:

```bash
python app.py
```

This will start the Flask development server. Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.


## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature/your-feature-name
    ```

3. Make your changes and commit them:

    ```bash
    git commit -m 'Add some feature'
    ```

4. Push to the branch:

    ```bash
    git push origin feature/your-feature-name
    ```

5. Create a pull request.

Please make sure your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for checking out the PDF to Audiobook Converter! I hope you find it useful and convenient.

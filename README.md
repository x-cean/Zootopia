# Zootopia

Zootopia is a Python project that fetches animal data from an API and generates an HTML file displaying the information.

## Features

- Fetch animal data from the API Ninjas API.
- Display animal information including diet, location, type, and slogan.
- Filter animals by skin type.
- Generate an HTML file with the animal data.

## Requirements

- Python 3.x
- `pip` for managing Python packages

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/x-cean/Zootopia.git
    cd Zootopia
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the `animals_web_generator.py` script:

    ```sh
    python Zootopia/animals_web_generator.py
    ```

2. Enter the name of an animal when prompted.

3. Select a skin type from the displayed list or enter `0` to display all animals.

4. The generated HTML file `animals.html` will be created in the `zootopia_api/Zootopia` directory.

## Configuration

- Update the `API_KEY` in `animals_web_generator.py` with your API Ninjas API key.

## Contributing

Contribution is welcome! 
Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.
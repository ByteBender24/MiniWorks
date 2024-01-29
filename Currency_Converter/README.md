# Currency Converter

A simple currency converter with a graphical user interface (GUI) built in Python using Tkinter.
A terminal version is also given

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ByteBender24/MiniWorks.git
    cd Currency_Converter
    ```

2. Install the required libraries:

    ```bash
    pip install requests
    ```

3. Obtain your API key from [Free Currency API](https://freecurrencyapi.com/) and replace `'YOUR OWN API KEY'` with your actual API key in the `API_KEY` variable in the code.

4. Run the program:

    For gui program:
    ```bash
    python Currency_Converter.py
    ```

    For terminal program:
    ```bash
    python original_code_without_gui.py
    ```

## Usage

- Enter the base currency code and press the "Convert" button to get conversion rates for selected currencies.
- To exit the program, enter 'Q' in the base currency input field.

## Screenshots

1. **Main Interface**
   
   ![Main Interface](screenshots/main_interface.png)

2. **Currency Conversion Example**

   ![Currency Conversion](screenshots/conversion_example.png)

3. **Currency Conversion Example**

   ![Currency Conversion](screenshots/conversion_example.png)

4. **Terminal Program**

   ![Terminal Program](screenshots/program_exit.png)

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new pull request.

Happy coding!

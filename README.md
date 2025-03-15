# Temperature Converter (Python Console App)

## Description

A console-based **Temperature Converter** built in Python as part of my software engineering learning journey. This project allows users to convert temperatures between Celsius and Fahrenheit through an interactive menu, featuring:

- A menu-driven interface with options to convert Celsius to Fahrenheit, Fahrenheit to Celsius, or exit.
- Accurate conversions using formulas `F = (C * 9/5) + 32` and `C = (F - 32) * 5/9`, rounded to one decimal place.
- Robust input validation to handle non-numeric entries gracefully, looping until valid input is provided.

## Features

- Interactive menu with three options: 1) Celsius to Fahrenheit, 2) Fahrenheit to Celsius, 3) Exit.
- Error handling with `try`/`except` to catch invalid inputs (e.g., letters instead of numbers).
- Clean output using f-strings (e.g., "25.5°C is 77.9°F").
- Persistent prompting for temperature inputs until valid, enhancing user experience.

## Skills Learned

- **Python Basics**: Functions, loops, conditionals, and console I/O.
- **Error Handling**: Using `try`/`except` for `ValueError`.
- **Arithmetic**: Implementing temperature conversion formulas.
- **String Formatting**: Dynamic output with f-strings.

## How to Run

1. Clone this repository.
2. Ensure Python 3.x is installed.
3. Navigate to the project folder and run: `python temperature_converter.py`.
4. Follow the menu prompts to convert temperatures!

## Example

Welcome to the Temperature Converter!
Convert between Celsius and Fahrenheit easily.

Menu:

1. Convert from Celsius to Fahrenheit
2. Convert from Fahrenheit to Celsius
3. Exit
   Enter your choice (1-3): 1

Enter a temperature to convert to fahrenheit: 25.5

25.5°C is 77.9°F

## Future Enhancements

- Add a "Press Enter to continue" prompt after conversions.
- Support additional temperature scales (e.g., Kelvin).
- Include unit tests for conversion functions.

## Author

Geoff Walsh

**Date**: March 2025

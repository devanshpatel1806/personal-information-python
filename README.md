# Personal Information Python Program

## Project Overview

The Personal Information Python Program is a simple interactive Python program that collects basic information from the user and demonstrates fundamental Python programming concepts.

The program collects the user's name, age, height, and favourite number. It calculates the estimated birth year, demonstrates arithmetic operators and type casting, and displays the data type and ID of each variable.

## Objectives

- Understand print() and input().
- Understand Python variables and data types.
- Demonstrate arithmetic operators.
- Calculate the estimated birth year using the user's age.
- Understand type casting.
- Use type() and id() functions.
- Create formatted and user-friendly output.

## Features

- Welcome message.
- Collects name, age, height, and favourite number.
- Calculates estimated birth year.
- Demonstrates addition, subtraction, multiplication, and division.
- Displays variable values, data types, and IDs.
- Demonstrates type casting.
- Displays a final thank-you message.

## Python Concepts Used

### 1. Input and Output

The program uses input() to collect information from the user and print() to display information and results.

### 2. Variables and Data Types

The program uses:

- name - String (str)
- age - Integer (int)
- height - Float (float)
- favourite_number - Integer (int)

### 3. Arithmetic Operators

The program demonstrates:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

The estimated birth year is calculated using:

birth_year = current_year - age

### 4. Type Casting

The program demonstrates two examples of type casting.

Float to Integer:

height_integer = int(height)

Integer to Float:

age_float = float(age)

### 5. type() Function

The type() function is used to identify the data type of a variable.

Example:

type(age)

### 6. id() Function

The id() function is used to display the unique identity of a Python object.

Example:

id(age)

The ID value may be different each time the program is executed.

### 7. Formatted Strings

The program uses f-strings to display information in a user-friendly format.

Example:

print(f"Name: {name}")

## Program Flow

Start

↓

Display Welcome Message

↓

Collect Name, Age, Height and Favourite Number

↓

Store Information in Variables

↓

Perform Calculations

↓

Calculate Estimated Birth Year

↓

Display User Information

↓

Display Data Types and IDs

↓

Perform Type Casting

↓

Display Arithmetic Results

↓

Thank You Message

↓

End

## Example Input

Name: Devansh
Age: 23
Height: 1.86
Favourite Number: 18

## Example Output

Name: Devansh
Age: 23
Height: 1.86 meters
Favourite Number: 18
Estimated Birth Year: 2003

The program also displays the data type and ID of each variable and demonstrates type casting.

## Assumptions

- The user enters a valid name.
- Age is entered as a positive integer.
- Height is entered as a numeric value in meters.
- Favourite number is entered as an integer.
- The current year is assumed to be 2026.
- The birth year is an approximate calculation based on the user's age.

## Project Structure

personal-information-python/

Personal_Information.py

README.md

## Technologies Used

- Python 3
- Python IDLE
- GitHub

## How to Run

1. Download or clone this repository.
2. Open Personal_Information.py in Python IDLE.
3. Press F5 to run the program.
4. Enter the requested information.
5. View the results in the Python Shell.

## Learning Outcomes

Through this project, I learned:

- How to take user input.
- How to use variables.
- How to work with different data types.
- How to use arithmetic operators.
- How to perform type casting.
- How to use type() and id().
- How to use formatted strings.
- How to create an interactive Python program.
- How to upload a project to GitHub.

## Author

Devansh Patel

This project was created as part of a Python programming assignment.

## License

This project is created for educational purposes.

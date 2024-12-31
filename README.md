# freecodecamp_demographic_data

# Demographic Data Analyzer

This project analyzes demographic data extracted from the 1994 U.S. Census database using Python and Pandas. The goal is to answer various demographic-related questions and validate the implementation with unit tests.

---

## Features

The analysis answers the following questions:
1. How many people of each race are represented in the dataset?
2. What is the average age of men?
3. What percentage of people have a Bachelor's degree?
4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) earn more than 50K?
5. What percentage of people without advanced education earn more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of people who work the minimum number of hours per week have a salary of >50K?
8. Which country has the highest percentage of people earning >50K, and what is that percentage?
9. What is the most popular occupation for those earning >50K in India?

---

## Files in the Repository

### 1. `demographic_data_analyzer.py`
This file contains the main analysis function, `demographic_data_analysis`, which processes the dataset and calculates the required statistics.

### 2. `main.py`
The main entry point for the project. This file:
- Runs the analysis and prints the results.
- Executes the unit tests from `test_module.py`.

### 3. `test_module.py`
Contains unit tests using Python's `unittest` module to validate the correctness of the analysis. Each functionality in `demographic_data_analyzer.py` has an associated test case.

---

## Requirements

- Python 3.7+
- Pandas library

To install dependencies, run:
```bash
pip install pandas

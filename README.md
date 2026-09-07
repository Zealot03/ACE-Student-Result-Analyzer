# ACE-Student-Result-Analyzer
A simple Python program that analyzes the marks of multiple students.

## Features

- Enter names and marks of multiple students
- Calculate class average
- Find the highest-scoring student
- Find the lowest-scoring student
- Count passed and failed students
- Assign a grade to each student
- Calculate pass percentage
- Save the results to a text file

## Grading System

- 90 and above: A+
- 80 - 89: A
- 70 - 79: B
- 60 - 69: C
- 50 - 59: D
- Below 50: F

## Approach

I used a list to store the details of all students.

Each student is stored as a dictionary containing their name,
marks and grade.

Different functions are used for different parts of the program.
One function takes student details, another calculates the class
analysis, and other functions display and save the results.

The program also checks whether a student has passed or failed
based on a passing mark of 50.

## Language
Python

## Output File

The program can save the result report in:
student_results.txt

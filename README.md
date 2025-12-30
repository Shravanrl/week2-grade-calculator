# Student Grade Calculator

## Project Description
A comprehensive grade calculator that processes multiple students' marks, calculates grades with personalized comments, and provides class statistics. This project demonstrates the use of conditionals, loops, lists, functions, and error handling in Python.

## What I Learned
1. **Conditional Logic**: Used if/elif/else statements for grade calculation  
2. **Lists**: Stored and managed multiple student records  
3. **Loops**: Used for loops and while loops to process data  
4. **Error Handling**: Used try-except blocks to handle invalid inputs  
5. **Functions**: Organized logic into reusable functions  

## Features
- ✅ Processes multiple students  
- ✅ Calculates grades using a defined grading system  
- ✅ Provides personalized comments  
- ✅ Computes class statistics (average, highest, lowest)  
- ✅ Input validation for marks  
- ✅ Error handling for edge cases  
- ✅ Supports test input using file redirection  

## How to Run

```bash
# Navigate to project folder
cd week2-grade-calculator
```

## Grading System
- **A**: 90–100 (Excellent!)
- **B**: 80–89 (Very Good!)
- **C**: 70–79 (Good)
- **D**: 60–69 (Needs Improvement)
- **F**: 0–59 (Failed – Please seek help)

## Sample Output
```
Name            Avg   Grade   Comment
-------------------------------------
John Smith      88.3  B       Very Good!
Sarah Johnson   81.3  B       Very Good!
```

## Challenges & Solutions
- **Challenge**: Handling invalid marks input  
  **Solution**: Used while loops with try-except blocks  

- **Challenge**: Formatting output neatly  
  **Solution**: Used string formatting  

- **Challenge**: Calculating multiple statistics  
  **Solution**: Used lists and built-in Python functions  

## Project Structure
```
week2-grade-calculator/
│── grade_calculator.py
│── test_students.txt
│── README.md
```

## Author
**Shravan R L**


# Run the program
python grade_calculator.py

# Run with sample test data
python grade_calculator.py < test_students.txt

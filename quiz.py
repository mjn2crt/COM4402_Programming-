# ====================================
"""
Holton College Digital Quiz System          # Program title description
Simple Version Using Only Variables          # Explains program simplicity
Author: Muhammad Jabran Ahmad Nisar           # Author name
Student Number: 2420992                       # Student ID
Date: 25 January 2026                        # Date of creation
"""
# ====================================

# -----------------------------
# DATA STORAGE
# -----------------------------

              # List to store all quiz questions
questions = [                                
    {
        "question": "What is the capital of France?",     # Question text
        "options": ["1. London", "2. Paris", "3. Berlin", "4. Madrid"],  # Multiple-choice options
        "answer": 2                                        # Correct option number
    },
    {
        "question": "Which data structure uses key-value pairs?",  # Question text
        "options": ["1. List", "2. Tuple", "3. Dictionary", "4. Set"],  # Options
        "answer": 3                                                # Correct answer index
    },
    {
        "question": "What does CPU stand for?",            # Question text
        "options": [                                       # List of answer options
            "1. Central Processing Unit",
            "2. Computer Personal Unit",
            "3. Central Processor Unit",
            "4. Computer Processing Unit"
        ],
        "answer": 1                                         # Correct answer
    },
    {
        "question": "Which programming language is known for data science?",  # Question
        "options": ["1. Java", "2. Python", "3. C++", "4. Ruby"],             # Options
        "answer": 2                                                           # Correct option
    },
    {
        "question": "What is the time complexity of binary search?",          # Question
        "options": ["1. O(n)", "2. O(n log n)", "3. O(log n)", "4. O(1)"],    # Options
        "answer": 3                                                           # Correct answer
    }
]

# -----------------------------
# INITIALISATION
# -----------------------------

score = 0                                       # Stores the user's score
question_index = 0                              # Tracks current question number
total_questions = len(questions)                # Total number of questions

# -----------------------------
# QUIZ START
# -----------------------------

print("=" * 50)                                              # Prints a decorative line
print("Welcome to the Holton College Digital Quiz System!")  # Welcome message
print("=" * 50)                                              # Decorative line
print("Answer using 1, 2, 3, or 4")                          # User instructions
print("-" * 50)                                              # Separator line

# -----------------------------
# MAIN QUIZ LOOP
# -----------------------------

while question_index < total_questions:             # Loop until all questions are answered

    current_question = questions[question_index]    # Get the current question dictionary

    print(f"\nQuestion {question_index + 1}: {current_question['question']}")  # Display question number and text
    print("Options:")                               # Label for answer options

    for option in current_question["options"]:      # Loop through answer options
        print(option)                               # Print each option

    # -------------------------
    # INPUT VALIDATION
    # -------------------------
    while True:                                 # Loop until valid input is entered
        user_input = input("\nYour answer: ").strip()  # Take user input and remove extra spaces

        if user_input.isdigit():                # Check if input is a number
            user_answer = int(user_input)       # Convert input to integer
            if 1 <= user_answer <= 4:           # Check if input is between 1 and 4
                break                           # Exit loop if valid
            else:
                print("Invalid input. Please enter a number between 1 and 4.")  # Range error message
        else:
            print("Invalid input. Please enter a number between 1 and 4.")      # Non-numeric error message

    # -------------------------
    # ANSWER CHECKING
    # -------------------------
    if user_answer == current_question["answer"]:  # Compare user answer with correct answer
        print("Correct!")                          # Feedback for correct answer
        score += 1                                 # Increase score by 1
    else:
        print("Incorrect!")                        # Feedback for wrong answer

    question_index += 1                            # Move to the next question
    print("-" * 50)                                # Separator line

# -----------------------------
# QUIZ RESULTS
# -----------------------------

percentage = (score / total_questions) * 100      # Calculate percentage score

print("\n" + "=" * 50)                            # Decorative line
print("QUIZ COMPLETE!")                           # Completion message
print("=" * 50)                                   # Decorative line
print(f"You scored {score} out of {total_questions}")  # Display score
print(f"Percentage: {percentage:.1f}%")           # Display percentage score

# Performance feedback (enhancement)
if percentage == 100:                              # Check for perfect score
    print("Perfect score! Excellent work!")
elif percentage >= 80:                             # Check for high score
    print("Great job!")
elif percentage >= 60:                             # Check for pass score
    print("Good effort!")
elif percentage >= 40:                             # Check for low score
    print("Keep practicing!")
else:
    print("Don’t give up!")                        # Encouragement for very low score

print("\nThank you for using the Holton College Digital Quiz System!")  # Closing message
print("=" * 50)                                   # Decorative line

# ====================================

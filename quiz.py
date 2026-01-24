# ====================================
"""
Holton College Digital Quiz System
Improved Version Using Functions
Author: Muhammad Jabran Ahmad Nisar
Student Number: 2420992
Date: 25 January 2026
"""
# ====================================

# -----------------------------
# DATA STORAGE
# -----------------------------

# List of dictionaries to store all quiz questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. London", "2. Paris", "3. Berlin", "4. Madrid"],
        "answer": 2  # Correct option number
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ["1. List", "2. Tuple", "3. Dictionary", "4. Set"],
        "answer": 3   # Correct option number
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "1. Central Processing Unit",
            "2. Computer Personal Unit",
            "3. Central Processor Unit",
            "4. Computer Processing Unit"
        ],
        "answer": 1   # Correct option number
    },
    {
        "question": "Which programming language is known for data science?",
        "options": ["1. Java", "2. Python", "3. C++", "4. Ruby"],
        "answer": 2   # Correct option number
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["1. O(n)", "2. O(n log n)", "3. O(log n)", "4. O(1)"],
        "answer": 3   # Correct option number
    }
]

# -----------------------------
# HELPER FUNCTION
# -----------------------------

def get_valid_input(min_val, max_val):
    """
    This function repeatedly asks the user for input
    until they enter a valid number within the given range.
    """
    while True:
        user_input = input("\nYour answer: ").strip()  # Get user input and remove spaces

        if user_input.isdigit():  # Check if input contains only digits
            ans = int(user_input)  # Convert input to integer

            if min_val <= ans <= max_val:  # Check if input is within valid range
                return ans  # Return valid answer
            else:
                print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")
        else:
            print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")

# -----------------------------
# INITIALISATION
# -----------------------------

score = 0                         # Stores how many questions the user gets correct
question_index = 0                # Tracks which question the user is currently on
total_questions = len(questions)  # Stores total number of questions in the quiz

# -----------------------------
# QUIZ START
# -----------------------------

print("=" * 50)  # Decorative line
print("Welcome to the Holton College Digital Quiz System!")
print("=" * 50)
print("Answer using 1, 2, 3, or 4")  # Instructions for the user
print("-" * 50)

# -----------------------------
# MAIN QUIZ LOOP
# -----------------------------

# Loop through all questions until the last one is reached
while question_index < total_questions:

    current_question = questions[question_index]  # Get current question dictionary

    # Display question number and question text
    print(f"\nQuestion {question_index + 1}: {current_question['question']}")
    print("Options:")

    # Display all answer options
    for option in current_question["options"]:
        print(option)

    # Get validated input from the user (must be between 1 and 4)
    user_answer = get_valid_input(1, 4)

    # -------------------------
    # ANSWER CHECKING
    # -------------------------

    # Compare user's answer with the correct answer
    if user_answer == current_question["answer"]:
        print("Correct!")
        score += 1  # Increase score if correct
    else:
        print("Incorrect!")

    question_index += 1  # Move to the next question
    print("-" * 50)

# -----------------------------
# QUIZ RESULTS
# -----------------------------

percentage = (score / total_questions) * 100  # Calculate percentage score

print("\n" + "=" * 50)
print("QUIZ COMPLETE!")
print("=" * 50)
print(f"You scored {score} out of {total_questions}")
print(f"Percentage: {percentage:.1f}%")

# Provide feedback based on performance
if percentage == 100:
    print("Perfect score! Excellent work!")
elif percentage >= 80:
    print("Great job!")
elif percentage >= 60:
    print("Good effort!")
elif percentage >= 40:
    print("Keep practicing!")
else:
    print("Do not give up!")

print("\nThank you for using the Holton College Digital Quiz System!")
print("=" * 50)

# ====================================

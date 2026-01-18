# ====================================
"""
Holton College Digital Quiz System
Simple Version Using Only Variables
Author: Muhammad Jabran Ahmad Nisar
Student Number: 2420992
Date: 25 January 2026
"""
# ====================================

# -----------------------------
# DATA STORAGE
# -----------------------------

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. London", "2. Paris", "3. Berlin", "4. Madrid"],
        "answer": 2
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ["1. List", "2. Tuple", "3. Dictionary", "4. Set"],
        "answer": 3
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "1. Central Processing Unit",
            "2. Computer Personal Unit",
            "3. Central Processor Unit",
            "4. Computer Processing Unit"
        ],
        "answer": 1
    },
    {
        "question": "Which programming language is known for data science?",
        "options": ["1. Java", "2. Python", "3. C++", "4. Ruby"],
        "answer": 2
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["1. O(n)", "2. O(n log n)", "3. O(log n)", "4. O(1)"],
        "answer": 3
    }
]

# -----------------------------
# INITIALISATION
# -----------------------------

score = 0
question_index = 0
total_questions = len(questions)

# -----------------------------
# QUIZ START
# -----------------------------

print("=" * 50)
print("Welcome to the Holton College Digital Quiz System!")
print("=" * 50)
print("Answer using 1, 2, 3, or 4")
print("-" * 50)

# -----------------------------
# MAIN QUIZ LOOP 
# -----------------------------

while question_index < total_questions:

    current_question = questions[question_index]

    print(f"\nQuestion {question_index + 1}: {current_question['question']}")
    print("Options:")

    for option in current_question["options"]:
        print(option)

    # -------------------------
    # INPUT VALIDATION
    # -------------------------
    while True:
        user_input = input("\nYour answer: ").strip()

        if user_input.isdigit():
            user_answer = int(user_input)
            if 1 <= user_answer <= 4:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    # -------------------------
    # ANSWER CHECKING
    # -------------------------
    if user_answer == current_question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Move to next question
    question_index += 1
    print("-" * 50)

# -----------------------------
# QUIZ RESULTS
# -----------------------------

percentage = (score / total_questions) * 100

print("\n" + "=" * 50)
print("QUIZ COMPLETE!")
print("=" * 50)
print(f"You scored {score} out of {total_questions}")
print(f"Percentage: {percentage:.1f}%")

# Performance feedback (enhancement)
if percentage == 100:
    print("Perfect score! Excellent work!")
elif percentage >= 80:
    print("Great job!")
elif percentage >= 60:
    print("Good effort!")
elif percentage >= 40:
    print("Keep practicing!")
else:
    print("Don’t give up!")

print("\nThank you for using the Holton College Digital Quiz System!")
print("=" * 50)

# ====================================

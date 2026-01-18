#====================================

"""
Holton College Digital Quiz System
Simple Version Using Only Variables
Author: [Your Name]
Student Number: [Your Student Number]
Date: January 2026
"""

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

total_questions = len(questions)
score = 0
question_number = 1

# -----------------------------
# QUIZ START
# -----------------------------

print("=" * 50)
print("Welcome to the Holton College Digital Quiz System!")
print("=" * 50)
print("\nPlease answer with the number (1, 2, 3, or 4).")
print("-" * 50)

# -----------------------------
# MAIN QUIZ LOOP
# -----------------------------

for question in questions:
    print(f"\nQuestion {question_number}: {question['question']}")
    print("\nOptions:")

    for option in question["options"]:
        print(f"  {option}")

    # Input validation loop
    while True:
        user_input = input("\nYour answer: ").strip()

        if user_input.isdigit():
            user_answer = int(user_input)

            if 1 <= user_answer <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a number (1–4).")

    # Check answer
    if user_answer == question["answer"]:
        print("✓ Correct!")
        score += 1
    else:
        print(f"✗ Incorrect. The correct answer was: {question['answer']}")

    question_number += 1
    print("-" * 50)

# -----------------------------
# RESULTS
# -----------------------------

percentage = (score / total_questions) * 100

print("\n" + "=" * 50)
print("QUIZ COMPLETE!")
print("=" * 50)
print(f"\nYou scored {score} out of {total_questions}.")
print(f"That's {percentage:.1f}%")

if percentage == 100:
    print("\n Perfect score! Excellent work!")
elif percentage >= 80:
    print("\n Great job!")
elif percentage >= 60:
    print("\n Good effort!")
elif percentage >= 40:
    print("\n Keep practicing!")
else:
    print("\n Don’t give up!")

print("\nThank you for using the Holton College Digital Quiz System!")
print("=" * 50)

# =========================
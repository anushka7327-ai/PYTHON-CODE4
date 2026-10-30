from questions import questions
from quiz import start_quiz

print("🎯 Welcome to Python Quiz!")

score = start_quiz(questions)

print("\n===== RESULT =====")
print(f"Your Score: {score}/{len(questions)}")
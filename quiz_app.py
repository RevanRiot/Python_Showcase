# File: quiz_app.py

def run_quiz(questions):
    """Runs a quiz with the given questions."""
    score = 0
    for question, options, answer in questions:
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        user_answer = int(input("Enter your answer (1/2/3/4): "))
        
        if options[user_answer - 1] == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
        print()

    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    questions = [
        ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
        ("What is 5 + 7?", ["10", "11", "12", "13"], "12"),
        ("Who wrote '1984'?", ["Orwell", "Huxley", "Hemingway", "Dickens"], "Orwell")
    ]
    run_quiz(questions)

import random
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "correct_answer": "7"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["6", "8", "10", "12"],
        "correct_answer": "8"
    }
]
def display_question(question):
    print("\n" + question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
    user_input = input("Enter your choice (1-4): ")
    return int(user_input) if user_input.isdigit() else None

# Function to evaluate the user's response
def evaluate_response(question, response):
    correct_answer = question["correct_answer"]
    if response == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")
        return 0

# Function to run the quiz
def run_quiz(questions):
    score = 0
    random.shuffle(questions)  # Shuffle the questions only once
    for question in questions:
        user_response = None
        while user_response not in [1, 2, 3, 4]:
            user_response = display_question(question)
            if user_response is None:
                print("Invalid input. Please enter a number between 1 and 4.")

        score += evaluate_response(question, question["options"][user_response - 1])

    print(f"\nQuiz completed! Your score: {score}/{len(questions)}")
run_quiz(questions)

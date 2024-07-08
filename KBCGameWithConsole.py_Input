# Define the questions and options
questions = {
    "Sachin is playing for which country?": {
        "options": ["A).India", "B).Srilanka"],
        "correct": "A"
    },
    "Indore is in which state?": {
        "options": ["A).U.P.", "B).M.P."],
        "correct": "B"
    },
    "Capital of India?": {
        "options": ["A).Delhi", "B).Indore"],
        "correct": "A"
    }
}

# Initialize the user's answers
user_answers = {}

# Play the game
for question, details in questions.items():
    print(question)
    print("Please select the correct answer:")
    for option in details["options"]:
        print(option)
    user_answer = input("Enter your answer: ")
    user_answers[question] = user_answer

# Check the answers
correct_answers = ["A", "B", "A"]
for i, (question, user_answer) in enumerate(user_answers.items()):
    if user_answer == correct_answers[i]:
        print(f"Correct answer for {question}!")
    else:
        print(f"Incorrect answer for {question}. The correct answer is {questions[question]['correct']}")

import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("What is your answer? :"))
    question["user_choice"] = user_choice
    
    
for index ,question in enumerate(data):
    message = f"{index + 1}: Your answer: {question['user_choice']} - Correct answer: {question['correct_answer']}"
    print(message)

    if question["user_choice"] == question["correct_answer"]:
        score += 1
        print("Correct answer!")
    else:
        print("Wrong Answer.")
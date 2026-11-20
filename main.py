import csv
from datetime import datetime

def get_score(criterion):
    while True:
        try:
            score = int(input(f"Rate {criterion} (1-5): "))
            if 1 <= score <= 5:
                return score
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Enter a whole number.")

def evaluate_response():
    print("\n=== AI RESPONSE EVALUATOR ===")

    question = input("Enter the original question: ")
    response = input("Enter the AI-generated response: ")

    print("\nRate the response from 1 (Poor) to 5 (Excellent).")

    accuracy = get_score("Accuracy")
    relevance = get_score("Relevance")
    clarity = get_score("Clarity")
    instruction = get_score("Instruction Following")

    total = accuracy + relevance + clarity + instruction
    average = total / 4

    print("\n=== EVALUATION REPORT ===")
    print(f"Total Score: {total}/20")
    print(f"Average Score: {average:.2f}/5")

    if average >= 4:
        print("Result: Good")
    elif average >= 3:
        print("Result: Needs Improvement")
    else:
        print("Result: Poor")

    with open("evaluation_results.csv", "a", newline="",
              encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            question,
            response,
            accuracy,
            relevance,
            clarity,
            instruction,
            average
        ])

    print("\nEvaluation saved successfully!")

evaluate_response()

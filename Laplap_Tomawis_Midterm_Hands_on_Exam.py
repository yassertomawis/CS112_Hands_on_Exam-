import random

def generate_question():
    operation = random.choice(['+', '-', '*', '/'])
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:
        result = num1 // num2
    question = f"{num1} {operation} {num2} = ?"

    return question, result

def main():
    while True:
        question, result = generate_question()
        print(question)
        answer = int(input("Please enter your answer: "))
        if answer == result:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", result)
        choice = input("Do you want to try another question? (y/n): ")
        if choice.lower() != 'y':

            break

if __name__ == "__main__":

    main()

import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = f"{left} {operator} {right}"

    # Manually calculate the answer instead of using eval()
    if operator == "+":
        answer = left + right
    elif operator == "-":
        answer = left - right
    elif operator == "*":
        answer = left * right

    return expr, answer

wrong = 0
input("Press Enter to continue...")
print("____________________________")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problems()
    while True:
        try:
            guess = int(input(f"Problem #{i+1}: {expr} = "))
            if guess == answer:
                break
            wrong += 1
            print("Incorrect, try again.")
        except ValueError:
            print("Please enter a valid integer.")

end_time = time.time()
total_time = end_time - start_time

print("____________________________")
print(f"Total Time: {total_time:.2f} seconds")
print(f"Number of incorrect attempts: {wrong}")

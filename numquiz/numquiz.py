import time
import random

def main():
    start_time = time.time()
    score = 0

    # Shuffle the numbers from 0 to 49
    numbers = list(range(50))
    random.shuffle(numbers)

    # Ask the user each question
    for number in numbers:
        # Get the correct answer
        correct_answer = 2 ** number

        # Keep asking until the user gets the answer correct
        while True:
            try:
                # Ask the user the question
                user_answer = int(input(f"What is 2^{number}? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            else:
                # Check if the user's answer is correct
                if user_answer == correct_answer:
                    score += 1
                    print("Correct!")
                    break
                else:
                    print(f"Incorrect. The correct answer is {correct_answer}.")

    # Calculate the time taken
    end_time = time.time()
    time_taken = end_time - start_time

    # Print the score and time taken
    print(f"You got {score} out of 50 questions correct.")
    print(f"It took you {time_taken:.2f} seconds to complete the quiz.")

if __name__ == "__main__":
    main()
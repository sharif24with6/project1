# Define the QuizBrain class
class QuizBrain:
    # Constructor to initialize QuizBrain object
    def __init__(self, question_list):
        self.question_number = 0  # Initialize question number
        self.score = 0  # Initialize score
        self.question_list = question_list  # Store list of questions
        self.completed = False  # Flag to track if quiz is completed

    # Method to check if there are still questions left to ask
    def still_has_question(self):
        return self.question_number < len(self.question_list) and not self.completed

    # Method to ask the next question
    def next_question(self):
        if self.still_has_question():  # Check if there are still questions left
            current_question = self.question_list[self.question_number]  # Get current question
            self.question_number += 1  # Increment question number
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")  # Prompt user for answer
            self.check_answer(user_answer, current_question.answer)  # Check user's answer
        else:
            self.completed = True  # Set quiz as completed
            print("Quiz completed!")  # Print completion message
            self.print_final_score()  # Print final score

    # Method to check user's answer against correct answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():  # Compare answers (case insensitive)
            self.score += 1  # Increment score if correct
            print("You got it right!")  # Print message for correct answer
        else:
            print("That's wrong.")  # Print message for incorrect answer
            self.completed = True  # Set quiz as completed on incorrect answer

        print(f"The correct answer was: {correct_answer}")  # Print correct answer
        self.print_score()  # Print current score

    # Method to print current score
    def print_score(self):
        print(f"Your current score is: {self.score}/{self.question_number}")  # Print current score
        print("")  # Print blank line for formatting

    # Method to print final score
    def print_final_score(self):
        print(f"Your final score is: {self.score}/{self.question_number}")  # Print final score

# End of quiz_brain.py

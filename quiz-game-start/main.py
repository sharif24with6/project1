# Import necessary classes from modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Function to create question bank from question_data
def create_question_bank(data):
    question_bank = []
    for quest in data:
        question_text = quest["text"]
        question_answer = quest["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank

# Function to run the quiz
def run_quiz(quiz):
    while quiz.still_has_question():  # Loop until there are no more questions or quiz is completed
        quiz.next_question()  # Ask next question
    quiz.print_final_score()  # Print final score when quiz is completed

# Main entry point of the program
if __name__ == "__main__":
    # Create question bank from data
    question_bank = create_question_bank(question_data)

    # Create a QuizBrain instance with the question bank
    quiz = QuizBrain(question_bank)

    # Run the quiz
    run_quiz(quiz)

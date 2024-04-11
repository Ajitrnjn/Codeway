import random


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer the following questions to test your knowledge.")
        print("-----------------------------------------------------")

    def present_quiz_questions(self):
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}: {question['question']}")
            if 'choices' in question:
                for choice_num, choice in enumerate(question['choices'],
                                                    start=1):
                    print(f"{choice_num}. {choice}")
                user_answer = input("Your answer: ")
            else:
                user_answer = input("Your answer (fill in the blank): ")
            self.evaluate_user_answer(question, user_answer)

    def evaluate_user_answer(self, question, user_answer):
        if user_answer.lower() == question['answer'].lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {question['answer']}")

    def display_final_results(self):
        print("-----------------------------------------------------")
        print("Quiz Completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ")
        return play_again.lower() == "yes"

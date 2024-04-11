# Main function to run the quiz game
from QuizGame.question_answer import questions
from QuizGame.quiz_game import QuizGame


def main():
    game = QuizGame(questions)
    game.display_welcome_message()
    while True:
        game.present_quiz_questions()
        game.display_final_results()
        if not game.play_again():
            break


if __name__ == "__main__":
    main()

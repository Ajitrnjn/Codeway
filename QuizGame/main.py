# Main function to run the quiz game
from QuizGame.quiz_game import QuizGame


def main():
    game = QuizGame("./resource/questions.json")
    game.display_welcome_message()
    while True:
        game.present_quiz_questions()
        game.display_final_results()
        if not game.play_again():
            break


if __name__ == "__main__":
    main()

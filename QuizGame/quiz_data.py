# Sample quiz questions
import json


class QuizData:

    def __init__(self, file_path):
        self.file_path = file_path
        self.questions = []
        self.load_json_data()

    def load_json_data(self):
        try:
            with open(self.file_path, "r") as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{self.file_path}'.")

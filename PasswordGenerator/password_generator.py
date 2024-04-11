import random
import re


class PasswordGenerator:
    def __init__(self):
        self.lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.digits = '0123456789'
        self.special_character = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    def generate_password(self, length):
        # Define the pool of characters based on complexity
        complexity_regex = re.compile(r'[ludxs]+')
        complexity = input(
            "Enter password complexity (l - lowercase, u - uppercase, "
            "d - digits, x - special_character, s - similar characters): "
            "").lower()
        while not complexity_regex.match(complexity):
            print("Invalid input! Please enter a combination of l, u, d, x, "
                  "s.")
            complexity = input(
                "Enter password complexity (l - lowercase, u - uppercase, "
                "d - digits, x - special_character, s - similar characters): ").lower()

        temp = ''
        if 'l' in complexity:
            temp += self.lowercase_letters
        if 'u' in complexity:
            temp += self.uppercase_letters
        if 'd' in complexity:
            temp += self.digits
        if 'x' in complexity:
            temp += self.special_character
        if 's' in complexity:
            temp += 'il1Lo0O'

        # Generate password
        password = ''.join(random.choice(temp) for _ in range(length))
        return password

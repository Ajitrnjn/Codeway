from PasswordGenerator.password_generator import PasswordGenerator


def main():
    length = int(input("Enter the desired length of the password: "))
    while length <= 0:
        print("Please enter a positive length.")
        length = int(input("Enter the desired length of the password: "))

    generator = PasswordGenerator()
    password = generator.generate_password(length)
    print("Generated Password:", password)


if __name__ == "__main__":
    main()

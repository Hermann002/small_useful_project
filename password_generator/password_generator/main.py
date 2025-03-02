import random
import string
import os

class PasswordGenerator():
    def __init__(self, length=12, uppercase=True, lowercase=True, numbers=True, symbols=True, name=None):
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.symbols = symbols
        self.name = name

    def generate_password(self):
        characters = string.ascii_lowercase
        if self.uppercase:
            characters += string.ascii_uppercase
        if self.numbers:
            characters += string.digits
        if self.symbols:
            characters += string.punctuation

        return ''.join(random.choice(characters) for _ in range(self.length))
    
    def save_password(self, name, password):
        header = "| Nom | type | Mot de passe |\n|-----|-------------|-----------|"
        if not os.path.exists('passwords.md'):
            with open('passwords.md', 'w') as file:
                file.write(header)
        
        with open('passwords.md', 'a') as file:
            file.write(f"\n| {name}   | password  | {password}  |")

def get_valid_input(prompt, input_type, validation_func=None):
    while True:
        try:
            user_input = input_type(input(prompt))
            if validation_func and not validation_func(user_input):
                raise ValueError
            return user_input
        except ValueError:
            print("Entrée invalide. Veuillez réessayer.")

def main():
    name = str(input("Entrer le nom de la clé:"))
    length = get_valid_input("Entrer la longueur de la clé:", int, lambda x: x > 0)
    uppercase = get_valid_input("Contenir des majuscules? (o/n):", bool, lambda x: x in ['o', 'n'])
    numbers = get_valid_input("Contenir des chiffres? (o/n):", bool, lambda x: x in ['o', 'n'])
    symbols = get_valid_input("Contenir des symboles? (o/n):", bool, lambda x: x in ['o', 'n'])

    generator = PasswordGenerator(length, uppercase, numbers, symbols, name)
    password = generator.generate_password()
    generator.save_password(name, password)
    print(f"Clé générée: {password}")

if __name__ == "__main__":
    main()
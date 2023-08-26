import random

class MastermindAI:
    def __init__(self):
        self.possible_codes = self.generate_possible_codes()
        self.guesses = []
        self.current_guess = self.generate_random_code()

    def generate_possible_codes(self):
        codes = []
        for i in range(10000):
            code = str(i).zfill(4)
            if len(set(code)) == 4:
                codes.append(code)
        return codes

    def generate_random_code(self):
        return random.choice(self.possible_codes)

    def generate_next_guess(self, feedback):
        if not feedback:
            self.current_guess = '1122'  # Initial guess based on Knuth's algorithm
            return self.current_guess

        self.possible_codes = [code for code in self.possible_codes if self.evaluate_guess(self.current_guess, code) == feedback]

        if not self.possible_codes:
            print("No remaining possible codes. Ending the game.")
            return

        self.current_guess = random.choice(self.possible_codes)
        return self.current_guess

    def evaluate_guess(self, guess, code):
        exact_matches = 0
        color_matches = 0
        for i in range(len(guess)):
            if guess[i] == code[i]:
                exact_matches += 1
            elif guess[i] in code:
                color_matches += 1
        return exact_matches, color_matches

class MastermindGame:
    def __init__(self):
        self.secret_code = None
        self.ai = MastermindAI()

    def generate_secret_code(self):
        self.secret_code = self.ai.generate_random_code()

    def play(self):
        self.generate_secret_code()
        print("Welcome to Mastermind!")
        print("Guess the 4-digit secret code (digits range from 0 to 9).")
        print("Enter your guess in the format '1234'.")
        print("Use 'q' to quit the game.")
        num_guesses = 0

        while True:
            guess = input("Enter your guess: ")
            if guess.lower() == 'q':
                print("Quitting the game...")
                break

            num_guesses += 1
            exact_matches, color_matches = self.ai.evaluate_guess(guess, self.secret_code)

            if exact_matches == 4:
                print(f"Congratulations! You guessed the secret code '{self.secret_code}' in {num_guesses} guesses.")
                break

            print(f"Exact matches: {exact_matches}")
            print(f"Color matches: {color_matches}")

            ai_guess = self.ai.generate_next_guess((exact_matches, color_matches))
            print(f"AI guesses: {ai_guess}")

if __name__ == '__main__':
    game = MastermindGame()
    game.play()

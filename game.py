#!/usr/bin/env python3

class HangmanGame:

    def __init__(self, word):
        self.word = word
        self.max_errors = 6
        self.errors = 0
        self.guessed_letters = []
        self.wrong_letters = []

    def display_progress(self):
        resultado = []
        for letra in self.word:
            if letra in self.guessed_letters or not letra.isalpha():
                resultado.append(letra)
            else:
                resultado.append("_")
        return " ".join(resultado)

    def process_guess(self, letter):
        if not letter.isalpha():
            return False

        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors += 1
            self.wrong_letters.append(letter)
            return False


    def is_won(self):
        for letra in self.word:
            if letra.isalpha() and letra not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        return self.errors >= self.max_errors

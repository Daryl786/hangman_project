#!/usr/bin/env python3

class HangmanGame:

    def __init__(self, word):
        self.word = word
        self.max_errors = 6
        self.errors = 0
        self.guessed_letters = []

    def display_progress(self):
        resultado = []
        for letra in self.word:
            if letra in self.guessed_letters:
                resultado.append(letra)
            else:
                resultado.append("_")
        return " ".join(resultado)


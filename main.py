#!/usr/bin/env python3

from utils import get_random_word
from game import HangmanGame

palabra = get_random_word()
juego = HangmanGame(palabra)

print("----------------------------------------------")
print("Adivina la pelicula:")
print("----------------------------------------------")

def pedir_letra(juego):
    while True:

        letra = input("Ingrese una letra: ").strip().lower()
        if len(letra) != 1:
            print("ingrese solo una letra para continuar")
            continue
        if not letra.isalpha():
            print("ingrese una letra valida para continuar")
            continue
        if letra in juego.guessed_letters or letra in juego.wrong_letters:
            print("la letra ya fue probada")
            continue

        return letra

while True:
    letra = pedir_letra(juego)
    juego.process_guess(letra)

    letras_probadas = sorted(juego.guessed_letters + juego.wrong_letters)
    print(f"Letras probadas: {', '.join(letras_probadas)}")

    print(juego.display_progress())

    print(f"Vidas restantes: {juego.max_errors - juego.errors}")


    if juego.is_won():
        print("Ganasteeeeeeee")
        break

    if juego.is_lost():
        print("perdiste :(")
        break

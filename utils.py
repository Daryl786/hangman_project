#!/usr/bin/env python3
import random

def get_random_word():
    palabras =  []
    with open("wordlist.txt") as f:
        for palabra in f:
            limpia = palabra.strip()
            if limpia.isalpha():
                palabras.append(limpia)
            else:
                print("las palabras no son alfabeticas")

    return random.choice(palabras)


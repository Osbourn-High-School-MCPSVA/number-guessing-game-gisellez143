"""
Filename: <number_guessing_game.py>
Author: <Zavala, Giselle>
Created: <2/25/2026>
Instructor: Giselle
"""
from random import randint

num = randint(1,100)

print("Welcome to the numberb guessing game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("enter your guess: \n"))
    if guess < num:
        print("Too low! try again")
    elif guess > num:
        print("Too high! try again")
    else:
        print("Correct! you got the number! tanks for playing")
        break
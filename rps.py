from random import choice
from time import sleep
import os

options = ["Rock", "Paper", "Scissors"]
ai_score = 0
player_score = 0

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def menu():
    global ai_score, player_score
    print("Let's play ROCK, PAPER, SCISSORS")
    if player_score > 0 or ai_score > 0:
        print(f"Score Board: AI - {ai_score} || YOU - {player_score}")
    choice = None
    while choice not in options:
        choice = input("Choose one of the following: Rock, Paper, Scissors\n> ").title().strip()
    return choice


def play():
    global ai_score, player_score
    playing_game = True
    while playing_game:
        player_choice = menu()
        ai_choice = choice(options)
        
        print("ROCK")
        sleep(1)
        print("PAPER")
        sleep(1)
        print("SCISSORS")
        sleep(1)
        print("SHOOT")
        sleep(1)

        print(f"AI Choice: {ai_choice}")
        print(f"Your Choice: {player_choice}")
        sleep(1)
        if ai_choice == "Rock" and player_choice == "Paper":
            print("Paper covers Rock... You Win!!")
            player_score += 1
        elif ai_choice == "Scissors" and player_choice == "Rock":
            print("Rock smashes Scissors... You Win!!")
            player_score += 1
        elif ai_choice == "Paper" and player_choice == "Scissors":
            print("Scissors cut Paper... You Win!!")
            player_score += 1
        elif player_choice == "Rock" and ai_choice == "Paper":
            print("Paper covers Rock... You Lose!!")
            ai_score += 1
        elif player_choice == "Scissors" and ai_choice == "Rock":
            print("Rock smashes Scissors... You Lose!!")
            ai_score += 1
        elif player_choice == "Paper" and ai_choice == "Scissors":
            print("Scissors cut Paper... You Lose!!")
            ai_score += 1
        else:
            print(f"You both chose: {ai_choice}. Tie Game!")

        play_again = input('Press "Y" to play again. Any key to quit. ').lower()
        if play_again == "y":
            playing_game = True
            clear()
        else:
            print("Thanks for playing... Exiting game.")
            playing_game = False

play()
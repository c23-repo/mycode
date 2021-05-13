#!/usr/bin/env python3
from random import choice

round_count = 0
answer_count = 0

question_list = ["Why does it get dark?", "Why do I have to sleep?", "Why do old people move slow?",
                 "Why are you so tall?",
                 "Why do dogs smell other dogs butt\'s?"]

response_list = ["ask your mom", "ask your dad", "i don\'t know", "want to play a game?", "cuz i said so"]


def intro_print():
    print("\nThis simulation will accurately measure your rating as a parent. Answer as many as you can to get a\n"
          "higher score. There are key phrases that allow you end the game early, punctuation matters. Let's begin\n"
          "\tScenario: A 3 year old comes up to you\n"
          "\t\t        MMMMMMM   \n"
          "\t\t       / __  __\\ \n"
          "\t\t     (|  0   0  |)\n"
          "\t\t      |    V    | \n"
          "\t\t      \\   ====  /\n"
          "\t\t       \\_______/ \n"
          "\t\t          |  |    \n"
          "\t\t     /------------\\\n"
          "and asks you a question that they sincerely want to know more on. How do you reply...\n")


def score_rating(rounds, answers):
    if answers == 0 and rounds == 100:
        print("You should probably go to an Audiologist!!!!")
    elif answers >= 90 and rounds >= 90:
        print("You should teach a class on patience")
    elif answers >= 50 and rounds >= 50:
        print("You care about your children's development")
    elif answers >= 20 and rounds >= 20:
        print("Standard parent skills...")
    elif answers >= 10 and rounds >= 10:
        print("No nonsense parent, kids might be scared of you.")
    else:
        print("Your an aunt or uncle, reconsider having kids if you want them.")


def ask_questions():
    intro_print()
    global round_count, answer_count
    while round_count < 100:
        if round_count == 0:
            answer = input(choice(question_list) + ': ').lower()
            if answer in response_list:
                print("OK!")
                break
            else:
                if answer != "":
                    answer_count += 1
                round_count += 1
        elif round_count != 0:
            answer = input('But why? ').lower()
            if answer in response_list:
                print("OK!")
                break
            elif answer == "":
                round_count += 1
            else:
                answer_count += 1
                round_count += 1
    score_rating(round_count, answer_count)


ask_questions()


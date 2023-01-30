"""
Made by - Aditya mangal
Purpose - Python mini project
Date  - 18 october 2020
"""
import re
from nltk.util import pr
from termcolor import cprint, colored
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import text2emotion as te
import time

chatbot = ChatBot("Bot")
trainer = ChatterBotCorpusTrainer(chatbot)
available = "\nAvailable languages >> \nbengali, chinese, english, french, german, hebrew, hindi, indonesian, italian,japanese, korean, marathi,\n oriya, persian, portuguese, russian, spanish, swedish, telugu, thai, traditionalchinese, turkish"
print(colored(available, "yellow"))
while True:
    language = input(
        "\n\nIn which language do you want to start the conversation ? >> "
    ).lower()
    if language in available:
        break
    else:
        print(
            f"Sorry {language} language is not available,\n please select from the above list."
        )
trainer.train(f"chatterbot.corpus.{language}")


def get_emoji(query):
    emotion = te.get_emotion(query)
    # taking list of emotion values in v
    v = list(emotion.values())
    # taking list of emotion keys in v
    k = list(emotion.keys())

    emotion = k[v.index(max(v))]  # Getting user's emotion

    emotion_dict = {
        "Happy": "😊",
        "Angry": "😠",
        "Surprise": "😯",
        "Sad": "😟",
        "Fear": "😨",
    }
    emoji = emotion_dict.get(f"{emotion}")  # Getting emoji of the emotion

    return emoji


if __name__ == "__main__":

    cprint("#" * 80, "magenta")
    cprint(
        (f"     \             ___| |             |    |             |   ").center(50),
        "yellow",
    )
    cprint(
        (f"    _ \           |     __ \    _` |  __|  __ \    _ \   __| ").center(50),
        "yellow",
    )
    cprint(
        (f"   ___ \  _____|  |     | | |  (   |  |    |   |  (   |  |   ").center(50),
        "yellow",
    )
    cprint(
        (f" _/    _\        \____|_| |_| \__._| \__| _.__/  \___/  \__| ").center(50),
        "yellow",
    )
    cprint("#" * 80, "magenta")

    print("You can exit by typing exit or bye\n")
    name = input("Enter your name:")
    cprint((f"Start Chatting").center(20), "yellow")
    print()

    while True:
        query = input(colored(f"    {name}>> ", "red"))
        if "exit" in query.lower() or "bye" in query.lower():
            print(colored("Bot>> Bye :) See you soon.....", "green"))
            exit()
        else:
            if language.lower() == "english":
                emoji = get_emoji(query)
                print(
                    colored(f"Bot>> {chatbot.get_response(query)} [{emoji} ]", "green")
                )
            else:
                print(colored(f"Bot>> {chatbot.get_response(query)}", "green"))

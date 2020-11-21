import random


def get_random_word():
    with open("dico.txt", "r", encoding="UTF-8") as file:
        word_list = file.read().splitlines()
        return random.choice(word_list)


def get_letter(char_list, current_word):
    count = 0
    char_already_said_list = []

    while char_list != current_word:
        if count == 6:
            to_print = ""
            for i in range(len(char_list)):
                to_print += char_list[i]
            print("Tu as perdu, le mot était " + to_print)
            return
        input_letter = input("Proposez une lettre : ").upper()
        if input_letter in char_already_said_list:
            print("Tu as déjà entré cette lettre")
        elif input_letter not in char_list:
            print("Cette lettre est incorrect")
            print(get_draw(count))
            count += 1
        elif input_letter in char_list:
            print("Cette lettre est correct")
            index = char_list.index(input_letter)
            current_word[index] = input_letter
        char_already_said_list.append(input_letter)
        to_print = ""
        for i in range(len(current_word)):
            to_print += current_word[i]
        print(to_print)
    return "Tu as gagné"


def get_draw(nb):
    tab = [
        """
           +-------+
           |       |
           |       O
           |
           |
           |
        ==============
        """
        ,
        """
           +-------+
           |       |
           |       O
           |       |
           |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |      -|
           |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |      -|-
           |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |      -|-
           |      |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |      -|-
           |      | |
           |
        ==============
        """
    ]
    return tab[nb]


def main():
    word = get_random_word()
    char_list = list(word)
    current_word = []

    for i in range(len(word)):
        current_word.append("_")

    string = ""
    for i in range(len(current_word)):
        string += current_word[i]
    print(string)

    get_letter(word, current_word)


main()

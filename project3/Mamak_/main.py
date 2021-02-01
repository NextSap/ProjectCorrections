import random


def get_random_word():
    words = []
    with open('words.txt', 'r') as file:
        for word in file:
            words.append(word.replace('\n', ''))
    selection = random.choice(words)
    return selection  # OK


def get_result(word, userinput):
    result = bool(False)
    array = list(word)
    save = []
    tool = 0
    for loop in array:
        if userinput == loop:
            result = bool(True)
            save.append(tool)
        tool += 1
    print(result, save)
    return result, save  # OK


def get_draw(draw):
    tab = [
        """
           +-------+
           |
           |
           |
           |
           |
        ==============
        """,
        """
           +-------+
           |   	|
           |   	O
           |
           |
           |
        ==============
        """
        ,
        """
           +-------+
           |   	|
           |   	O
           |   	|
           |
           |
        ==============
        """,
        """
           +-------+
           |   	|
           |   	O
           |  	-|
           |
           |
        ==============
        """,
        """
           +-------+
           |   	|
           |   	O
           |  	-|-
           |
           |
        ==============
        """,
        """
           +-------+
           |   	|
           |   	O
           |  	-|-
           |  	|
           |
        ==============
        """,
        """
           +-------+
           |   	|
           |   	O
           |  	-|-
           |  	| |
           |
        ==============
        """
    ]
    return tab[draw]


def cheating_check(user_responses, user_input, word):
    for check in user_responses:
        if user_input == check:
            result = get_result(word, user_input)[0]
            if result:
                print("Vous avez déjà rentré cette lettre, de plus, cette réponse était correcte.")
            else:
                print("Vous avez déjà rentré cette lettre, de plus, cette réponse était incorrecte.")
            cheating = bool(True)
        else:
            cheating = bool(False)
        return cheating


def ask_for_a_letter(user_responses, word):
    user_input = input("Veuillez entrer une lettre: ").upper()

    cheating = cheating_check(user_responses, user_input, word)
    if cheating == bool(False):
        user_responses.append(user_input)
    return get_result(word, user_input)[0], user_input


def replace(word, letter, index):  # Méthode qui permet de remplacer un '_' dans un word par la letter à l'index + affiche le résultat
    return ""


def main():
    draw = 0
    user_responses = []
    word = get_random_word()
    length = len(word)
    current_word = "_"

    print(word)

    while len(current_word) < length:
        current_word += "_"

    while current_word != word:
        if draw == 6:
            print("Vous avez perdu")
            return
        response = ask_for_a_letter(user_responses, word)
        if response[0]:
            print("Vous avez rentré la lettre " + response[1] + " et vous aviez raison !")
            # replace(....)
        else:
            get_draw(draw)
            print("La lettre " + response[1] + " est incorrecte, essayez encore.")


main()

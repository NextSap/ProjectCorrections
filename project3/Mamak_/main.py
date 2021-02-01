import random


def select():
    words = []
    with open('words.txt', 'r') as file:
        for word in file:
            words.append(word.replace('\n', ''))
    selection = random.choice(words)
    return selection  # ok


def boolean(word, userinput):
    result = bool(False)
    array = list(word)
    save = []
    tool = 0
    for loop in array:
        if userinput == loop:
            result = bool(True)
            save.append(tool)
    tool = tool + 1
    return result, save  # give le résultat, ok


def dessinPendu(draw):
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


def cheatingcheck(userresponses, userinput, word):
    for check in userresponses:
        finalcheck = bool(False)
    if userinput == check:
        result = boolean(word, userinput)
        if result == bool(True):
            print("Vous avez déjà rentré cette lettre, de plus, cette réponse était correcte.")
        cheating = bool(True)
        else:
        print("Vous avez déjà rentré cette lettre, de plus, cette réponse était incorrecte.")
        cheating = bool(True)
    else:
        finalcheck = bool(False)
        cheating = bool(False)
    return cheating


def main():
    draw = 0
    userresponses = []
    word = select()
    lenght = len(word)
    find = "-"
    while len(find) < lenght:
        find = find + "-"
    print(word + "\n" + find)
    userinput = input("Veuillez entrer une lettre: ")
    userinput = userinput.upper
    userinput = str(userinput)
    cheating = cheatingcheck(userresponses, userinput, word)
    if cheating == bool(False):
        userresponses.append(userinput)
    result = boolean(word, userinput)[0]
    if result == True:
        print("Vous avez rentré la lettre " + userinput + " et vous aviez raison !")
    else:
        draw = draw + 1
        print("La lettre " + userinput + " est incorrecte, essayez encore.")

main()
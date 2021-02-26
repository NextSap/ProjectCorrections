import random


def get_random_word():
    words = []
    with open('words.txt', 'r') as file:
        for word in file:
            words.append(word.replace('\n', ''))
    selection = random.choice(words)
    return selection  # OK
def get_result(word, user_input):
    result = bool(False)
    array = list(word)
    save = []
    tool = 0
    for loop in array:
        if user_input == loop:
            result = bool(True)
            save.append(tool)
        tool += 1
    print(result, save)
    return result, save  # OK
def get_draw(draw):
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
    return tab[draw]


def cheating_check(user_responses, user_input, word):
    if user_input in user_responses:
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
    return get_result(word, user_input), user_input, user_responses, cheating


# Méthode qui permet de remplacer un '_' dans un word par la letter à l'index + affiche le résultat
def replace(letter, index, current_word):
    final_word = ""
    return final_word


def main():
    draw = 0
    get_draw(draw)
    user_responses = []
    word = get_random_word()
    length = len(word)
    current_word = "_"
    print(word)  # debug
    while len(current_word) < length:
        current_word += "_"
    while current_word != word:
        if draw == 6:
            print("Vous avez perdu")
            return
        response = ask_for_a_letter(user_responses, word)
        user_responses = response[2]
        cheating = response[3]
        if response[0][0]:
            print("Vous avez rentré la lettre " + response[1] + " et vous aviez raison !")
            for i in response[0][1]:
                current_word = replace(response[1], i, current_word)
        else:
            if not cheating:
                print(get_draw(draw))
                print("La lettre " + response[1] + " est incorrecte, essayez encore.")
                draw += 1
# replace("COUCOU", "O", (2, 5), "C_U__U")
main()

# Globalement, le programme fonctionne : Il sait quand la lettre fait partie du mot et il sait quand elle ne fait pas
# partie du mot. Le seul problème c'est que tu t'es trop compliqué la vie pour la fonction replace()
# La fonction replace() doit faire dans l'ordre :
#   -> transformer le current_word en une liste de caractère de sorte à ce que "WORD" devienne ["W","O","R","D"]
#   -> remplacer dans ce tableau grâce à l'index et à la lettre donné
#   -> retourner ce même tableau en string
#   -> attention à pas oublier d'inclure le système qui permet de print le mot
# ! ATTENTION ! j'ai remplacé le nom du fichier à la ligne 6 donc ce sera sûrement ta première erreur si tu lances le
# programme

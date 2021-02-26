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
            print("⚠ Vous avez déjà rentré cette lettre, de plus, cette réponse était correcte.")
        else:
            print("⚠ Vous avez déjà rentré cette lettre, de plus, cette réponse était incorrecte.")
        cheating = bool(True)
    else:
        cheating = bool(False)
    return cheating


def ask_for_a_letter(user_responses, word):
    user_input = input("➜ Veuillez entrer une lettre: ").upper()

    cheating = cheating_check(user_responses, user_input, word)
    if cheating == bool(False):
        user_responses.append(user_input)
    return get_result(word, user_input), user_input, user_responses, cheating

def replace(letter, index, current_word):
    word_array=list(current_word)
    word_array[index]=letter
    final_word=""
    for char in word_array:
        final_word=final_word+str(char)
    return final_word


def main():
    draw = 0
    get_draw(draw)
    user_responses = []
    word = get_random_word()
    length = len(word)
    current_word = "-"
    while len(current_word) < length:
        current_word += "-"
    print(current_word)
    while current_word != word:
        if draw == 6:
            print("\n➜ Partie terminée ! Vous avez perdu !")
            print("➜ Le mot attendu était: "+word)
            return
        response = ask_for_a_letter(user_responses, word)
        user_responses = response[2]
        cheating = response[3]
        if response[0][0]:
            for i in response[0][1]:
                current_word = replace(response[1], i, current_word)
            if cheating==False:
                print("✓ Vous avez rentré la lettre " + response[1] + " et vous aviez raison !")
                print(current_word)
        else:
            if not cheating:
                print(get_draw(draw))
                print("✗ La lettre " + response[1] + " est incorrecte, essayez encore.")
                print("➜ Nous recherchons le mot: "+ current_word)
                draw += 1
main()

import random


def load_questions():
    with open('qcm.txt', 'r', encoding="UTF-8") as file:
        return file.read().splitlines()


def main():
    lines = load_questions()
    rounds = 10
    score = 0
    for i in range(rounds):
        current_lines = random.choice(lines)
        lines.remove(current_lines)
        current_questions = current_lines.split(";;")[0]
        current_response = current_lines.split(";;")[1]
        current_entrance = input("Question " + str(i + 1) + ": " + current_questions + "\nVotre réponse: ").upper()
        if current_entrance == current_response:
            score += 1
            print("Bonne réponse ! Vous remportez un point. Question suivante.\n")
        else:
            print("Mauvaise réponse ! Le bonne réponse était la réponse" + current_response + ". Question suivante.\n")
    print("Le QCM est terminé. Vous avez obtenu la note de " + str(score) + "/" + str(rounds) + ".")


main()

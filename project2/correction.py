import random
import re


def pickQuestions():
    with open("project2/qcm.txt", "r", encoding="UTF-8") as file:
        return file.read().splitlines()


def main(rounds):
    questions_list = pickQuestions()
    score = 0
    for i in range(rounds):
        question = random.choice(questions_list)
        questions_list.remove(question)

        current_question = question.split("A-")[0]
        current_choices_list = re.split("( [A-Z]-)", question.split(";;")[0])
        current_choices_list.pop(0)
        current_response = question.split(";;")[1]

        print("Question " + str(i + 1) + ": " + current_question)
        for i in range(len(current_choices_list)):
            if i % 2 == 0:
                print(current_choices_list[i].replace("-", ". ") + current_choices_list[i + 1])

        if input().upper() == current_response:
            print("Vrai ! C'est la bonne réponse" + "\n\n")
            score += 1
        else:
            print("Faux ! La bonne réponse était la " + current_response + "\n\n")

    print("Votre score est de " + str(score) + "/" + str(rounds))
    if score < 5:
        print("Tu es en échec! Tu feras mieux la prochaine fois.")
    else:
        print("Très bien, tu as réussi le test!\n")
    response = input("Veux-tu recommencer le test ? (O/N) ")
    if response == "O":
        print("\n\n\n")
        main(10)
    else:
        exit()


main(10)

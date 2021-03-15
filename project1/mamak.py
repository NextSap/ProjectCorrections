def search():
    success = 0
    search = input("Entrez un nom:")
    with open('datauser.txt', 'r') as datas:
        for n in datas:
            datas = n.split()
            if search == datas[0]:
                print (datas[0] + ": " + datas[1])
                success = success + 1
        if success == 0:
            return "Inconnu"
    menu()


def write():
    name = input("Nom (0 pour quitter):")
    if name == "0":
        menu()
    else:
        phone_number = input("Téléphone:")
        with open('datauser.txt', 'a') as f:
            f.write(name + " " + phone_number + "\n")
    menu()


def menu():
    choice = input(
        "Menu principal:\n0 - Quitter\n1 - Ecrire dans le  répertoire\n2 - Rechercher dans le répertoire\nVotre choix ?")
    if choice == "1":
        write()
    else:
        if choice == "2":
            search()
        else:
            if choice == "0":
                print("Arrêt")
            else:
                print("Valeur incorrecte")
                menu()


menu()
def write():
    repertory_w = open("repertory.txt", "a")
    repertory_r = open("repertory.txt", "r").read()

    print("\n   > Création d'une nouvelle fiche : ")
    name = input("Nom : ")
    cellphone_number = input("Numéro de téléphone : ")

    if name in repertory_r:
        print("\nErreur: Ce nom est déjà inscrit dans le répertoire.")
        main()
    if cellphone_number in repertory_r:
        print("\nErreur: Ce numéro est déjà inscrit dans le répertoire.")
        main()

    repertory_w.write("[" + name + ":" + cellphone_number + "]")
    repertory_w.close()
    print("Succès. Vous avez créé une nouvelle fiche.")
    print("\n\n")
    request()


def writeWithName(name):
    repertory_w = open("repertory.txt", "a")
    repertory_r = open("repertory.txt", "r").read()

    print("\n   > Création d'une nouvelle fiche : ")
    print("Nom : " + name)
    cellphone_number = input("Numéro de téléphone : ")

    if name in repertory_r:
        print("\nErreur: Ce nom est déjà inscrit dans le répertoire.")
        main()
    if cellphone_number in repertory_r:
        print("\nErreur: Ce numéro est déjà inscrit dans le répertoire.")
        main()

    repertory_w.write("[" + name + ":" + cellphone_number + "]")
    repertory_w.close()
    print("Succès. Vous avez créé une nouvelle fiche.")
    print("\n\n")
    request()


def writeWithNumber(cellphone_number):
    repertory_w = open("repertory.txt", "a")
    repertory_r = open("repertory.txt", "r").read()

    print("\n   > Création d'une nouvelle fiche : ")
    name = input("Nom : ")
    print("Numéro de téléphone : " + cellphone_number)

    if name in repertory_r:
        print("\nErreur: Ce nom est déjà inscrit dans le répertoire.")
        main()
    if cellphone_number in repertory_r:
        print("\nErreur: Ce numéro est déjà inscrit dans le répertoire.")
        main()

    repertory_w.write("[" + name + ":" + cellphone_number + "]")
    repertory_w.close()
    print("Succès. Vous avez créé une nouvelle fiche.")
    print("\n\n")
    request()


def search():
    repertory_r = open("repertory.txt", "r", encoding="UTF-8").read()

    response = input("""
   > Rechercher par : (1) Nom \n
                      (2) Numéro de téléphone
            ---> """)
    if response == "1":
        name = input("Entrez un nom : ")
        if name not in repertory_r:
            current_response = input(
                "Pas de résultat trouvé.\nVoulez-vous créer une nouvelle fiche avec le nom " + name + "? (O/N)\n---> ")
            if current_response == "O":
                writeWithName(name)
            else:
                print("\n\n")
                request()
        else:
            current_name = name
            current_cellphone_number = repertory_r.split(name + ":")[1].split("]")[0]
            print("Résultat de la recherche :\n   > Nom : " + current_name + "\n   > Numéro de téléphone : "
                  + current_cellphone_number + "\n\n")
            request()
    elif response == "2":
        cellphone_number = input("Entrez un numéro de téléphone : ")
        if cellphone_number not in repertory_r:
            current_response = input(
                "Pas de résultat trouvé.\nVoulez-vous créer une nouvelle fiche avec le numéro " + cellphone_number +
                "? (O/N)\n---> ")
            if current_response == "O":
                writeWithNumber(cellphone_number)
            else:
                print("\n\n")
                request()
        else:
            current_name = repertory_r.split(":" + cellphone_number + "]")[0].split("[")[1]
            current_cellphone_number = cellphone_number
            print("Résultat de la recherche :\n   > Nom : " + current_name + "\n   > Numéro de téléphone : "
                  + current_cellphone_number + "\n\n")
            request()
    else:
        request()


def main():
    print(
        """
    * * * * * * * * * * * * * * * * * * * * * * * * * * *
    *                                                   *
    *  R E P E R T O I R E     T E L E P H O N I Q U E  *
    *                                                   *
    * * * * * * * * * * * * * * * * * * * * * * * * * * *
        
        """)
    request()


def request():
    response = input("1 - Créer une nouvelle fiche\n2 - Rechercher une fiche\n0 - Quitter\n\n---> ")
    if response == "1":
        write()
    elif response == "2":
        search()
    else:
        quit()


main()

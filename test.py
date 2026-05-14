## input des écurie dans le genre de menu
    #Analyse.circuit_plus_longtemps(gestion)
    lst_ecurie = []
    liste_nom = []
    #choisir l'écurie
    for ecurie in gestion.lst_ecuries:
        if ecurie.nom not in liste_nom:
            lst_ecurie.append(ecurie)
            liste_nom.append(ecurie.nom)

    index = 0
    for team in lst_ecurie:
        print(f"{index}. {team.nom}")
        index += 1
    try:
        print()
        ecurie_int = int(input("Entrez le numéro de l'écurie voulu: "))
        ecurie_str = lst_ecurie[ecurie_int]

    except:
        print("Choix du circuit out of range")


            
    #input des pilotes
    #choisir le pilote
    lst_pilote = []
    liste_nom = []

    for pilote in gestion.lst_pilotes:
            
        if pilote.driver_id not in liste_nom:
            lst_pilote.append(pilote)
            liste_nom.append(pilote.driver_id)

    index = 0
    for driver in lst_pilote:
        print(f"{index}. {driver.prenom}  {driver.nom}")
        index += 1
    try:
        print()
        pilote_int = int(input("Entrez le numéro du pilote voulu: "))
        pilote_str = lst_pilote[pilote_int]

    except:
        print("Choix du circuit out of range")

    print(Analyse.plus_de_podium(gestion, pilote_str))

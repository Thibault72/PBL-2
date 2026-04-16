def verification(avion):
    # Récupère le nombre total d'avions dans la liste
    n = len(avion)
    
    # Liste pour stocker tous les IDs afin de vérifier les doublons
    ids = []

    # Parcourt chaque avion (dictionnaire) dans la liste
    for i in avion:
        # Compteur du nombre de clés trouvées
        list_k = 0
        
        # Compteur du nombre de valeurs correctes (bon type)
        list_v = 0

        # Parcourt chaque paire clé/valeur du dictionnaire avion
        for key, value in i.items():

            # Vérifie la clé "fuel"
            if key == "fuel":
                list_k += 1  # Compte la clé
                if type(value) == int:  # Vérifie que la valeur est un entier
                    list_v += 1
                else:
                    print(f"Error of value plane {i}, for {key}")

            # Vérifie la clé "diplomatic_level"
            if key == "diplomatic_level":
                list_k += 1
                if type(value) == int:
                    list_v += 1
                else:
                    print(f"Error of value plane {i}, for {key}")

            # Vérifie la clé "id"
            if key == "id":
                ids.append(value)  # Ajoute l'id à la liste pour vérifier les doublons
                list_k += 1
                if type(value) == str:  # L'id doit être une chaîne de caractères
                    list_v += 1
                else:
                    print(f"Error of value plane {i}, for {key}")

            # Vérifie la clé "medical"
            if key == "medical":
                list_k += 1
                if type(value) == bool:  # Doit être un booléen
                    list_v += 1
                else:
                    print(f"Error of value plane {i}, for {key}")

            # Vérifie la clé "technical_issue"
            if key == "technical_issue":
                list_k += 1
                if type(value) == bool:
                    list_v += 1
                else:
                    print(f"Error of value plane {i}, for {key}")

            # Vérifie la clé "arrival_time"
            if key == "arrival_time":
                list_k += 1
                if type(value) == float:  # Doit être un float
                    list_v += 1
                else:
                    print(f"Error of value plane {i}, for {key}")

        # Vérifie que toutes les 6 clés sont présentes
        if list_k != 6:
            print(f"Error from key, plane {i} : miss one key")
            return False

        # Vérifie que toutes les valeurs sont du bon type
        if list_v != 6:
            print(f"Error from value, plane {i} : wrong value type")
            return False

    # Vérifie qu'il n'y a pas deux avions avec le même id
    for k in range(n):
        for j in range(k + 1, n):
            if ids[j] == ids[k]:
                print(f"Two planes have the same id ({ids[j]})")
                return False

    # Si tout est correct, retourne True
    return True
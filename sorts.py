# Sorting functions used to determine the landing order of aircraft.
# Two quadratic sorting algorithms are implemented:
# - Insertion sort
# - Selection sort
# Both algorithms use a policy function that compares two aircraft and decides
# which one has priority.

# Importe le module priority qui contient la fonction de comparaison
import priority


def insertion_sort(aircraft_list, policy):
    # Copie chaque avion pour éviter de modifier la liste originale
    aircraft_list = [plane.copy() for plane in aircraft_list]
    
    # Nombre d'avions
    n = len(aircraft_list)

    # Parcourt la liste à partir du deuxième élément
    for i in range(1, n):
        # Avion à insérer à la bonne position
        current_aircraft = aircraft_list[i]
        j = i - 1

        # Décale les éléments tant que l'avion courant est prioritaire
        while j >= 0 and priority.Priority(policy, current_aircraft, aircraft_list[j], n):
            aircraft_list[j + 1] = aircraft_list[j]
            j -= 1

        # Insère l'avion à sa position correcte
        aircraft_list[j + 1] = current_aircraft

    # Retourne la liste triée
    return aircraft_list


def selection_sort(aircraft_list, policy):
    # Copie chaque avion pour éviter de modifier la liste originale
    aircraft_list = [plane.copy() for plane in aircraft_list]
    
    # Nombre d'avions
    n = len(aircraft_list)

    # Parcourt toute la liste sauf le dernier élément
    for i in range(n - 1):
        # Index de l'avion prioritaire dans la partie non triée
        priority_index = i

        # Recherche de l'avion le plus prioritaire
        for j in range(i + 1, n):
            if priority.Priority(policy, aircraft_list[j], aircraft_list[priority_index], n):
                priority_index = j

        # Échange des positions
        aircraft_list[i], aircraft_list[priority_index] = aircraft_list[priority_index], aircraft_list[i]

    # Retourne la liste triée
    return aircraft_list


def simulate_landings(sorted_aircraft):
    # Copie des avions en attente
    waiting_planes = [plane.copy() for plane in sorted_aircraft]
    
    # Liste des avions ayant atterri
    landed_planes = []
    
    # Liste des avions crashés
    crashed_planes = []

    # Tant qu'il reste des avions en attente
    while waiting_planes:
        # L'avion prioritaire (premier de la liste) atterrit
        current_plane = waiting_planes.pop(0)
        landed_planes.append(current_plane)

        # Les autres avions perdent 1 unité de carburant
        survivors = []
        for plane in waiting_planes:
            plane["fuel"] -= 1  # Consommation de carburant
            
            # Si le carburant est épuisé → crash
            if plane["fuel"] <= 0:
                crashed_planes.append(plane)
            else:
                survivors.append(plane)

        # Met à jour la liste des avions encore en attente
        waiting_planes = survivors

    # Retourne :
    # - la liste des avions ayant atterri
    # - le nombre de crashs
    # - la liste des avions crashés
    return landed_planes, len(crashed_planes), crashed_planes


def sort_aircraft(aircraft_list, policy, method="insertion"):
    # Choix de la méthode de tri
    if method == "insertion":
        sorted_planes = insertion_sort(aircraft_list, policy)
    elif method == "selection":
        sorted_planes = selection_sort(aircraft_list, policy)
    else:
        # Erreur si méthode inconnue
        raise ValueError("Unknown sorting method")

    # Lance la simulation des atterrissages avec la liste triée
    return simulate_landings(sorted_planes)
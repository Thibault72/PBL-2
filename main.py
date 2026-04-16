# Importe le module de génération du trafic aérien
import traffic_generator

# Importe les fonctions utilitaires (affichage, filtres, etc.)
import Fonction_utilitaires

# Importe la fonction de vérification des données
import verification_key

# Importe les fonctions de tri et de simulation
import sorts

# Choix de la méthode de tri utilisée
methods = "selection"
# "insertion" or "selection"



def Main(crisis, number_of_planes, Plane = None):
    # Si une liste d'avions est fournie en paramètre, on l'utilise directement
    if Plane != None:
        planes = Plane
    else:
        # Sinon, on génère automatiquement les avions selon le scénario et le nombre demandé
        planes = traffic_generator.generate_traffic(crisis, number_of_planes)

    # Vérifie que les données des avions sont valides
    if not verification_key.verification(planes):
        print("Error in the data, please check the planes' information.")
        # Affiche les avions pour aider à repérer l'erreur
        Fonction_utilitaires.afficher_avions(planes)
        return
    
    # Trie les avions selon la politique choisie puis simule les atterrissages
    sorted_planes, crash, planes_crash = sorts.sort_aircraft(planes, crisis, methods)
    
    # Affiche les avions qui se sont crashés
    print(f"Planes that crashed: ")
    Fonction_utilitaires.afficher_avions(planes_crash)
    
    # Affiche les avions qui ont réussi à atterrir
    print(f"Planes that landed: ")
    Fonction_utilitaires.afficher_avions(sorted_planes)
    
    # Affiche le nombre total d'avions crashés
    print(f"Number of planes that crashed: {crash}")

# Lance le programme principal avec le scénario normal et 100 avions
Main("normal", 100)
# "fuel_crisis", "medical_crisis", "diplomatic_summit", "normal"
import random
# Importe la fonction afficher_avions depuis le module Fonction_utilitaires
from Fonction_utilitaires import afficher_avions

def generate_traffic(scenario, n):
    # Vérifie que le scénario est valide
    if scenario not in ["normal","fuel_crisis","medical_crisis","diplomatic_summit"]:
        raise ValueError("unknown scenario")

    # Liste qui contiendra tous les avions générés
    planes = []
    
    # Liste pour stocker les IDs déjà utilisés (éviter les doublons)
    used_ids = []

    # Boucle pour générer n avions
    for i in range(n):

        # Génération d’un ID unique
        while True:
            # Génère deux lettres majuscules (ASCII 65 à 90)
            letter1 = chr(random.randint(65,90))
            letter2 = chr(random.randint(65,90))
            
            # Génère un nombre entre 100 et 999
            number = random.randint(100,999)

            # Construit l'ID de l'avion (ex : AB123)
            plane_id = letter1 + letter2 + str(number)

            # Vérifie que l'ID n'a pas déjà été utilisé
            if plane_id not in used_ids:
                used_ids.append(plane_id)
                break  # Sort de la boucle une fois un ID unique trouvé

        # Création du dictionnaire représentant un avion
        plane = {
            "id": plane_id,
            # Niveau de carburant dépendant de n (avec variation)
            "fuel": random.randint(int(0.3*n), int(n*1.2)),
            "medical": False,  # Par défaut pas d'urgence médicale
            "diplomatic_level": random.randint(1,5),  # Niveau diplomatique entre 1 et 5
            "technical_issue": False,  # Pas de problème technique par défaut
            # Heure d'arrivée progressive (incrémentée légèrement)
            "arrival_time": round(19.4 + i * 0.01, 2)
        }

        # Ajustements selon le scénario choisi

        # Scénario de crise de carburant → carburant faible
        if scenario == "fuel_crisis":
            plane["fuel"] = random.randint(3,100)

        # Scénario de crise médicale → certains avions ont une urgence
        elif scenario == "medical_crisis":
            if random.random() < 0.3:  # 30% de probabilité
                plane["medical"] = True

        # Sommet diplomatique → niveau diplomatique plus élevé
        elif scenario == "diplomatic_summit":
            plane["diplomatic_level"] = random.randint(2,5)

        # Ajoute l'avion à la liste finale
        planes.append(plane)

    # Retourne la liste des avions générés
    return planes
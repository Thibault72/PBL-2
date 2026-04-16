def Priority(crisis_type, plane1, plane2, n):

    # Cas prioritaire global : carburant très faible (< 20% de n)
    # Si plane1 est en situation critique et pas plane2 → priorité à plane1
    if plane1["fuel"] < n*0.2 and plane2["fuel"] >= n*0.2:
        return plane1["fuel"] < plane2["fuel"]

    # Scénario : crise de carburant
    if crisis_type == "fuel_crisis":
        # Priorité absolue aux avions avec moins de 5 de fuel
        if plane1["fuel"] < 5 and plane2["fuel"] >= 5:
            return True
        if plane2["fuel"] < 5 and plane1["fuel"] >= 5:
            return False
        # Sinon, priorité à celui qui a le moins de fuel
        return plane1["fuel"] < plane2["fuel"]


    # Scénario : crise médicale
    if crisis_type == "medical_crisis":
        # Priorité aux avions avec urgence médicale
        if plane1["medical"] != plane2["medical"]:
            return plane1["medical"]
        # Ensuite priorité au carburant le plus faible
        if plane1["fuel"] != plane2["fuel"]:
            return plane1["fuel"] < plane2["fuel"]
        # Si égalité, compare encore le carburant (redondant mais explicite)
        return plane1["fuel"] < plane2["fuel"]


    # Scénario : sommet diplomatique
    if crisis_type == "diplomatic_summit":
        # Priorité au niveau diplomatique le plus élevé
        if plane1["diplomatic_level"] != plane2["diplomatic_level"]:
            return plane1["diplomatic_level"] > plane2["diplomatic_level"]
        # En cas d'égalité, priorité au carburant le plus faible
        return plane1["fuel"] < plane2["fuel"]


    # Cas général (scénario "normal")

    # Priorité aux urgences médicales
    if plane1["medical"] != plane2["medical"]:
        return plane1["medical"]
    
    # Ensuite priorité aux problèmes techniques
    if plane1["technical_issue"] != plane2["technical_issue"]:
        return plane1["technical_issue"]

    # Ensuite priorité au carburant le plus faible
    if plane1["fuel"] != plane2["fuel"]:
        return plane1["fuel"] < plane2["fuel"]

    # Ensuite priorité au niveau diplomatique le plus élevé
    if plane1["diplomatic_level"] != plane2["diplomatic_level"]:
        return plane1["diplomatic_level"] > plane2["diplomatic_level"]

    # Enfin, priorité à l'avion arrivé le plus tôt
    return plane1["arrival_time"] < plane2["arrival_time"]
1/      Nael
    Prend en entrée la liste d'avions et return True si elle n'a pas d'erreurs et False si elle en a et afficher les erreurs.

2/      Thibault
     Implémenter des fonctions utilitaires (affichage, recherche d’un minimum, extraction d’un sous-ensemble d'avions)

3/      Lizon
    Définir trois POLICY différentes (ex. priorité carburant, priorité 
    incidents, priorité diplomatique), sous forme de comparateurs ou de 
    fonctions de scoring. (qui décide quel avion est prioritaire)
    Prend en entrée 2 avions et return celui prioritaire.
    (Permettre de changer de POLICY sans réécrire l’algorithme de tri 
    (séparation POLICY / ALGORITHME).)

4/      Blanhe
    Implémenter au moins deux fonction de tris en temps quadratique (tri par insertion et tri par sélection) pour établir l’ordre d’atterrissage. 
    Fonction qui prend en entrée une liste d'avions, un POLICY et return la liste des avions trié dans l'ordre d'atterissage (priorité).(Elle utilisera la fonction créée précédement en 3)

    Comparer empiriquement les algorithmes (nombre de comparaisons, éventuellement temps d’exécution) sur plusieurs tailles de trafic. 

5/      Ryan
    Programmer un générateur de trafic permettant de créer différents scénarios (normal, crise carburant, crise médicale, sommet 
    diplomatique). Prend en entrée le type de scénario et le nombre d'avion voulu et renvoi une liste d'avion.

6/      Thibault
    Tester votre module sur des volumes croissants (10, 30, 50, 100 avions) et 
    analyser les limites du tri quadratique. 

7/      Nael
    Simuler l’écoulement du temps : à chaque tour, un avion atterrit, le 
    carburant des autres diminue, et un crash survient si fuel ≤ 0 ! 

    Produire un bilan (avions sauvés / crashés) et justifier vos choix

Du 1 au 5 doivent être publié !!!"AU PLUS TARD DIMANCHE!!! dimanche
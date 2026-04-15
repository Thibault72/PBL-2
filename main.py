import traffic_generator
import Fonction_utilitaires
import verification_key
import sorts

methods = "selection"
#"insertion" or "selection"



def Main(crisis, number_of_planes, Plane = None):
    if Plane != None:
        planes = Plane
    else:
        planes = traffic_generator.generate_traffic(crisis, number_of_planes)

    if not verification_key.verification(planes):
        print("Error in the data, please check the planes' information.")
        Fonction_utilitaires.afficher_avions(planes)
        return
    
    sorted_planes, crash, planes_crash = sorts.sort_aircraft(planes, crisis, methods)
    print(f"Planes that crashed: ")
    Fonction_utilitaires.afficher_avions(planes_crash)
    print(f"Planes that landed: ")
    Fonction_utilitaires.afficher_avions(sorted_planes)
    print(f"Number of planes that crashed: {crash}")

Main("normal", 100)
        
    


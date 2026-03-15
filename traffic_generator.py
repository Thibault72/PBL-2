import random
from Fonction_utilitaires import afficher_avions

def generate_traffic(scenario, n):

    if scenario not in ["normal","fuel_crisis","medical_crisis","diplomatic_summit"]:
        raise ValueError("unknown scenario")

    planes = []
    used_ids = []

    for i in range(n):

        while True:
            letter1 = chr(random.randint(65,90))
            letter2 = chr(random.randint(65,90))
            number = random.randint(100,999)

            plane_id = letter1 + letter2 + str(number)

            if plane_id not in used_ids:
                used_ids.append(plane_id)
                break

        plane = {
            "id": plane_id,
            "fuel": random.randint(10,60),
            "medical": False,
            "diplomatic_level": random.randint(1,5),
            "technical_issue": False,
            "arrival_time": round(19.4 + i * 0.01, 2)
        }

        if scenario == "fuel_crisis":
            plane["fuel"] = random.randint(5,30)

        elif scenario == "medical_crisis":
            if random.random() < 0.3:
                plane["medical"] = True

        elif scenario == "diplomatic_summit":
            plane["diplomatic_level"] = random.randint(3,5)

        planes.append(plane)

    return planes

afficher_avions(generate_traffic("fuel_crisis", 20))
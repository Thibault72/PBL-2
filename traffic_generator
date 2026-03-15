import random

def generate_traffic(scenario, n):

    if scenario not in ["normal","fuel_crisis","medical_crisis","diplomatic_summit"]:
        raise ValueError("unknown scenario")
    
    planes = []

    for i in range(n):

        plane = {
            "id": "A" + str(i),
            "fuel": random.randint(10,60),
            "medical": False,
            "diplomatic_level": random.randint(1,5),
            "technical_issue": False,
            "arrival_time": 19.40 + i * 0.01
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
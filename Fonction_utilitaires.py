#Implémenter des fonctions utilitaires (affichage, recherche d’un minimum, extraction d’un sous-ensemble d'avions)

AVIONS_INITIAL = [
    {"id": "AF342", "fuel": 18, "medical": False, "technical_issue": False, "diplomatic_level": 2, "arrival_time": 19.42},
    {"id": "LH908", "fuel": 25, "medical": False, "technical_issue": True,  "diplomatic_level": 1, "arrival_time": 19.44},
    {"id": "BA117", "fuel": 14, "medical": True,  "technical_issue": False, "diplomatic_level": 3, "arrival_time": 19.46},
    {"id": "EK202", "fuel": 40, "medical": False, "technical_issue": False, "diplomatic_level": 5, "arrival_time": 19.47},
    {"id": "IB455", "fuel": 12, "medical": False, "technical_issue": False, "diplomatic_level": 2, "arrival_time": 19.49},
    {"id": "AZ721", "fuel": 9,  "medical": False, "technical_issue": False, "diplomatic_level": 1, "arrival_time": 19.50},
    {"id": "UA331", "fuel": 22, "medical": False, "technical_issue": False, "diplomatic_level": 4, "arrival_time": 19.51},
    {"id": "QR998", "fuel": 16, "medical": False, "technical_issue": False, "diplomatic_level": 5, "arrival_time": 19.52},
    {"id": "TK876", "fuel": 8,  "medical": False, "technical_issue": False, "diplomatic_level": 2, "arrival_time": 19.53},
    {"id": "AC410", "fuel": 35, "medical": False, "technical_issue": False, "diplomatic_level": 3, "arrival_time": 19.54},
    {"id": "DL550", "fuel": 11, "medical": True,  "technical_issue": False, "diplomatic_level": 2, "arrival_time": 19.55},
    {"id": "SU119", "fuel": 27, "medical": False, "technical_issue": False, "diplomatic_level": 1, "arrival_time": 19.56},
    {"id": "SN204", "fuel": 6,  "medical": False, "technical_issue": False, "diplomatic_level": 2, "arrival_time": 19.57},
    {"id": "KL330", "fuel": 19, "medical": False, "technical_issue": False, "diplomatic_level": 3, "arrival_time": 19.58},
    {"id": "EY601", "fuel": 28, "medical": False, "technical_issue": False, "diplomatic_level": 4, "arrival_time": 19.59},
    {"id": "AF118", "fuel": 15, "medical": False, "technical_issue": True,  "diplomatic_level": 2, "arrival_time": 20.00},
    {"id": "LH332", "fuel": 21, "medical": False, "technical_issue": False, "diplomatic_level": 1, "arrival_time": 20.01},
    {"id": "BA450", "fuel": 10, "medical": False, "technical_issue": False, "diplomatic_level": 3, "arrival_time": 20.02},
    {"id": "IB900", "fuel": 17, "medical": False, "technical_issue": False, "diplomatic_level": 2, "arrival_time": 20.03},
    {"id": "AZ333", "fuel": 13, "medical": False, "technical_issue": False, "diplomatic_level": 1, "arrival_time": 20.04},
    {"id": "UA870", "fuel": 24, "medical": False, "technical_issue": False, "diplomatic_level": 4, "arrival_time": 20.05},
    {"id": "QR555", "fuel": 7,  "medical": False, "technical_issue": False, "diplomatic_level": 5, "arrival_time": 20.06},
    {"id": "TK221", "fuel": 20, "medical": False, "technical_issue": False, "diplomatic_level": 2, "arrival_time": 20.07},
    {"id": "AC990", "fuel": 5,  "medical": False, "technical_issue": False, "diplomatic_level": 3, "arrival_time": 20.08},
]



def afficher_avions(Liste):
    for avion in Liste:
        print(f"ID: {avion['id']}, Fuel: {avion['fuel']}, Medical: {avion['medical']}, Technical Issue: {avion['technical_issue']}, Diplomatic Level: {avion['diplomatic_level']}, Arrival Time: {avion['arrival_time']}")   

def utilitaire(Avions, minfuel = 0,maxfuel = 100, medical = None, technical_issue = None, mindiplomatic_level = 0, maxdiplomatic_level = 5):

    filtered_avions = []
    if medical != None and technical_issue != None:
        for avion in Avions:
            if (avion['fuel'] >= minfuel and avion['fuel'] <= maxfuel and avion['medical'] == medical and avion['technical_issue'] == technical_issue and
                avion['diplomatic_level'] >= mindiplomatic_level and avion['diplomatic_level'] <= maxdiplomatic_level):
                filtered_avions.append(avion)
    
    if medical == None and technical_issue != None:
        for avion in Avions:
            if (avion['fuel'] >= minfuel and avion['fuel'] <= maxfuel and avion['technical_issue'] == technical_issue and
                avion['diplomatic_level'] >= mindiplomatic_level and avion['diplomatic_level'] <= maxdiplomatic_level):
                filtered_avions.append(avion)

    if medical != None and technical_issue == None:
        for avion in Avions:
            if (avion['fuel'] >= minfuel and avion['fuel'] <= maxfuel and avion['medical'] == medical and
                avion['diplomatic_level'] >= mindiplomatic_level and avion['diplomatic_level'] <= maxdiplomatic_level):
                filtered_avions.append(avion)

    if medical == None and technical_issue == None:
        for avion in Avions:
            if (avion['fuel'] >= minfuel and avion['fuel'] <= maxfuel and
                avion['diplomatic_level'] >= mindiplomatic_level and avion['diplomatic_level'] <= maxdiplomatic_level):
                filtered_avions.append(avion)

    return filtered_avions

def minimum_fuel(Avions):
    if Avions == []:
        return None
    min_avion = Avions[0]
    for avion in Avions:
        if avion['fuel'] < min_avion['fuel']:
            min_avion = avion
    return min_avion

def minimum_arrival_time(Avions):
    if Avions == []:
        return None
    min_avion = Avions[0]
    for avion in Avions:
        if avion['arrival_time'] < min_avion['arrival_time']:
            min_avion = avion
    return min_avion

def maximum_diplomatic_level(Avions):
    if Avions == []:
        return None
    max_avion = Avions[0]
    for avion in Avions:
        if avion['diplomatic_level'] > max_avion['diplomatic_level']:
            max_avion = avion
    return max_avion


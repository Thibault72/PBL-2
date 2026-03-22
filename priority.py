

def Priority(crisis_type, plane1, plane2):

    if crisis_type == "fuel_crisis":
        if plane1["fuel"] < 5 and plane2["fuel"] >= 5:
            return True
        if plane2["fuel"] < 5 and plane1["fuel"] >= 5:
            return False
        return plane1["fuel"] < plane2["fuel"]


    if crisis_type == "medical_crisis":
        if plane1["medical"] != plane2["medical"]:
            return plane1["medical"]
        if plane1["fuel"] != plane2["fuel"]:
            return plane1["fuel"] < plane2["fuel"]
        return plane1["arrival_time"] < plane2["arrival_time"]


    if crisis_type == "diplomatic_summit":
        if plane1["diplomatic_level"] != plane2["diplomatic_level"]:
            return plane1["diplomatic_level"] > plane2["diplomatic_level"]
        return plane1["arrival_time"] < plane2["arrival_time"]



    if plane1["medical"] != plane2["medical"]:
        return plane1["medical"]
    
    if plane1["technical_issue"] != plane2["technical_issue"]:
        return plane1["technical_issue"]

    if plane1["fuel"] != plane2["fuel"]:
        return plane1["fuel"] < plane2["fuel"]

    if plane1["diplomatic_level"] != plane2["diplomatic_level"]:
        return plane1["diplomatic_level"] > plane2["diplomatic_level"]

    return plane1["arrival_time"] < plane2["arrival_time"]


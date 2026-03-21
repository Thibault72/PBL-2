"""
POLICIES MODULE
Defines decision rules (comparators) used to prioritize aircraft.
A policy. returns True if aircraft a1 should land before aircraft a2.
"""



"""
Priority order:
1. must_land
2. technical_issue
3. medical
4. lowest fuel
5. diplomatic
6. arrival_time (tie-break)
"""

a2= {
    "id": "A1",
    "fuel": 9,
    "medical": False,
    "technical_issue": True
}
a1 = {
    "id": "B2",
    "fuel": 6,
    "medical": False,
    "technical_issue": False
}

def priority(plane1,plane2):   
    if plane1["technical_issue"] != plane2["technical_issue"]:
        return plane1["technical_issue"] 

    # 2. if equal : medical emergency
    if plane1["medical"] != plane2["medical"]:
        return plane1["medical"] 

    # 3. if equal : fuel level 
    if plane1["fuel"] < plane2["fuel"]:
        return True
# if fuel < 5 : needs to land immediately
def fuel_crisis(plane1,plane2):
    if plane2["fuel"]< 5 < plane1["fuel"]:
        return False
    return True
# if fuel < 10 and technical issue : needs to land immediately
def crisis_weather(plane1, plane2):
    if (plane1["fuel"] < 10 and plane1["technical_issue"]) or (plane2["fuel"] < 10 and plane2["technical_issue"]):
        return (plane1["fuel"] < plane2["fuel"])
    return True    

if fuel_crisis != None:
    print (fuel_crisis(a1,a2))
elif crisis_weather != None :
    print(crisis_weather(a1,a2))
else :
    print(priority(a1,a2))



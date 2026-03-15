"""
POLICIES MODULE
Defines decision rules (comparators) used to prioritize aircraft.
A policy returns True if aircraft a1 should land before aircraft a2.
"""


def crisis_priority_policy(a1, a2):
    """
    Priority order:
    1. must_land
    2. technical_issue
    3. medical
    4. lowest fuel
    5. diplomatic
    6. arrival_time (tie-break)
    """

    if a1.must_land != a2.must_land:
        return a1.must_land

    if a1.technical_issue != a2.technical_issue:
        return a1.technical_issue

    if a1.medical != a2.medical:
        return a1.medical

    if a1.fuel != a2.fuel:
        return a1.fuel < a2.fuel

    if a1.diplomatic != a2.diplomatic:
        return a1.diplomatic

    return a1.arrival_time < a2.arrival_time



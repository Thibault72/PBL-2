# PBL-2
The best team
## Project Name
PBL 2 - Error finder
## Group Members
| Thibault | Project lead + Developper + Kanban + Tester |
| Nael | Developper |
| Lizon | Developper + readme |
| Ryan | Developper |
| Blanche | Developper |
## Description
APP_datasets builds several datasets of airplanes (“avions”) with different characteristics, to simulate air traffic prioritization during normal and crisis situations (deciding which plane should land first).

Fonction_utilitaires defines a set of utility functions to analyze and filter airplane data, to decide landing priorities.

Priority compares two planes and returns which one should be prioritized (returns True if plane1 has higher priority than plane2) based on the type of crisis.

Sorts implements two sorting algorithms (insertion sort and selection sort) to order planes by priority, using the Priority function as a custom comparison rule.

traffic_generator generates a random list of airplanes simulating different traffic scenarios, then displays them(20 differerent planes at the end).

verification_key checks whether each plane dictionary is valid and correctly formatted, and tries to detect duplicate IDs. It verifies that every plane has all required fields (id, fuel, medical, technical_issue, diplomatic_level, arrival_time) and that each value has the correct data type (int, bool, float, str).
## Installation / Usage
None
## Project Structure
Files/ Dictionnaries
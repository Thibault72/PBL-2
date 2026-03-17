# Sorting functions used to determine the landing order of aircraft.
# Two quadratic sorting algorithms are implemented:
# - Insertion sort
# - Selection sort
# Both algorithms use a policy function that compares two aircraft and decides wich one has priority.


def insertion_sort(aircraft_list, policy):
    n = len(aircraft_list)
    for i in range(1, n):
        current_aircraft = aircraft_list[i]
        j = i - 1
        while j >= 0 and policy(current_aircraft, aircraft_list[j]):
            aircraft_list[j + 1] = aircraft_list[j]
            j -= 1
        aircraft_list[j + 1] = current_aircraft
    return aircraft_list


def selection_sort(aircraft_list, policy):
        n = len(aircraft_list)
        for i in range(0, n - 1):
             priority_index = i
             for j in range(i + 1, n):
                  if policy(aircraft_list[j], aircraft_list[priority_index]):
                       priority_index = j
             aircraft_list[i], aircraft_list[priority_index] = aircraft_list[priority_index], aircraft_list[i]
        return aircraft_list
        

def sort_aircraft(aircraft_list, policy, method="insertion"):

     if method=="insertion":
          return insertion_sort(aircraft_list, policy)
     
     elif method=="selection":
          return selection_sort(aircraft_list, policy)
     
     else:
          raise ValueError("Unknown sorting method")
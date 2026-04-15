# Sorting functions used to determine the landing order of aircraft.
# Two quadratic sorting algorithms are implemented:
# - Insertion sort
# - Selection sort
# Both algorithms use a policy function that compares two aircraft and decides wich one has priority.


import priority


def insertion_sort(aircraft_list, policy):
     n = len(aircraft_list)
     crash = 0
     planes_crash = []
     for i in range(1, n):
          current_aircraft = aircraft_list[i]
          j = i - 1
          while j >= 0 and priority.Priority(policy, current_aircraft, aircraft_list[j]):
               aircraft_list[j+1] = aircraft_list[j]
               j -= 1
          aircraft_list[j + 1] = current_aircraft
          for c in aircraft_list[j+2:]:
               c["fuel"] -= 1
               print(c["id"], c["fuel"])
               if c["fuel"] == 0:
                    crash += 1
                    planes_crash.append(c)
     return aircraft_list, crash, planes_crash


def selection_sort(aircraft_list, policy):
     aircraft_list = [plane.copy() for plane in aircraft_list]
     n = len(aircraft_list)
     crash = 0
     planes_crash = []
     for i in range(0, n - 1):
          priority_index = i
          for j in range(i + 1, n):
               if priority.Priority(policy, aircraft_list[j], aircraft_list[priority_index]):
                    priority_index = j
          aircraft_list[i], aircraft_list[priority_index] = aircraft_list[priority_index], aircraft_list[i]
          for c in aircraft_list[i+1:]:
               if c not in planes_crash:
                    c["fuel"] -= 1
                    if c["fuel"] <= 0:
                         crash += 1
                         planes_crash.append(c)
     L = []
     for el in aircraft_list:
          if el not in planes_crash:
               L.append(el)
     return L, crash, planes_crash

        

def sort_aircraft(aircraft_list, policy, method="insertion"):

     if method=="insertion":
          return insertion_sort(aircraft_list, policy)
     
     elif method=="selection":
          return selection_sort(aircraft_list, policy)
     
     else:
          raise ValueError("Unknown sorting method")
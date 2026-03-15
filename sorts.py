# Sorting functions used to determine the landing order of aircraft.
# Two quadratic sorting algorithms are implemented:
# - Insertion sort
# - Selection sort
# Both algorithms use a policy function that compares two aircraft and decides wich one has priority.

def insertion_sort(aircraft_list, policy):
    # Create a copy of the list to avoid modifying the original dataset
    aircraft = aircraft_list.copy()
    # Loop through the list starting from the second element
    for i in range(1, len(aircraft)):
        # Aircraft currently being placed in the sorted part
        current_aircraft = aircraft[i]
        j=j-1
        # Move elements that have lower priority to the right until we find correct position
        while j>=0 and policy(current_aircraft, aircraft[j]):
            aircraft[j+1] = aircraft[j]  # shift aircraft to the right
            j-=1
        # Insert th aircraft in the correct position
        aircraft[j+1] = current_aircraft
    # Return the sorted list
    return aircraft


def selection_sort(aircraft_list, policy):
        # Copy the list so the original data is not modified
        aircraft = aircraft_list.copy()
        # Get the number of aircraft
        n=len(aircraft)
        # Move the boundary of the unsorted part of the list
        for i in range(n):
             # Assume the first aircraft of the unsorted part has priority
             priority_index = i
             # Search for a higher priority aircraft in the rest of the list
             for j in range (i + 1, n):
                  # If aircaft [j] has higher priority, update the index
                  if policy(aircraft[j], aircraft[priority_index]):
                       priority_index = j
        # Swap the found aircraft with the first unsorted position
        aircraft[i], aircraft[priority_index] = aircraft[priority_index], aircraft[i]
        # Return the sorted list
        return aircraft
        
        
def sort_aircraft(aircraft_list, policy, method="insertion"):
     # Choose the sorting algorithm depending o the method parameter
     if method=="insetion":
          return insertion_sort(aircraft_list, policy)
     
     elif method=="selection":
          return selection_sort(aircraft_list, policy)
     # If the method does not exist, raise an error
     else:
          raise ValueError("Unknown sorting method")
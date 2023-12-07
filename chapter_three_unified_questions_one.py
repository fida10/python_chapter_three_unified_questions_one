"""
Practice Question 1: Favorite Cities and Their Descriptions

Task:

Create a function city_descriptions that takes a dictionary 
where keys are city names and values are their descriptions. 
Return a list of strings, each containing the name of the city 
and its description in a readable format.
"""

def city_descriptions(cities):
    ans = []
    for key, value in cities.items():
        ans.append(f"{key}: {value}")
    return ans

"""
Practice Question 2: Manipulate Guest List

Task:

Write a function manage_guests that simulates inviting, 
removing, and re-inviting guests. 
It should take a list of guests, 
remove one specified guest, 
add a new guest, 
and return the modified list.
"""

def manage_guests(guests, guest_to_remove, guest_to_add):
    if guest_to_remove in guests:
        guests[guests.index(guest_to_remove)] = guest_to_add
    else:
        guests.append(guest_to_add);
    return guests

"""
Practice Question 3: Sorting and Reversing a List

Task:

Implement a function sort_and_reverse that takes 
a list of integers and 
returns a tuple of two lists: 
the first list should be the input list sorted in ascending order, 
and the second list should be the input list sorted in descending order.
"""

def sort_and_reverse(numbers):
    return sorted(numbers), sorted(numbers, reverse=True)

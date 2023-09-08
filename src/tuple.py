import os
from collections import namedtuple

term_size: int = os.get_terminal_size()

# creating a tuple directly as literal
numbers: tuple = (5, 4, 3, 2, 1)
person = ("Gaurav", 25, "Dehradun", "Uattarakhand", "India")

if '__main__' == __name__:
    print('-' * term_size.columns)
    print(person)
    print(numbers)
    print('-' * term_size.columns)

    # Tuple Packing and Unpacking:
    name, age, city, state, country = person
    print(name, age, city, state, country)
    print('-' * term_size.columns)

    # Tuples as Dictionary Keys:
    person_info = {("Gaurav", "Tripti"): 25, ("Mohit", "Bhavil"): 30}
    print(person_info[("Gaurav", "Tripti")])
    print('-' * term_size.columns)
    
    # Tuples in Data Structures: lists of tuples
    numbers = [(1, "one"), (2, "two"), (3, "three")]
    print(numbers)
    print('-' * term_size.columns)

    # Named Tuples: give names to each field for better readability
    Person = namedtuple('Person', ['name', 'age'])
    gaurav = Person('Gaurav', 25)
    print(gaurav)
    name, age = gaurav
    print(name, age)
    print('-' * term_size.columns)

    # Tuple Comprehensions:
    squared = tuple(x**2 for x in range(1, 6))
    print("squared in range 1, 6:- ", squared)
    print('-' * term_size.columns)

    # Using Tuples in Zip:
    names = ('Gaurav', 'Tripti', 'Bhavil')
    scores = (85, 92, 78)
    zipped = list(zip(names, scores))
    print(f"zipping names & scores {names} | {scores}:- ", zipped)
    print('-' * term_size.columns)
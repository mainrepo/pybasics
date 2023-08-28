# creating a list directly as literal
numbers: list = [5, 4, 3, 2, 1]

if '__main__' == __name__:
    # creating a list from iterable
    new_numbers = list(numbers)
    # checking to see if they point to same location
    num_id = id(numbers);   new_id = id(new_numbers)
    print(f"{num_id}  :  {new_id}")
    # checking if they are equal
    print("numbers == new_numbers", numbers == new_numbers)

    # Append: Adds an element to the end of the list.
    numbers.append(6)
    print(f"after numbers.append :  {numbers}")

    # Extend: Extends the list by adding elements from another iterable.
    numbers.extend([7, 8, 9])
    print(f"after numbers.extend :  {numbers}")

    # Insert: Inserts an element at a specific index.
    numbers.insert(0, 0)
    print(f"after numbers.insert 0 at 0 :  {numbers}")

    # Remove: Removes the first occurrence of a value.
    numbers.remove(5)
    print(f"after numbers.remove first occurrence of 5:  {numbers}")

    # Pop: Removes and returns an element by index.
    popped_element = numbers.pop(2)
    print(f"after numbers.pop at index 2 got element {popped_element}:  {numbers}")

    # Updating elements in a list:
    numbers[2] = 10
    print(f"numbers[2] = 10:  {numbers}")

    # Index: Returns the index of the first occurrence of a value.
    index_of_4 = numbers.index(4)
    print(f"numbers.index for element 4: {index_of_4}")

    # Count: Returns the number of occurrences of a value.
    count_of_2 = numbers.count(2)
    print(f"numbers.count for element 2: {count_of_2}")

    # Sorting a list:
    sorted_numbers = sorted(numbers)  # Creates a new sorted list.
    print(f"sorted_numbers:  {sorted_numbers}")
    numbers.sort()  # Sorts the list in-place.
    print(f"in place sorting with numbers.sort:  {numbers}")
    
    # Reversing a list:
    reversed_numbers = reversed(numbers)  # Creates a reversed iterator.
    print(f"reversed_numbers:  {reversed_numbers}")
    numbers.reverse()  # Reverses the list in-place.
    print(f"in place reversal with numbers.reverse:  {numbers}")

    # Filtering elements:
    filtered_numbers = [x for x in numbers if x > 7]
    print(f"filtered_numbers greater than 7:  {filtered_numbers}")
    
    # List comprehensions:
    numbers_squared = [x**2 for x in numbers]
    print(f"numbers_squared:  {numbers_squared}")

    # Mapping elements:
    mapped_numbers = [x * 2 for x in numbers]
    print(f"mapped_numbers to double each element:  {mapped_numbers}")
    
    # Mapping elements after filtering:
    mapped_numbers = [x * 2 for x in numbers if x > 7]
    print(f"mapped_numbers to double each element after filtering:  {mapped_numbers}")

    # Shallow copy: Creates a new list, copying references to nested objects. :TODO
    new_numbers = numbers.copy()
    print(f"numbers.copy:  {new_numbers}")

    # Deep copy: Creates a new list with new copies of nested objects.
    import copy
    new_numbers = copy.deepcopy(numbers)
    print(f"copy.deepcopy(numbers):  {new_numbers}")

    # Clear: Removes all elements from the list.
    numbers.clear()
    print(f"after numbers.clear:  {numbers}")
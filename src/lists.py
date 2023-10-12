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

    # Nested List Comprehension (Matrix Transpose):
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"matrix:  {matrix}")
    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"matrix.transpose:  {transpose}")
    '''
    the inner comprehension [row[i] for row in matrix] iterates through each 
    row and extracts the element at the same index i from each row, effectively 
    transposing the matrix
    '''

    # Nested List Comprehension (Multiple Iterables):
    pairs = [(x, y) for x in [1, 2, 3] for y in [10, 20, 30]]
    print(f"multiple iterables:  {pairs}")

    # Complex Transformation and Filtering:
    words = ["apple", "banana", "cherry"]
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_words = [word.upper() if word[0] in vowels else word.lower() for word in words]
    print(f"filtered_words:  {filtered_words}")
    
    # Conditional Transformation and Flattening:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_even = [num for row in matrix if any(row) for num in row if num % 2 == 0]
    print(f"flattened_even:  {flattened_even}")
    '''
    This comprehension iterates through the matrix, flattening even numbers from each 
    row only if the row contains at least one non-zero element.
    '''

    # List of Prime Numbers:
    primes = [x for x in range(2, 100) if all(x % d != 0 for d in range(2, int(x**0.5)+1))]
    print(f"primes:  {primes}")

    # List Comprehension with Dictionary:
    numbers = [1, 2, 3, 4, 5]
    squared_dict = {x: x**2 for x in numbers}
    print(f"squared_dict:  {squared_dict}")

    # Fibonacci numbers
    n = 5  # Number of Fibonacci numbers to generate
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    # fib = [fib[i-1] + fib[i-2] for i in range(2, n)]
    print(f"fibonacci:  {fib}")
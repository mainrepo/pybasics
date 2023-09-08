def my_generator():
    yield 1
    yield 2
    yield 3

def read_large_file_in_batches(file_path, batch_size=10000):
    try:
        with open(file_path, 'r') as file:
            batch = []
            for line in file:
                batch.append(line.strip())
                if len(batch) >= batch_size:
                    yield batch
                    batch = []
            if batch:
                yield batch
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def api_call(url, method, read_timeout=60):
    def decorator(api_func):
        def wrapper(*args, **kwargs):
            response = None
            try:
                # parse *args, **kwargs to create a payload
                # call the api response = api(url, method, payload, read_timeout)
                response = api_func(response)
                print("api call ok:- ", response)
            except Exception as excp:
                print("Error:- ", excp.message if hasattr(excp, "message") else str(excp))
            return response
        return wrapper
    return decorator

@api_call('/payment/service', 'post')
def call_payment(data):
    return data

if '__main__' == __name__:
    # Example usage: generators
    gen = my_generator()
    for value in gen:
        print(value)

    try:
        next(gen)
    except StopIteration:
        print("Generator is exhausted.")

    # Example usage: iterating dictionary
    ages = {
        "gaurav": "30", "tripti": "26", "bhavil":"8"
    }
    for name, age in ages.items():
        print(name, ":- ", age)

    # Example usage: reading large files of 10-50 GB etc.
    file_path = 'path_to_large_file.txt'

    for batch in read_large_file_in_batches(file_path):
        # Process the batch of lines (e.g., perform operations or analysis)
        for line in batch:
            # Process each line within the batch
            pass
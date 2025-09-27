import os
import random

def create_files(sizes):
    """
    Creates text files with lists of numbers for sorting algorithm testing.
    For each size, it generates three files:
    - random_numbers_{size}.txt
    - ascending_numbers_{size}.txt
    - descending_numbers_{size}.txt
    """
    for size in sizes:
        print(f"Generating files for size: {size}...")

        # Generate a list of random integers
        random_list = [random.randint(0, 1000000) for _ in range(size)]

        # --- Random Order ---
        random_filename = f"random_numbers_{size}.txt"
        with open(random_filename, 'w') as f:
            for number in random_list:
                f.write(f"{number}\n")
        print(f"  - Created '{random_filename}'")

        # --- Ascending Order ---
        ascending_list = sorted(random_list)
        ascending_filename = f"ascending_numbers_{size}.txt"
        with open(ascending_filename, 'w') as f:
            for number in ascending_list:
                f.write(f"{number}\n")
        print(f"  - Created '{ascending_filename}'")

        # --- Descending Order ---
        descending_list = sorted(random_list, reverse=True)
        descending_filename = f"descending_numbers_{size}.txt"
        with open(descending_filename, 'w') as f:
            for number in descending_list:
                f.write(f"{number}\n")
        print(f"  - Created '{descending_filename}'")

if __name__ == '__main__':
    # List of all required sizes for testing
    test_sizes = [100, 1000, 5000, 30000, 50000, 100000, 150000, 200000]

    # Create a directory to store the files
    if not os.path.exists("test_data"):
        os.makedirs("test_data")
        os.chdir("test_data")
    else:
        os.chdir("test_data")
    
    create_files(test_sizes)
    print("\nAll files have been generated in the 'test_data' folder.")
import sys

## STEP 1
def count_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            byte_count = len(file.read())
        print(f"{byte_count} {filename}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)







if sys.argv[1] == '-c':
    count_bytes(sys.argv[2])
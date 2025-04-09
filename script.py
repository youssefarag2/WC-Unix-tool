import sys

# STEP 1 : Count Bytes
def count_bytes(filename):
    try:
        with open(filename, 'rb') as file:
            byte_count = len(file.read())
        print(f"{byte_count} {filename}")
        return byte_count

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)



# STEP2 : Count Lines
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = len(file.read().splitlines())
        print(f"{lines} {filename}")
        return lines

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

# STEP3: Word Count
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            words = len(file.read().split())
        print(f"{words} {filename}")
        return words

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

# STEP4: Count Characters
def count_characters(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read() # Normalize line endings
        print(f"{len(text)} {filename}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

# STEP5: Count default
def get_counts(filename):
    try:
        with open(filename, 'rb') as f:
            content = f.read()
            byte_count = len(content)
            
        with open(filename, 'r') as f:
            text = f.read()
            line_count = len(text.splitlines())
            word_count = len(text.split())
            
        return (line_count, word_count, byte_count)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)

def wc_default(filename):
    lines, words, bytes = get_counts(filename)
    print(f"{lines:>8}{words:>8}{bytes:>8} {filename}")
    return (lines, words, bytes, filename)


if sys.argv[1] == '-c':
    count_bytes(sys.argv[2])
elif sys.argv[1] == '-l':
    count_lines(sys.argv[2])
elif sys.argv[1] == '-w':
    count_words(sys.argv[2])
elif sys.argv[1] == '-m':
    count_characters(sys.argv[2])
elif len(sys.argv) == 2:
    wc_default(sys.argv[1])

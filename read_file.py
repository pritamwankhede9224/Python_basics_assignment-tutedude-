# Read from a file
try:
    with open('output.txt', 'r') as f:
        data = f.read()
    print('Contents of output.txt:\n')
    print(data)
except FileNotFoundError:
    print('output.txt not found. Run write_file.py first.')

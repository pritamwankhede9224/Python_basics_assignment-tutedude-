# Write to a file
content = """This is a sample file created for the assignment.
Lets go attempt two """

with open('output.txt', 'w') as f:
    f.write(content)

print('Wrote to output.txt')

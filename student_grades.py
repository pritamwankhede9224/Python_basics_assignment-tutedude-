# Student Grades - simple menu-based program
grades = {}  # student_name -> grade (string)

def add_student(name, grade):
    grades[name] = grade
    print(f'Added {name} with grade {grade}')

def update_student(name, grade):
    if name in grades:
        grades[name] = grade
        print(f'Updated {name} to grade {grade}')
    else:
        print(f'Student {name} not found. Use add to create.')

def print_all():
    if not grades:
        print('No students yet.')
    else:
        print('Student Grades:')
        for name, g in grades.items():
            print(f'- {name}: {g}')

def menu():
    while True:
        print('\nMenu: 1) Add  2) Update  3) Print  4) Exit')
        choice = input('Choose: ').strip()
        if choice == '1':
            n = input('Student name: ').strip()
            gr = input('Grade: ').strip()
            add_student(n, gr)
        elif choice == '2':
            n = input('Student name to update: ').strip()
            gr = input('New grade: ').strip()
            update_student(n, gr)
        elif choice == '3':
            print_all()
        elif choice == '4':
            break
        else:
            print('Invalid choice.')
            
if __name__ == "__main__":
    menu()

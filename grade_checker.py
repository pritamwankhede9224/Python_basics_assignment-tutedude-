# Grade Checker
score = input('Enter score (0-100): ')
try:
    score = float(score)
    if score >= 90:
        print('Grade: A')
    elif score >= 80:
        print('Grade: B')
    elif score >= 70:
        print('Grade: C')
    elif score >= 60:
        print('Grade: D')
    else:
        print('Grade: F')
except ValueError:
    print('Please enter a valid number.')

"""

Broken program to determine score status
"""



score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print('Excellent')
    elif score in range (50, 90):
        print('Pass')
    else:
        print('Bad')
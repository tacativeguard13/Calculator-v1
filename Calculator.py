from Calculations import Calculations

validity = True

print("     Calculator      ")
print("Welcome to calculator")
print('''1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Find the square
6: Find the cube
7: Find the Square Root
8: Find the Cube Root
9: Find percentage''')
work = input("What work do you want to do ?\n")

if work == '1':
    Calculations.Addition()
elif work == '2':
    Calculations.Subtraction()
elif work == '3':
    Calculations.Multiplication()
elif work == '4':
    Calculations.Division()
elif work == '5':
    Calculations.Square()
elif work == '6':
    Calculations.Cube()
elif work == '7':
    Calculations.SquareRoot()
elif work == '8':
    Calculations.CubeRoot()
elif work == '9':
    Calculations.Percentage()
else:
    print("Plese define a Work to do")
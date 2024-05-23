import math

def calculate(radius):
    return math.pi * radius**2

while True:
    inputfromuser = input("Enter the radius of the circle (or type 'DONE' to exit): ")

    if inputfromuser == "DONE":
        print("Exiting the program. Thank you!")
        break

    try:
        radius = float(inputfromuser)
        if radius >= 0:
            area = calculate(radius)
            print(f"The area of the circle with radius {radius:.2f} is {area:.2f}")
        else:
            print("Incorrect input, try again!")
    except ValueError:
        print("Incorrect input, try again!")
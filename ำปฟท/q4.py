import math as m

shape = input("Input a shape T/S/C: ")
leagth = input("Input a length:  ")

leagth = int(leagth)

shape = shape.upper()

if shape == "C" :
    
    circle = m.pi*(leagth/2)**2
    print("The surface area of circle is %.2f"% circle)
    
elif shape == "S" :
    
    square =  (leagth**2)/2
    print("The surface area of square is %.2f "% square)
    
elif shape == "T" :
    
    trin = 1/2*leagth*(leagth/2)
    print("The surface area of trinangle is %.2f"% trin)
    
else :
    print("Length must be more than or equal to zero.")
a = input("Input:a=? ")
b = input("Input:b=? ")
c = input("Input:c=? ")

if not a.isdigit() and not b.isdigit() and not c.isdigit():
    print('Some input is not a number.')
    exit()

a = int(a)
b= int(b)
c= int(c)

if a<0 or b<0 or c<0:
    print("Output:Can't form a triangle")
    exit()
if a>=b and a>=c :
    if a < b+c:
        print("Output: Form a triangle")
    else:
        print("Output:Can't form a triangle")
    
elif b>=a and b>=c:
    if b < a+c:
         print("Output: Form a triangle")
    else:
         print("Output:Can't form a triangle")
    
elif c>=a and c>=b: 
    if c < b+a:
        print("Output: Form a triangle")
    else:
        print("Output:Can't form a triangle")
     
    

    


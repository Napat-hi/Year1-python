line = int(input("enter no. of lines: "))
if line < 1:
    print("Error")
for i in range(1,line+1):
    if n%2 == 0:
        n = "-"
    else:
        n = "*"
    print(i*n)
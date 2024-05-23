size = input("Enter an integer number: ")
size = int(size)
rowCount = 0
columnCount = 0 #keep track of number of columns created in each row (reset after every loops)

while rowCount < size: #keep track of number of row created
    if rowCount == 0 or rowCount == size-1: #check whether it's the first or the last row
        while columnCount < size: #if it's the first or the last row, then print "x" the entire line
            print("o", end=" ")
            columnCount += 1
        columnCount = 0 #reset column
    else: #if it's not the first or the last row, then check if it's the first or thhe last column
        while columnCount < size:
            if columnCount == 0 or columnCount == size-1: #if it's the first or the last column, then print "X"
                print("o", end=" ")
            else: #if it's not then print " "
                print(" ", end=" ")
            columnCount += 1
        columnCount = 0 #reset column
    print()
    rowCount += 1  
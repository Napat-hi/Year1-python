input = input("Input: ")

if len(input) == 9 and input.count(".") + input.count("X") + input.count("O") == 9:
    print("""\n-------
|%s|%s|%s|
-------
|%s|%s|%s|
-------
|%s|%s|%s|
-------""" % (input[0], input[1], input[2], input[3], input[4], input[5], input[6], input[7], input[8]))
    
else:
    print("Error")

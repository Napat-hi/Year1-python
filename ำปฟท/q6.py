first = input("Give me a character: ")
second = input("Give me another character: ")

alphabets = "abcdefghijklmnopqretuvwxyz"

startindex = 0
endindex = 0

if first > second :
    temp = first 
    first = second 
    second = temp
    
if first.isalpha() and second.isalpha():
    
    for i in range (len(alphabets)):
        
        if alphabets[i] == first:
            startindex = i
        elif alphabets[i] == second:
            endindex = i
    print("Output: ")       
    
    for i in range(startindex, endindex+1):
        print(alphabets[i], end = "")
    
else :
    print("You need to input two characters.")        

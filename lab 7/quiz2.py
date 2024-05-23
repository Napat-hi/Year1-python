names_list = []

while True:
    name =input("Input: Enter a word:")
    if name == "exit" :
           break
    
    names_list.append(name.capitalize())

    
print("Output:", names_list)   
    
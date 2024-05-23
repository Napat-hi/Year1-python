words_list = []

while True:
    word = input("Input: Enter a word:")
    if word == "exit":
        break
    
    if word.endswith("y"):
        word = word[:-1] + "ily"
    words_list.append(word)
print("Output:", words_list)
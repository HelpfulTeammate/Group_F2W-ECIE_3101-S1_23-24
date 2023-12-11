input_string = input("Please enter a string: ")
letters= []
letters_count = []
print("Enter 3 letters: ")
for i in range (3):
    letter = input()
    letters.append(letter)
    letter_count = input_string.lower().count(letters[i].lower())
    letters_count.append(letter_count)
for i in range (3):
    print(letters[i], " appears ", letters_count[i], " times.")
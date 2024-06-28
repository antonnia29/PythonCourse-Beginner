# Antonnia Abdul - AN24020013912


#Pseudocode that creates alternating character and words based on user's input

""" Steps:
1. create an input option for user to enter sentence.
2. create a for loop that changes alternate character in string.
3. create a for loop that changes alternate word in string.
4. display both results to user.

"""



# user's input string

character_string = input("\nPlease enter a message for alternating character sentence demo...\n\n").lower()
print("\n----------------------------------------------------------------------- \n")



#Part 1 - Alternate character

new_string = ""

for alt_car in range(len(character_string)):
    if alt_car % 2 == 0:
        new_string += character_string[alt_car].upper()
    else:
        new_string += character_string[alt_car].lower()

print(f"\nAlternate Characters... \n>> {new_string}")



print("\n----------------------------------------------------------------------- \n")


#Part 2 - Alternate word


words = character_string.split()
for alt_word in range(len(words)):
    if alt_word % 2 == 0:
        words[alt_word] = words[alt_word].upper()
    else:
        words[alt_word] = words[alt_word].lower()

join_words = " ".join(words)
print(f"Alternate Word... \n>> {join_words}\n")


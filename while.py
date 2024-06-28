# Antonnia Abdul - AN24020013912

#Pseudocode to create a loop that ask user's input till condition is met and calculates the average of the values

"""Steps.
1. create loop to ask user's input 
2. define average function and logic to calculate average
3. create variable for empty list
4. state print values in the presence of a valid input 
4. Run terminal to test output
"""


#action to record list of numbers and calculate the average from user input
list_of_entry = []  #empty list

def Average(list):
    return sum(list) / len(list)


# ask user to input number(s)

while input != -1:  #loop will repeat while the input response is true
    user_entry = float(input("Enter any number (when done enter ' -1 ')): "))
    list_of_entry.insert(0,user_entry)

    if user_entry < -1 or user_entry > -1:
        print("keep going")

    elif user_entry == -1:   #trigger the break, input statement no longer true
        break

#indented out of the loop so that the response bellow doesnot appear with every loop
if len(list_of_entry) != 0:  #if the length of values is not zero, does contain value
        list_of_entry.remove(-1)
        print("Here are the numbers you've entered! ")
        print(list_of_entry)
        print( )
        print("Average of the numbers are: ", Average(list_of_entry))

else: 
    print("no valid input")
    
   
    



# Antonnia Abdul Task 8 - AN24020013912

#Pseudocode that allows a user to register students for an exam venue

"""Steps:
1. request user to input no. of students
2. create a file that the user input will be stored in
3. create a loop for the number of students to be entered

"""


try:

    no_of_students = int(input("\nHow many students are you registering?   "))
    print("\n..............................................................\n" )
    
    with open ('reg_form.txt','w') as file:

            for num in range(no_of_students):
                if num <= no_of_students:
                    student_id = input(f"Enter the ID number for student: {num+1}!  ")
                    file.write(f'{student_id :15} Signature ..................\n')
                    # print('============================================================\n')

    print("student id is written to text file, action complete")
                    
                

except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except NameError as e:
    print(f"Error: {e}")



   
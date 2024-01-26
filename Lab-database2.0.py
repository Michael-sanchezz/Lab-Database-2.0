# At the top of main.py, create a list of dictionaries to store data about three or more
# students. You can pick the names, hometowns, and favorite foods, or just use the list above.
student_tina = {'name': 'Tina', 'hometown': 'Portland', 'favorite_food': 'puppy chow'}
student_Klaus = {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"}
student_julia = {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}


# Write a function list_names that…
# takes in the list of students as a parameter
# loops through the list and prints out their name along with their position in the list (index + 1). For example,
def list_names(stu):
    # print(len(queue))
    count = 1  # sets up a counter to keep track of where I am in the loop if I need it
    if stu == "view":
        for x in queue:
            print(f'{count}. {x["name"]}')
            count += 1

    elif type(stu) == str:  # compare if the input is a string
        for student in queue: # loops through the queue list
            if stu == student["name"]:  # if the input matches a name in queue then name is printed
                print(f'{count}. {stu}')
                view_choice = input("would you like to see this students (hometown) or (favorite food)? ")
                # prompts for more information
                while view_choice != 'hometown' or view_choice != "favorite food":
                    if view_choice == 'hometown':  # use keywords to learn more information
                        print(student['hometown'])
                        print()
                        return
                    elif view_choice == 'favorite food':
                        print(student['favorite_food'])
                        print()
                        return
                    else:
                        print("invalid choice, try again! ")
                        view_choice = input("would you like to see this students hometown or favorite food? ")
            count += 1
    elif type(stu) == int:
        for x in range(len(queue) + 1):  # loops through list +1 so it reaches the end
            if x == stu:
                q = queue[stu - 1]
                print(f'{x}. {q["name"]}\n')  # print if index found
                view_choice = input("would you like to see this students (hometown) or (favorite food)? ")
                while view_choice != 'hometown' or view_choice != "favorite food":
                    # check which keyword was entered and print relevant info
                    if view_choice == 'hometown':
                        print(q['hometown'])
                        return
                    elif view_choice == 'favorite food':
                        print(q['favorite_food'])
                        return
                    else:
                        print("invalid choice, try again! ")  # if invalid choice then restarts loop
                        view_choice = input("would you like to see this students (hometown) or (favorite food)?")

        print()
    return ""


def get_new_student():  # creates new student information
    print()
    new_student = {'name': "", 'hometown': "", 'favorite_food': ""}  # create new dictionary
    new_name = input("enter the new students name ")
    new_hometown = input("enter the new students hometown ")
    new_food = input("enter the new students favorite food ")
    new_student['name'] = new_name  # adds new name to the list
    new_student["hometown"] = new_hometown  # add new hometown
    new_student["favorite_food"] = new_food  # add new food
    print(new_student)
    return queue.append(new_student)


print()

queue = [student_julia, student_tina, student_Klaus]  # combine all the dictionaries together
user_choice = True
while user_choice:
    user_input = input("select one of the following options\nadd - to create a new student"  # displays the menu options
                       "\nview - to look at existing students"
                       "\nquit - to exit the program ")
    # stu_name = input("enter a students name you would like to learn more about ")  # uses a string to find a student
    # list_names(stu_name)  # calls the function with a string
    if user_input == "add":
        get_new_student()  # makes a call to the function to add a new student
    elif user_input == "view":  # lists the student name and numbers
        print(list_names(user_input))  # calls the function
        student_num = int(input("which student file would you like to access? select the relevant number "))
        # uses an int to find a student
        if student_num > len(queue) + 1 or student_num <= 0:  # checks if student number is in database
            print("not a valid number! try again ")  # if invalid print this message
        else:
            list_names(student_num)  # if the number is fine then call the function
    elif user_input == "quit":  # exits the program
        print("Goodbye")  # print this message before exit
        exit(1)
    else:
        print("not a valid input! ")  # if an invalid input was entered print this message and restart the loop
    print()

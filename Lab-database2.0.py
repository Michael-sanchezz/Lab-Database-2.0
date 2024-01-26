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
    y = 1
    count = 0
    if stu == "view":
        for x in queue:
            print(f'{y}. {x["name"]}')
            y += 1
        num_choice = int(input("enter a students number"))
        while num_choice > len(queue) or num_choice <  0:
            print("invalid")
        else:
            view_choice = input("enter 'hometown' or 'favorite food' to learn more ")
            while view_choice != 'hometown' or view_choice != "favorite food":
                if view_choice == 'hometown':
                    home=queue[num_choice-1]
                    print(home["hometown"])
                    print()
                    return ""
                elif view_choice == 'favorite food':
                    food=queue[num_choice-1]
                    print(food["favorite_food"])
                    print()
                    return ""
                else:
                    print("invalid choice, try again! ")
                    view_choice = input(("would you like to see this students hometown or favorite food?"))
    elif type(stu) == str:
        for student in queue:
            count += 1
            if stu == student["name"]:
                print(f'{count}. {stu}')
                view_choice= input(("would you like to see this students hometown or favorite food? "))
                while view_choice != 'hometown' or view_choice != "favorite food":
                    if view_choice == 'hometown':
                        print(student['hometown'])
                        print()
                        return
                    elif view_choice == 'favorite food':
                        print(student['favorite_food'])
                        print()
                        return
                    else:
                        print("invalid choice, try again! ")
                        view_choice = input(("would you like to see this students hometown or favorite food?"))
    elif type(stu) == int:
        for x in range(len(queue)):
            if x == stu:
                q = queue[stu ]
                print(f'{x}. {q["name"]}')
                view_choice= input(("would you like to see this students hometown or favorite food? "))
                while view_choice != 'hometown' or view_choice != "favorite food":
                    if view_choice == 'hometown':
                        print(q['hometown'])
                        return
                    elif view_choice == 'favorite food':
                        print(q['favorite_food'])
                        return
                    else:
                        print("invalid choice, try again! ")
                        view_choice = input(("would you like to see this students hometown or favorite food?"))
                break
        print()
    return ""
def get_new_student():
    print()
    new_student = {'name': "", 'hometown': "", 'favorite_food': ""}
    new_name = input("enter the new students name ")
    new_hometown = input("enter the new students hometown ")
    new_food = input("enter the new students favorite food ")
    new_student['name'] = new_name
    new_student["hometown"] = new_hometown
    new_student["favorite_food"] = new_food
    print(new_student)
    return queue.append(new_student)

print()
queue = [student_julia, student_tina, student_Klaus]
user_choice = True
while user_choice:
    user_input = input("select one of the following options\nadd - to create a new student"
                       "\nview - to look at existing students"
                       "\nquit - to exit the program ")
    stu_name = input("enter a students name you would like to learn more about ")
    list_names(stu_name)
    if user_input == "add":
        get_new_student()  # makes a call to the function to add a new student
    elif user_input == "view":# lists all the current dictionaries
        print(list_names(user_input))
        student_num = int(input("which student file would you like to access? select the relevant number "))
        if student_num > len(queue) or student_num <=0 :
            print("not a valid number! try again ")
        else:
            list_names(student_num)
    elif user_input == "quit":
        print("Goodbye")
        exit(1)
    else:
        print("not a valid input! ")

    print()


from functions import new_student, list_student, find_student, update_student, delete_student
from data.data import save_csv, load_csv
inventory = []

while True:
    print("\n--- MENU ---")
    print("1. Add student")
    print("2. List student")
    print("3. Find student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Save CSV")
    print("7. Load CSV")
    print("0. Exit")

    option = input("Choose an option: ")

    if option == "1":
        new_student(inventory)

    elif option == "2":
        list_student(inventory)

    elif option == "3":
        name = input("Type student name: ")
        result = find_student(inventory, id, name)
        if result:
            print(result)
        else:
            print("Student not found")

    elif option == "4":
        name = input("Type the student is name: ")
        id = input("Type student ID: ")
        age = input("New age (leave empty if no change): ")
        program = input("New program (leave empty if no change): ")
        status = input("New status (leave empty if no change): ")

        age = int(age) if age else None
        program= program if program else None
        status= status if status else None

        update_student(inventory, name, id, age, program, status)

    elif option == "5":
        name = input("Enter student name: ")
        delete_student(inventory, name)


    elif option == "6":
        save_csv(inventory, "data/data.csv")
        print(inventory)
    
    elif option == "7":
        inventory = load_csv("data/data.csv")
        print(inventory)
    
    elif option == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option")



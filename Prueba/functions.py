"""
This folder will save the CRUD functions
"""

#add new student function
def new_student(inventory):
    student_id = input("Student ID: ")
    student_name = input("Student name: ")
    student_age = input("Student age: ")
    student_program = input("Student program: Backend, Frontend, Full- stack: ")
    student_status = input("Student state: active, inactive ")

    students = {
        "id" : student_id,
        "name" : student_name,
        "age" : student_age,
        "program" : student_program,
        "status" : student_status
    }

    inventory.append(students)
    print("A new student have been added succesfully!")

#list students function
def list_student(inventory):
    for students in inventory:
        print(students)

#find an student with their ID or name function
def find_student(inventory, id, name):
    for students in inventory:
        if students["name"] == name:
            return students
        elif students["id"] == id:
            return students
    return None

#Update information function
def update_student(inventory, name, id, new_age=None, new_program=None, new_status=None,):
    for students in inventory:
        if students["name"] == name and students["id"] == id:

                if new_age is not None:
                    students["age"] = int(new_age)
                
                if new_program is not None:
                    students["program"] = new_program
                
                if new_status is not None:
                    students["status"] = new_status
    
                print("Student updated successfully!")
                return
    print("Student not found")

#Delete a student function
def delete_student(inventory, name):
    for students in inventory:
        if students["name"] == name :
            inventory.remove(students)
            print("Student deleted succesfully!")
            return
    print("Student not found")




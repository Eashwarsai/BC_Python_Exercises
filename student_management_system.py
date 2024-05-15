# Define a dictionary to store student details
student_details = {}

# Function to add a new student
def add_student(name, age, grade):
    global student_details
    student_id = len(student_details) + 1  # Generate a unique student ID
    student_details[student_id] = {'name': name, 'age': age, 'grade': grade}
    return student_id

# Function to update student details
def update_student(student_id, new_info):
    global student_details
    if student_id in student_details:
        student_details[student_id].update(new_info)
        return True
    return False

# Function to remove a student
def remove_student(student_id):
    global student_details
    if student_id in student_details:
        del student_details[student_id]
        return True
    return False

# Function to retrieve details of a student by ID
def get_student_details(student_id):
    return student_details.get(student_id)

# Function to retrieve a list of students by grade
def get_students_by_grade(grade):
    return [value for value in student_details.values() if value['grade'] == grade]

# Function to retrieve details of all students
def get_all_students():
    return student_details

# Main program loop
flag = True
while flag:
    print('Enter 0 to exit')
    print('Enter 1 to get all students')
    print('Enter 2 to add a student')
    print('Enter 3 to update student details')
    print('Enter 4 to remove a student')
    print('Enter 5 to get student details by ID')
    print('Enter 6 to get students by grade')

    choice = int(input('Enter your choice: '))

    if choice == 0:
        flag = False
        print('Exiting...')
    elif choice == 1:
        print('All students:', get_all_students())
    elif choice == 2:
        name = input('Enter student name: ')
        age = int(input('Enter student age: '))
        grade = input('Enter student grade: ')
        student_id = add_student(name, age, grade)
        print('Student added with ID:', student_id)
    elif choice == 3:
        student_id = int(input('Enter student ID to update: '))
        new_info = {}
        new_name = input('Enter new name (leave blank to keep unchanged): ')
        new_age = input('Enter new age (leave blank to keep unchanged): ')
        new_grade = input('Enter new grade (leave blank to keep unchanged): ')
        if new_name:
            new_info['name'] = new_name
        if new_age:
            new_info['age'] = int(new_age)
        if new_grade:
            new_info['grade'] = new_grade
        success = update_student(student_id, new_info)
        if success:
            print('Student details updated successfully.')
        else:
            print('Student not found.')
    elif choice == 4:
        student_id = int(input('Enter student ID to remove: '))
        success = remove_student(student_id)
        if success:
            print('Student removed successfully.')
        else:
            print('Student not found.')
    elif choice == 5:
        student_id = int(input('Enter student ID to get details: '))
        required_student_details = get_student_details(student_id)
        if required_student_details:
            print('Student details:', required_student_details)
        else:
            print('Student not found.')
    elif choice == 6:
        grade = input('Enter grade to get students: ')
        students = get_students_by_grade(grade)
        if students:
            print('Students in grade', grade + ':', students)
        else:
            print('No students found in grade', grade)
    else:
        print('Invalid choice. Please enter a valid option.')

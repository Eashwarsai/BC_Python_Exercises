class Student:
    """Class to represent a student."""

    def __init__(self, name, age, grade):
        """Initialize a Student object with name, age, and grade."""
        self.name = name
        self.age = age
        self.grade = grade

    def update_details(self, new_name=None, new_age=None, new_grade=None):
        """Update student details."""
        if new_name:
            self.name = new_name
        if new_age:
            self.age = new_age
        if new_grade:
            self.grade = new_grade

    def __str__(self):
        """Return a string representation of the student."""
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManager:
    """Class to manage students."""

    def __init__(self):
        """Initialize StudentManager object."""
        self.students = {}

    def add_student(self, name, age, grade):
        """Add a new student to the student list."""
        student = Student(name, age, grade)
        student_id = len(self.students) + 1
        self.students[student_id] = student
        return student_id

    def update_student(self, student_id, new_name=None, new_age=None, new_grade=None):
        """Update details of an existing student."""
        student = self.students.get(student_id)
        if student:
            student.update_details(new_name, new_age, new_grade)
            return True
        return False

    def remove_student(self, student_id):
        """Remove a student from the student list."""
        student = self.students.pop(student_id, None)
        return student is not None

    def get_student_details(self, student_id):
        """Get details of a specific student."""
        return self.students.get(student_id)

    def get_students_by_grade(self, grade):
        """Get a list of students in a specific grade."""
        return [student for student in self.students.values() if student.grade == grade]

    def get_all_students(self):
        """Get details of all students."""
        return self.students


# Main program loop
student_manager = StudentManager()
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
        print('All students:')
        for student in student_manager.get_all_students().values():
            print(student)
    elif choice == 2:
        name = input('Enter student name: ')
        age = int(input('Enter student age: '))
        grade = input('Enter student grade: ')
        student_id = student_manager.add_student(name, age, grade)
        print('Student added with ID:', student_id)
    elif choice == 3:
        student_id = int(input('Enter student ID to update: '))
        new_name = input('Enter new name (leave blank to keep unchanged): ')
        new_age = input('Enter new age (leave blank to keep unchanged): ')
        new_grade = input('Enter new grade (leave blank to keep unchanged): ')
        success = student_manager.update_student(student_id, new_name, new_age, new_grade)
        if success:
            print('Student details updated successfully.')
        else:
            print('Student not found.')
    elif choice == 4:
        student_id = int(input('Enter student ID to remove: '))
        success = student_manager.remove_student(student_id)
        if success:
            print('Student removed successfully.')
        else:
            print('Student not found.')
    elif choice == 5:
        student_id = int(input('Enter student ID to get details: '))
        student = student_manager.get_student_details(student_id)
        if student:
            print('Student details:', student)
        else:
            print('Student not found.')
    elif choice == 6:
        grade = input('Enter grade to get students: ')
        students = student_manager.get_students_by_grade(grade)
        if students:
            print('Students in grade', grade + ':')
            for student in students:
                print(student)
        else:
            print('No students found in grade', grade)
    else:
        print('Invalid choice. Please enter a valid option.')

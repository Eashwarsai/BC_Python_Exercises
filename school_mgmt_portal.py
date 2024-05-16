# Define inner function to manage school admissions
def school_management():
    # Initialize total students count
    total_students = 0
    # Check if admitting a new student exceeds the capacity
    def check_capacity():
        return total_students < 10

    # Admit a new student and update the count
    def admit():
        nonlocal total_students
        total_students += 1

    # Reject admission if capacity is reached
    def reject():
        return "Admission failed: Maximum capacity reached (10 students)."

    # Function to admit a student, utilizing inner functions
    def admit_student():
        nonlocal total_students

        if check_capacity():
            admit()
            return "Student admitted successfully."
        else:
            return reject()

    # Return the function for admitting students
    return admit_student

# Create a function for admitting students
admit_student = school_management()

print(admit_student())  
print(admit_student())
print(admit_student())  
print(admit_student()) 
print(admit_student()) 
print(admit_student())
print(admit_student())  
print(admit_student())
print(admit_student())  
print(admit_student()) 
print(admit_student())  

import os  # Importing the os module for file operations

class ContextManager:  
    """
    A context manager for file handling.
    """

    def __init__(self, file_name, mode):  
        """
        Initializes the ContextManager.

        Args:
            file_name (str): The name of the file.
            mode (str): The mode in which the file should be opened.
        """
        self.filename = file_name  
        self.mode = mode  
        self.file = None  

    def __enter__(self):  
        """
        Enters the context. Opens the file and returns it.

        Returns:
            file: The opened file object.
        """
        self.file = open(self.filename, self.mode)  
        return self.file  

    def __exit__(self, exc_type, exc_value, exc_traceback):  
        """
        Exits the context. Closes the file.

        Args:
            exc_type: The exception type.
            exc_value: The exception value.
            exc_traceback: The traceback information.
        """
        self.file.close()  

def read_notes(file_name):  
    """
    Reads notes from the specified file.

    Args:
        file_name (str): The name of the file.

    Returns:
        None
    """
    if os.path.exists(file_name):  
        with ContextManager(file_name, "r") as file:  
            notes = file.read()  
            if notes:  
                print("Existing notes:\n", notes)  
            else:
                print("No notes found")  
    else:
        print("No notes found")  

def write_note(file_name, note):  
    """
    Writes a note to the specified file.

    Args:
        file_name (str): The name of the file.
        note (str): The note to be written.

    Returns:
        None
    """
    with ContextManager(file_name, "w") as file:  
        file.write(note)  
    print("Note written successfully")  

def append_note(file_name, note):  
    """
    Appends a note to the specified file.

    Args:
        file_name (str): The name of the file.
        note (str): The note to be appended.

    Returns:
        None
    """
    if os.path.exists(file_name):  
        with ContextManager(file_name, "a") as file:  
            file.write("\n" + note)  
        print("Note appended successfully")  
    else:
        print("No existing file to append. Creating a new one.")  
        write_note(file_name, note)  

def main():  
    """
    Main function to handle user interaction.

    Returns:
        None
    """
    file_name = "notes.txt"  
    flag = True  
    while flag:  
        print('Enter 1 to read notes from the file.')
        print('Enter 2 to write a new note to the file.')
        print('Enter 3 to append a note to the existing file')
        print('Enter 4 to exit.')
        choice = int(input('Enter your choice: '))  

        if choice == 1:  
            read_notes(file_name)  

        elif choice == 2:  
            note = input("Enter your note: ")  
            write_note(file_name, note)  

        elif choice == 3:  
            note = input("Enter the note to append: ")  
            append_note(file_name, note)  

        elif choice == 4:  
            print("Exiting the application")  
            flag = False  

        else:
            print("Incorrect input")  

if __name__ == "__main__":  
    main()  

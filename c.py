
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Certificate:
    def __init__(self, person, degree, date, institution):
        self.person = person
        self.degree = degree
        self.date = date
        self.institution = institution
        self.verification_results = []

    def verify(self, person_name, degree, date, institution):
        """
        Verify the authenticity of the certificate by comparing the input values with the stored values.
        """
        verification_result = (
            self.person.name == person_name and
            self.degree == degree and
            self.date == date and
            self.institution == institution
        )
        self.verification_results.append(verification_result)
        return verification_result
    def get_verification_history(self):
        """
        Get the verification history for the certificate.
        """
        return self.verification_results
    
    def get_entered_data(self):
        """
        Get the entered data for the certificate.
        """
        return {
            'person_name': self.person.name,
            'degree': self.degree,
            'date': self.date,
            'institution': self.institution
        }

# List to store registered persons
registered_persons = []

# Example usage:

def get_input(message):
    """
    Helper function to get input from the user.
    """
    try:
        return input(message)
    except KeyboardInterrupt:
        print("\nProgram terminated.")
        exit()

def register_person():
    """
    Register a new person.
    """
    print("\nRegister a new person:")
    name = get_input("Name: ")

    # Create a person object
    person = Person(name)

    # Add the person to the registered persons list
    registered_persons.append(person)
    print("Registration successful.")

def show_registered_persons():
    """
    Show the stored data of registered persons.
    """
    print("\nRegistered persons:")
    for i, person in enumerate(registered_persons, start=1):
        print(f"{i}. {person}")

# Greet the person
print("Welcome! Please provide your name.")
name = get_input("Name: ")

# Check if the person is already registered
registered = False
for person in registered_persons:
    if person.name == name:
        registered = True
        break

# Register the person if not already registered
if not registered:
    register_person()

# Create a certificate for the person
person = registered_persons[0]  # Assuming only one person is registered
certificate = Certificate(person, "Bachelor of Science", "2021-05-01", "Example University")

# Ask for certificate verification, showing stored data, or quitting the program
while True:
    print("\nChoose an option:")
    print("1. Verify certificate")
    print("2. Show stored data")
    print("3. Quit")

    choice = get_input("Choice: ")

    if choice == "1":
        # Ask for certificate details and verify
        print("\nPlease provide the details for certificate verification.")
        degree = get_input("Degree: ")
        date = get_input("Date: ")
        institution = get_input("Institution: ")

        # Verify the certificate
        print("Certificate verification:", certificate.verify(person.name, degree, date, institution))
    elif choice == "2":
        # Show the stored data of registered persons
        show_registered_persons()
    elif choice == "3":
        print("Program terminated.")
        break
    else:
        print("Invalid choice. Please try again.")

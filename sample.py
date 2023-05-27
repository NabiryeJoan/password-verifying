import json


class Certificate:
    def __init__(self, degree_name, year_completed):
        self.degree_name = degree_name
        self.year_completed = year_completed

    def __str__(self):
        return f"Degree Name: {self.degree_name}\nYear Completed: {self.year_completed}"

    def to_dict(self):
        return {
            "degree_name": self.degree_name,
            "year_completed": self.year_completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["degree_name"], data["year_completed"])


class CertificateRegistry:
    def __init__(self):
        self.certificates = []

    def register_certificate(self, degree_name, year_completed):
        certificate = Certificate(degree_name, year_completed)
        self.certificates.append(certificate)
        print("Certificate registered successfully.")

    def verify_certificate(self, degree_name, year_completed):
        for certificate in self.certificates:
            if certificate.degree_name == degree_name and certificate.year_completed == year_completed:
                print("Certificate found:")
                print(certificate)
                return
        print("Certificate not found.")

    def print_all_certificates(self):
        if len(self.certificates) == 0:
            print("No certificates registered.")
        else:
            print("Registered Certificates:")
            for certificate in self.certificates:
                print(certificate)

    def save_certificates(self, filename):
        data = [certificate.to_dict() for certificate in self.certificates]
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Certificates saved to {filename}.")

    def load_certificates(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.certificates = [Certificate.from_dict(certificate_data) for certificate_data in data]
            print(f"Certificates loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def clear_certificates(self):
        self.certificates = []
        print("All certificates cleared.")


def main():
    registry = CertificateRegistry()

    while True:
        print("\n===== Certificate Registration Program =====")
        print("1. Register a Certificate")
        print("2. Verify a Certificate")
        print("3. View All Certificates")
        print("4. Save Certificates")
        print("5. Load Certificates")
        print("6. Clear All Certificates")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            degree_name = input("Enter the degree name: ")
            year_completed = input("Enter the year of completion: ")
            registry.register_certificate(degree_name, year_completed)
        elif choice == "2":
            degree_name = input("Enter the degree name to verify: ")
            year_completed = input("Enter the year of completion to verify: ")
            registry.verify_certificate(degree_name, year_completed)
        elif choice == "3":
            registry.print_all_certificates()
        elif choice == "4":
            filename = input("Enter the filename to save certificates (e.g., certificates.json): ")
            registry.save_certificates(filename)
        elif choice == "5":
            filename = input("Enter the filename to load certificates from: ")
            registry.load_certificates(filename)
        elif choice == "6":
            confirm = input("Are you sure you want to clear all certificates? (y/n): ")
            if confirm.lower() == "y":
                registry.clear_certificates()

import json

FILENAME = "grades.json"


class StudentRegistry:

    def __init__(self, raw_data: dict):
        self.records = raw_data

    def student_exists(self, name: str) -> bool:
        return name in self.records

    def add_or_update(self, name: str, grade: float) -> None:
        self.records[name] = grade

    def delete(self, name: str) -> None:
        if self.student_exists(name):
            del self.records[name]


def load_grades() -> dict:
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_grades(data: dict) -> None:
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except IOError as error:
        print(f"Error saving data: {error}")


def add_student_grade(registry: StudentRegistry) -> None:
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    score_input = input(f"Enter grade for {name}: ")

    try:
        score = float(score_input)
        if not (0 <= score <= 100):
            print("Grade must be between 0 and 100!")
            return

        registry.add_or_update(name, score)
        save_grades(registry.records)
        print(f"Successfully saved {name}'s grade.")
    except ValueError:
        print("Error: You must enter a valid numeric grade!")


def view_all_grades(registry: StudentRegistry) -> None:
    if not registry.records:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for name, grade in registry.records.items():
        print(f"Student: {name} | Grade: {grade}")


def delete_student_grade(registry: StudentRegistry) -> None:
    name = input("Enter student name to delete: ").strip()

    if registry.student_exists(name):
        registry.delete(name)
        save_grades(registry.records)
        print(f"Successfully deleted {name}'s record.")
    else:
        print(f"Error: Student '{name}' not found in the records.")


def main_menu() -> None:
    raw_data = load_grades()
    registry = StudentRegistry(raw_data)

    while True:
        print("\n=== IT Step Grade Manager ===")
        print("1. Add/Update Student Grade")
        print("2. View All Grades")
        print("3. Delete Student Record")
        print("4. Exit Application")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            add_student_grade(registry)
        elif choice == "2":
            view_all_grades(registry)
        elif choice == "3":
            delete_student_grade(registry)
        elif choice == "4":
            print("Exiting program. Process killed. Goodbye!")
            break
        else:
            print("Invalid input! Please type 1, 2, 3, or 4.")


if __name__ == "__main__":
    main_menu()


if __name__ == "__main__":
    main_menu()

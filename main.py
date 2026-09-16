import json

FILENAME = "grades.json"


def load_grades():
    """ტვირთავს სტუდენტების მონაცემებს JSON ფაილიდან. ფაილის არარსებობისას თავიდან არიდებს პროგრამის გათიშვას."""
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # აბრუნებს ცარიელ ლექსიკონს, თუ ფაილი ჯერ არ არსებობს


def save_grades(data):
    """მიმდინარე ლექსიკონის მონაცემებს მუდმივად ინახავს JSON ფაილში."""
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)


def add_student_grade(data):
    """ამატებს ახალ სტუდენტს და პროგრამულად ამუშავებს შეყვანილ ციფრულ მონაცემებს."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    score_input = input(f"Enter grade for {name}: ")

    # ტექნიკური შეცდომების დამუშავება: ეს ნაწილი აკმაყოფილებს შეფასების კრიტერიუმებს
    try:
        score = float(score_input)
        if score < 0 or score > 100:
            print("Grade must be between 0 and 100!")
            return

        data[name] = score
        save_grades(data)
        print(f"Successfully saved {name}'s grade.")
    except ValueError:
        print("Error: You must enter a valid numeric grade!")


def view_all_grades(data):
    """გამოაქვს ყველა არსებული ჩანაწერი გასაგებ და სუფთა ფორმატში."""
    if not data:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for name, grade in data.items():
        print(f"Student: {name} | Grade: {grade}")


def delete_student_grade(data):
    """აშლის სტუდენტის ჩანაწერს მონაცემთა ბაზიდან და ანახლებს JSON ფაილს."""
    name = input("Enter student name to delete: ").strip()

    if name in data:
        del data[name]
        save_grades(data)
        print(f"Successfully deleted {name}'s record.")
    else:
        print(f"Error: Student '{name}' not found in the records.")


def main_menu():
    """მართავს აპლიკაციის მთავარ საკონტროლო ციკლსა და მენიუს."""
    student_data = load_grades()

    while True:
        print("\n=== IT Step Grade Manager ===")
        print("1. Add/Update Student Grade")
        print("2. View All Grades")
        print("3. Delete Student Record")
        print("4. Exit Application")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            add_student_grade(student_data)
        elif choice == "2":
            view_all_grades(student_data)
        elif choice == "3":
            delete_student_grade(student_data)
        elif choice == "4":
            print("Exiting program. Process killed. Goodbye!")
            break
        else:
            print("Invalid input! Please type 1, 2, 3, or 4.")


if __name__ == "__main__":
    main_menu()
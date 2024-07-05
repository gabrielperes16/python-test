def decoration(msg):
    print("\033[32m==\033[m" * 30)
    print(msg)
    print("\033[32m==\033[m" * 30)

def validator(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [1, 2, 3]:
                return value
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    print("\033[32m==" * 30)
    print('''                1- View registered people
                2- Register new person
                3- Exit the system\033[m'''.center(100))
    print("\033[32m==\033[m" * 30)

def view_registered_people(people):
    if not people:
        print("No people registered yet.")
    else:
        print('\033[32m=='*50)
        print("THE LIST OF REGISTERED PEOPLE IS:".center(94))
        print('=='*50)
        for person in people:
            print(f"NAME: {person['name']}")
            print(f"AGE: {person['age']}")
            print(f"GENDER: {person['gender']}")
            print('=='*50)
    print("\033[m")

def register_new_person(people):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    while True:
        gender = input("Enter your gender [MALE] or [FEMALE]: ").upper().strip()
        if gender in ['MALE', 'FEMALE']:
            break
        else:
            print("Error: enter correctly!")

    person = {
        'name': name,
        'age': age,
        'gender': gender
    }
    people.append(person)
    print("Data successfully recorded:", person)

people = []

while True:
    menu()
    choice = validator("Your Choice: ")

    if choice == 1:
        view_registered_people(people)

    elif choice == 2:
        register_new_person(people)

    elif choice == 3:
        print("\033[32mEND OF PROGRAM. SEE YOU LATER!\033[m")
        print("==" * 30)
        break

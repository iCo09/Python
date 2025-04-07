import json

def add_person():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    person = {
        'name': name,
        'age': age,
        'email': email
    }
    return person

def delete_contact(people):
    display_contacts(people)
    while True:
        number = input("Enter a number to delete a contact: ")
        try: 
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number. Please try again.")
            else:
                break
        except:
            print("Invalid input. Please enter a number.")
            
    people.pop(number - 1)
    print("Contact deleted successfully!")

def display_contacts(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person['name'], '|', person['age'], '|', person['email'])

def search(people):
    search_name = input("Search for a contact by name: ").lower()
    results = []
    for person in people:
        name = person['name']
        if search_name in name.lower():
            results.append(person)

    display_contacts(results)   

    
print('Welcome to the Contact Management System!')

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print("Contact list size:", len(people))
    command = input("You can 'Add','Delete','Search' or 'Q': ").lower()
    if command == 'add':
        person = add_person()
        people.append(person)
        print("Person added successfully!")
    elif command == 'delete':
        delete_contact(people)
    elif command == 'search':
        search(people)
    elif command == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid command. Please enter 'Add', 'Delete', or 'Search'.")


with open("contacts.json", "w") as f:
    json.dump({"contacts":people}, f)
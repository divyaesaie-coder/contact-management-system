#Program to create a contact management system with add, display, and delete contact features using text files.
# -------- ADD CONTACTS --------
while True:
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    with open("contacts.txt", "a") as f:
        f.write(name + "," + phone + "\n")

    if input("Add more? (yes/no): ") != "yes":
        break


# -------- MENU --------
while True:
    print("\n1) Show contacts")
    print("2) Delete a contact")
    print("3) Exit")

    ch = input("Choose: ")

    # SHOW CONTACTS
    if ch == "1":
        with open("contacts.txt", "r") as f:
            print(f.read())

    # DELETE CONTACT (by phone number)
    elif ch == "2":
        phone_to_delete = input("Enter phone number to delete: ")

        with open("contacts.txt", "r") as f:
            lines = f.readlines()

        with open("contacts.txt", "w") as f:
            for line in lines:
                if phone_to_delete not in line:
                    f.write(line)

        print("Contact deleted (if it existed)")

    # EXIT
    elif ch == "3":
        print("Goodbye!")
        break


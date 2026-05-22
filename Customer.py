# customer.py
# This module handles all customer-related functions
# for the Car Wash & Service Booking Management System.

CUSTOMER_FILE = "customers.txt"


# ==================================================
# Function: add_customer()
# ==================================================
def add_customer():
    try:
        # Get valid customer ID (or cancel anytime)
        while True:
            customer_id = input("Enter Customer ID (e.g. C001) or type 'cancel': ").strip()

            if customer_id.lower() == "cancel":
                print("Operation cancelled.")
                return

            customer_id = customer_id[0].upper() + customer_id[1:] if len(customer_id) > 0 else customer_id

            if not (customer_id.startswith("C") and customer_id[1:].isdigit()):
                print("Error: Invalid format. Must be C followed by numbers (e.g. C001) and cannot be empty.")
                continue

            if customer_exists(customer_id):
                print("Error: Customer ID already exists.")
                continue

            break

        # Name (must not be empty)
        while True:
            name = input("Enter Name or type 'cancel': ").strip()

            if name.lower() == "cancel":
                print("Operation cancelled.")
                return

            if len(name.replace(" ", "")) == 0:
                print("Error: Name cannot be empty.")
                continue

            break

        # Phone
        while True:
            phone = input("Enter Phone or type 'cancel': ").strip()

            if phone.lower() == "cancel":
                print("Operation cancelled.")
                return

            if phone.replace("+", "").isdigit():
                break

            print("Error: Phone must contain only numbers or '+' symbol and cannot be empty.")

        # Email
        while True:
            email = input("Enter Email or type 'cancel': ").strip()

            if email.lower() == "cancel":
                print("Operation cancelled.")
                return

            if "@" in email and email.count("@") == 1:
                break

            print("Error: Email must contain a valid '@' symbol and cannot be empty.")

        with open(CUSTOMER_FILE, "a") as file:
            file.write(customer_id + "|" + name + "|" + phone + "|" + email + "\n")

        print("Customer added successfully.")

    except:
        print("Error adding customer.")


# ==================================================
# Function: view_customers()
# ==================================================
def view_customers():
    try:
        file = open(CUSTOMER_FILE, "r")
        print("\n===== CUSTOMER LIST =====")

        for line in file:
            data = line.strip().split("|")
            if len(data) == 4:
                print("Customer ID :", data[0])
                print("Name        :", data[1])
                print("Phone       :", data[2])
                print("Email       :", data[3])
                print("--------------------------")

        file.close()

    except FileNotFoundError:
        print("Customer file not found.")
    except:
        print("Error reading customer file.")


# ==================================================
# Function: search_customer()
# ==================================================
def search_customer():
    try:
        customer_id = input("Enter Customer ID (or cancel): ").strip()

        if customer_id.lower() == "cancel":
            print("Operation cancelled.")
            return

        customer_id = customer_id[0].upper() + customer_id[1:] if len(customer_id) > 0 else customer_id

        found = False
        file = open(CUSTOMER_FILE, "r")

        for line in file:
            data = line.strip().split("|")
            if data[0] == customer_id:
                found = True
                print("\nCustomer Found")
                print("Customer ID :", data[0])
                print("Name        :", data[1])
                print("Phone       :", data[2])
                print("Email       :", data[3])
                break

        file.close()

        if not found:
            print("Customer not found.")

    except:
        print("Error searching customer.")


# ==================================================
# Function: update_customer()
# ==================================================
def update_customer():
    try:
        customer_id = input("Enter Customer ID (or cancel): ").strip()

        if customer_id.lower() == "cancel":
            print("Operation cancelled.")
            return

        customer_id = customer_id[0].upper() + customer_id[1:] if len(customer_id) > 0 else customer_id

        updated_data = []
        found = False

        file = open(CUSTOMER_FILE, "r")

        for line in file:
            data = line.strip().split("|")

            if data[0] == customer_id:
                found = True
                print("Enter New Details (or cancel)")

                while True:
                    new_name = input("Enter New Name (or type 'cancel'): ").strip()

                    if new_name.lower() == "cancel":
                        print("Operation cancelled.")
                        file.close()
                        return

                    if len(new_name.replace(" ", "")) == 0:
                        print("Error: Name cannot be empty.")
                        continue

                    break

                while True:
                    new_phone = input("Enter New Phone (or type 'cancel'): ").strip()

                    if new_phone.lower() == "cancel":
                        print("Operation cancelled.")
                        file.close()
                        return

                    if new_phone.replace("+", "").isdigit():
                        break

                    print("Error: Phone must contain only numbers or '+' symbol and cannot be empty.")

                while True:
                    new_email = input("Enter New Email (or type 'cancel'): ").strip()

                    if new_email.lower() == "cancel":
                        print("Operation cancelled.")
                        file.close()
                        return

                    if "@" in new_email and new_email.count("@") == 1:
                        break

                    if len(new_email.replace(" ", "")) == 0:
                        print("Error: Email cannot be empty.")
                        continue

                    print("Error: Email must contain a valid '@' symbol and cannot be empty.")

                updated_data.append(customer_id + "|" + new_name + "|" + new_phone + "|" + new_email + "\n")

            else:
                updated_data.append(line)

        file.close()

        file = open(CUSTOMER_FILE, "w")
        file.writelines(updated_data)
        file.close()

        if found:
            print("Customer updated successfully.")
        else:
            print("Customer not found.")

    except:
        print("Error updating customer.")


# ==================================================
# Function: delete_customer()
# ==================================================
def delete_customer():
    try:
        customer_id = input("Enter Customer ID (or cancel): ").strip()

        if customer_id.lower() == "cancel":
            print("Operation cancelled.")
            return

        customer_id = customer_id[0].upper() + customer_id[1:] if len(customer_id) > 0 else customer_id

        updated_data = []
        found = False

        file = open(CUSTOMER_FILE, "r")

        for line in file:
            data = line.strip().split("|")

            if data[0] == customer_id:
                found = True
            else:
                updated_data.append(line)

        file.close()

        file = open(CUSTOMER_FILE, "w")
        file.writelines(updated_data)
        file.close()

        if found:
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")

    except:
        print("Error deleting customer.")


# ==================================================
# Function: customer_exists()
# ==================================================
def customer_exists(customer_id):
    try:
        file = open(CUSTOMER_FILE, "r")

        for line in file:
            data = line.strip().split("|")
            if data[0] == customer_id:
                file.close()
                return True

        file.close()
        return False

    except:
        return False


# ==================================================
# MENU
# ==================================================
def customer_menu():
    while True:
        print("\n===== CUSTOMER MENU =====")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("0. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            update_customer()
        elif choice == "5":
            delete_customer()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    customer_menu()
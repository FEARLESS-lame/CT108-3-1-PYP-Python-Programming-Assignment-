# Module File Name: customer.py
# Coder: Pang Kai Jie TP144452
# This module handles all customer-related functions for the Car Wash & Service Booking Management System.
# User can cancel the process at any moment
# Primary Key for the customer_id is formated for better and more organized storage
CUSTOMER_FILE = "customers.txt" # File to store customer data
# ==================================================
# CUSTOMER MENU
# ==================================================
def customer_menu():
    CUSTOMER_FILE = "customers.txt" # File to store customer data
    while True:
        # Menu Overview (Available Choices)
        print("\n===== CUSTOMER MENU =====")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("0. Back")

        choice = input("Enter choice: ")
        # Connection to each of the sub-module
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
# ==================================================
# Function: Add Customer to Saved File
# ==================================================
def add_customer():
    CUSTOMER_FILE = "customers.txt" # File to store customer data
    try:
        # Get valid customer ID (or cancel anytime)
        while True:
            customer_id = input("Enter Customer ID (e.g. C001) or type 'cancel': ").strip()
            # Cancel operation if user types 'cancel'
            if customer_id.lower() == "cancel":
                print("Operation cancelled.")
                return
            # Ensure first character is uppercase and rest are as entered
            customer_id = customer_id[0].upper() + customer_id[1:] if len(customer_id) > 0 else customer_id
            # Validate format: must start with 'C' followed by digits and cannot be empty
            if not (customer_id.startswith("C") and customer_id[1:].isdigit()):
                print("Error: Invalid format. Must be C followed by numbers (e.g. C001) and cannot be empty.")
                continue
            # Check for duplicate customer ID
            if customer_exists(customer_id):
                print("Error: Customer ID already exists.")
                continue
            
            break

        # Name (must not be empty)
        while True:
            name = input("Enter Name or type 'cancel': ").strip()
            # Cancel operation if user types 'cancel'
            if name.lower() == "cancel":
                print("Operation cancelled.")
                return
            # Ensure name is not empty (ignoring spaces)
            if len(name.replace(" ", "")) == 0:
                print("Error: Name cannot be empty.")
                continue

            break

        # Phone
        while True:
            phone = input("Enter Phone or type 'cancel': ").strip()
            # Cancel operation if user types 'cancel'
            if phone.lower() == "cancel":
                print("Operation cancelled.")
                return
            # Validate phone: must contain only digits or '+' and cannot be empty
            if phone.replace("+", "").isdigit():
                break
            print("Error: Phone must contain only numbers or '+' symbol and cannot be empty.")

        # Email
        while True:
            email = input("Enter Email or type 'cancel': ").strip()
            # Cancel operation if user types 'cancel'
            if email.lower() == "cancel":
                print("Operation cancelled.")
                return
            # Validate email: must contain exactly one '@' symbol and cannot be empty
            if "@" in email and email.count("@") == 1:
                break
            print("Error: Email must contain a valid '@' symbol and cannot be empty.")
        # Save customer data to file
        with open(CUSTOMER_FILE, "a") as file:
            file.write(customer_id + "|" + name + "|" + phone + "|" + email + "\n")
        # Confirmation message
        print("Customer added successfully.")

    except:
        print("Error adding customer.")


# ==================================================
# Function: View Customers from Saved File
# ==================================================
def view_customers():
    CUSTOMER_FILE = "customers.txt" # File to store customer data
    try:
        file = open(CUSTOMER_FILE, "r")
        print("\n===== CUSTOMER LIST =====")
        # Read and display each customer in a formatted manner
        for line in file:
            data = line.strip().split("|")
            if len(data) == 4:
                print("Customer ID :", data[0])
                print("Name        :", data[1])
                print("Phone       :", data[2])
                print("Email       :", data[3])
                print("--------------------------")
        # Close the file after reading
        file.close()
    # Handle case where customer file does not exist (Currently Should have the File)
    except FileNotFoundError:
        print("Customer file not found.")
    except:
        print("Error reading customer file.")


# ==================================================
# Function: Search Customer from Saved File
# ==================================================
def search_customer():
    CUSTOMER_FILE = "customers.txt" # File to store customer data
    try:
        customer_id = input("Enter Customer ID (or cancel): ").strip()
        # Cancel operation if user types 'cancel'
        if customer_id.lower() == "cancel":
            print("Operation cancelled.")
            return
        # Ensure first character is uppercase and rest are as entered
        customer_id = customer_id[0].upper() + customer_id[1:] if len(customer_id) > 0 else customer_id
        
        found = False # Flag to track if customer is found
        file = open(CUSTOMER_FILE, "r")
        # Read through the file to find the customer with the given ID
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
        # Close the file after searching
        file.close()
        # If customer is not found, display a message
        if not found:
            print("Customer not found.")

    except:
        print("Error searching customer.")


# ==================================================
# Function: Update Customer from Saved File
# ==================================================
def update_customer():
    CUSTOMER_FILE = "customers.txt" # File to store customer data
    try:
        customer_id = input("Enter Customer ID (or cancel): ").strip()
        # Cancel operation if user types 'cancel'
        if customer_id.lower() == "cancel":
            print("Operation cancelled.")
            return
        # Ensure first character is uppercase and rest are as entered
        customer_id = customer_id[0].upper() + customer_id[1:] if len(customer_id) > 0 else customer_id
        # Read all customer data, update the matching customer, and write back to file
        updated_data = []
        found = False

        file = open(CUSTOMER_FILE, "r")
        # Read through the file to find the customer with the given ID and update their details
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
        # Close the file after reading
        file.close()
        # Write the updated data back to the file
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
# Function: Delete Customer from Saved File
# ==================================================
def delete_customer():
    CUSTOMER_FILE = "customers.txt" # File to store customer data
    try:
        customer_id = input("Enter Customer ID (or cancel): ").strip()
        # Cancel operation if user types 'cancel'
        if customer_id.lower() == "cancel":
            print("Operation cancelled.")
            return

        customer_id = customer_id[0].upper() + customer_id[1:] if len(customer_id) > 0 else customer_id
        # New Cleared Data Format
        updated_data = []
        found = False

        file = open(CUSTOMER_FILE, "r")
        # Find the line of the saved customer data in the txt
        for line in file:
            data = line.strip().split("|")
            if data[0] == customer_id:
                found = True
            else:
                updated_data.append(line)
        # Close the file after reading
        file.close()
        # Write the updated data back to the file
        file = open(CUSTOMER_FILE, "w")
        file.writelines(updated_data)
        file.close()
        # Identification of Delete Status
        if found:
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")
    except:
        print("Error deleting customer.")


# ==================================================
# Function: Check if Customer Exists in Saved File
# ==================================================
def customer_exists(customer_id):
    CUSTOMER_FILE = "customers.txt" # File to store customer data
    try:
        file = open(CUSTOMER_FILE, "r")
        # Read through the file to check if the customer ID already exists
        for line in file:
            data = line.strip().split("|")
            if data[0] == customer_id:
                file.close()
                return True
        file.close()
        return False
    except:
        return False



# Code of Individual Testing
if __name__ == "__main__":
    customer_menu()
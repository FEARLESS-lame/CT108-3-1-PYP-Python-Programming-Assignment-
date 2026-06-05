# ==========================================
# ROLE: SYSTEM ADMINISTRATOR
# SYSTEM: ShinePro Auto Care
# ==========================================
# This module lets the administrator manage service packages and booking slots,
# view all stored data, and generate an overall service report.
# Data format standardised on the pipe '|' separator to match the whole system.
import os

# ----- File name constants -----
SERVICES_FILE = "services.txt"
CUSTOMERS_FILE = "customers.txt"
VEHICLES_FILE = "vehicles.txt"
BOOKINGS_FILE = "bookings.txt"
PAYMENTS_FILE = "payments.txt"


def clear_screen():
    # Clears the terminal screen for a clean UI
    os.system('cls' if os.name == 'nt' else 'clear')


# ==================================================
# SYSTEM ADMINISTRATOR MENU
# ==================================================
def system_admin_menu():
    while True:
        clear_screen()
        print("\n==========================================")
        print("       SHINEPRO SYSTEM ADMINISTRATOR      ")
        print("==========================================")
        print(" 1. Add Service Package")
        print(" 2. Update Service Package")
        print(" 3. Remove Service Package")
        print(" 4. View All Data")
        print(" 5. Generate Report")
        print(" 6. Return to Main Menu")
        print("==========================================")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_service_package()
        elif choice == "2":
            update_service_package()
        elif choice == "3":
            remove_service_package()
        elif choice == "4":
            view_all_data()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice!")
            input("Press Enter to continue...")


# ==================================================
# Helper: check if a Service ID already exists
# ==================================================
def service_exists(service_id):
    try:
        file = open(SERVICES_FILE, "r")
        for line in file:
            data = line.strip().split("|")
            if data[0] == service_id:
                file.close()
                return True
        file.close()
        return False
    except FileNotFoundError:
        return False


# ==================================================
# Function: Add Service Package
# ==================================================
def add_service_package():
    clear_screen()
    print("\n--- ADD SERVICE PACKAGE ---")

    # Service ID (format: S followed by digits, e.g. S01) and must be unique
    while True:
        service_id = input("Enter Service ID (e.g. S01) or 'cancel': ").strip()
        if service_id.lower() == "cancel":
            print("Operation cancelled.")
            input("Press Enter to continue...")
            return
        if len(service_id) > 0:
            service_id = service_id[0].upper() + service_id[1:]
        if not (service_id.startswith("S") and service_id[1:].isdigit()):
            print("Error: Invalid format. Must be 'S' followed by numbers (e.g. S01).")
            continue
        if service_exists(service_id):
            print("Error: Service ID already exists.")
            continue
        break

    # Service name (must not be empty)
    while True:
        service_name = input("Enter service name (or 'cancel'): ").strip()
        if service_name.lower() == "cancel":
            print("Operation cancelled.")
            input("Press Enter to continue...")
            return
        if len(service_name.replace(" ", "")) == 0:
            print("Error: Service name cannot be empty.")
            continue
        break

    # Price (must be a valid non-negative number)
    while True:
        price = input("Enter price (RM) (or 'cancel'): ").strip()
        if price.lower() == "cancel":
            print("Operation cancelled.")
            input("Press Enter to continue...")
            return
        try:
            price_value = float(price)
            if price_value < 0:
                print("Error: Price cannot be negative.")
                continue
            break
        except ValueError:
            print("Error: Price must be a valid number.")

    # Slots (must be a valid non-negative whole number)
    while True:
        slot = input("Enter number of available slots (or 'cancel'): ").strip()
        if slot.lower() == "cancel":
            print("Operation cancelled.")
            input("Press Enter to continue...")
            return
        if slot.isdigit():
            break
        print("Error: Slots must be a whole number (0 or more).")

    try:
        file = open(SERVICES_FILE, "a")
        file.write(service_id + "|" + service_name + "|" + price + "|" + slot + "\n")
        file.close()
        print("Service package added successfully!")
    except Exception as e:
        print(f"Error saving service package: {e}")

    input("Press Enter to continue...")


# ==================================================
# Function: Update Service Package
# ==================================================
def update_service_package():
    clear_screen()
    print("\n--- UPDATE SERVICE PACKAGE ---")

    service_id = input("Enter Service ID to update (or 'cancel'): ").strip()
    if service_id.lower() == "cancel":
        print("Operation cancelled.")
        input("Press Enter to continue...")
        return
    if len(service_id) > 0:
        service_id = service_id[0].upper() + service_id[1:]

    try:
        file = open(SERVICES_FILE, "r")
        services = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: services.txt not found!")
        input("Press Enter to continue...")
        return

    found = False
    updated_data = []

    for service in services:
        data = service.strip().split("|")

        if len(data) >= 1 and data[0] == service_id:
            found = True
            print("Service found! Enter new details.")

            # New name
            while True:
                new_name = input("Enter new service name (or 'cancel'): ").strip()
                if new_name.lower() == "cancel":
                    print("Operation cancelled.")
                    input("Press Enter to continue...")
                    return
                if len(new_name.replace(" ", "")) == 0:
                    print("Error: Service name cannot be empty.")
                    continue
                break

            # New price
            while True:
                new_price = input("Enter new price (RM) (or 'cancel'): ").strip()
                if new_price.lower() == "cancel":
                    print("Operation cancelled.")
                    input("Press Enter to continue...")
                    return
                try:
                    if float(new_price) < 0:
                        print("Error: Price cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Error: Price must be a valid number.")

            # New slots
            while True:
                new_slot = input("Enter new number of slots (or 'cancel'): ").strip()
                if new_slot.lower() == "cancel":
                    print("Operation cancelled.")
                    input("Press Enter to continue...")
                    return
                if new_slot.isdigit():
                    break
                print("Error: Slots must be a whole number (0 or more).")

            updated_data.append(service_id + "|" + new_name + "|" + new_price + "|" + new_slot + "\n")
        else:
            updated_data.append(service)

    if found:
        file = open(SERVICES_FILE, "w")
        file.writelines(updated_data)
        file.close()
        print("Service updated successfully!")
    else:
        print("Service ID not found.")

    input("Press Enter to continue...")


# ==================================================
# Function: Remove Service Package
# ==================================================
def remove_service_package():
    clear_screen()
    print("\n--- REMOVE SERVICE PACKAGE ---")

    service_id = input("Enter Service ID to remove (or 'cancel'): ").strip()
    if service_id.lower() == "cancel":
        print("Operation cancelled.")
        input("Press Enter to continue...")
        return
    if len(service_id) > 0:
        service_id = service_id[0].upper() + service_id[1:]

    try:
        file = open(SERVICES_FILE, "r")
        services = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: services.txt not found!")
        input("Press Enter to continue...")
        return

    found = False
    updated_data = []

    for service in services:
        data = service.strip().split("|")
        if len(data) >= 1 and data[0] == service_id:
            found = True
        else:
            updated_data.append(service)

    if found:
        file = open(SERVICES_FILE, "w")
        file.writelines(updated_data)
        file.close()
        print("Service removed successfully!")
    else:
        print("Service ID not found.")

    input("Press Enter to continue...")


# ==================================================
# Function: View All Data
# ==================================================
def view_all_data():
    clear_screen()
    print("\n--- VIEW ALL DATA ---")

    files = [
        SERVICES_FILE,
        CUSTOMERS_FILE,
        VEHICLES_FILE,
        BOOKINGS_FILE,
        PAYMENTS_FILE
    ]

    for file_name in files:
        print("\n======", file_name, "======")
        try:
            file = open(file_name, "r")
            data = file.read()
            if data.strip() == "":
                print("No data found")
            else:
                print(data)
            file.close()
        except FileNotFoundError:
            print("File not found")

    input("\nPress Enter to continue...")


# ==================================================
# Function: Generate Overall Service Report
# ==================================================
def generate_report():
    clear_screen()

    total_bookings = 0
    total_revenue = 0.0
    total_slots = 0

    # Count total bookings
    try:
        file = open(BOOKINGS_FILE, "r")
        bookings = file.readlines()
        # Only count non-empty lines
        total_bookings = len([b for b in bookings if b.strip() != ""])
        file.close()
    except FileNotFoundError:
        print("Note: Bookings file not found.")

    # Sum revenue from payments. Format: PaymentID|Amount|...
    try:
        file = open(PAYMENTS_FILE, "r")
        for line in file:
            data = line.strip().split("|")
            if len(data) > 1:
                try:
                    total_revenue += float(data[1])
                except ValueError:
                    # Skip malformed amount values instead of crashing
                    pass
        file.close()
    except FileNotFoundError:
        print("Note: Payments file not found.")

    # Sum available slots from services. Format: ServiceID|Name|Price|Slots
    try:
        file = open(SERVICES_FILE, "r")
        for line in file:
            data = line.strip().split("|")
            if len(data) >= 4:
                try:
                    total_slots += int(data[3])
                except ValueError:
                    pass
        file.close()
    except FileNotFoundError:
        print("Note: Services file not found.")

    print("\n==========================================")
    print("        OVERALL SERVICE REPORT            ")
    print("==========================================")
    print(f"Total bookings        : {total_bookings}")
    print(f"Total revenue         : RM {total_revenue:.2f}")
    print(f"Total available slots : {total_slots}")
    print("==========================================")

    input("\nPress Enter to continue...")


# Code of Individual Testing
if __name__ == "__main__":
    system_admin_menu()
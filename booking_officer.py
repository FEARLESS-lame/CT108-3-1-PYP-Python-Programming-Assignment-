# ==========================================
# ROLE: BOOKING OFFICER
# SYSTEM: ShinePro Auto Care
# ==========================================
import os
from datetime import datetime

def clear_screen():
    # Clears the terminal screen for a clean UI
    os.system('cls' if os.name == 'nt' else 'clear')

def booking_officer_menu():
    is_running = True
    while is_running:
        clear_screen()
        print("\n==========================================")
        print("       SHINEPRO BOOKING OFFICER MENU      ")
        print("==========================================")
        print(" 1. Register New Customer & Vehicle")
        print(" 2. Make a Service Booking")
        print(" 3. Cancel / Reschedule Booking")
        print(" 4. View Booking Schedule & History")
        print(" 5. Return to Main Menu")
        print("==========================================")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            register_customer()
        elif choice == "2":
            make_booking()
        elif choice == "3":
            manage_booking()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            print("Returning to Main Menu...")
            is_running = False
        else:
            print("Invalid input! Please enter a number between 1 and 5.")
            input("Press Enter to continue...")

def register_customer():
    clear_screen()
    print("\n--- NEW CUSTOMER REGISTRATION ---")
    
    # Auto-Generate Customer ID
    cust_id = "C001" 
    try:
        file = open("customers.txt", "r")
        lines = file.readlines()
        file.close()
        
        if len(lines) > 0:
            last_line = lines[-1]
            last_id = last_line.split("|")[0].strip()
            if last_id.startswith("C") and last_id[1:].isdigit():
                new_num = int(last_id[1:]) + 1
                cust_id = f"C{new_num:03d}" 
    except FileNotFoundError:
        pass 
        
    print(f"Assigning new Customer ID: {cust_id}")

    name = input("Enter Customer Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    
    # Allow an optional leading '+' (international format), matching customer.py rules
    if not phone.replace("+", "").isdigit():
        print("Error: Phone number must contain only numbers or a '+' symbol!")
        input("Press Enter to return...")
        return
        
    email = input("Enter Email Address: ").strip()
    plate = input("Enter Car Plate (e.g., VDD1234): ").strip()
    
    # Check for Duplicate Car Plate
    try:
        veh_file = open("vehicles.txt", "r")
        vehicle_lines = veh_file.readlines()
        veh_file.close()
        
        for line in vehicle_lines:
            record = line.strip().split("|")
            if len(record) >= 2 and record[1].upper() == plate.upper():
                print(f"Error: The car plate '{plate.upper()}' is already registered in the system!")
                input("Press Enter to return...")
                return
    except FileNotFoundError:
        pass 

    make = input("Enter Car Make (e.g., Honda): ").strip()
    model = input("Enter Car Model (e.g., Civic): ").strip()
    
    if not name or not phone or not plate:
        print("Error: Name, Phone, and Car Plate cannot be empty!")
        input("Press Enter to return...")
        return

    # Save to files using | separator
    customer_record = f"{cust_id}|{name}|{phone}|{email}\n"
    vehicle_record = f"{cust_id}|{plate.upper()}|{make}|{model}\n"
    
    try:
        cust_file = open("customers.txt", "a")
        cust_file.write(customer_record)
        cust_file.close()
        
        veh_file = open("vehicles.txt", "a")
        veh_file.write(vehicle_record)
        veh_file.close()
        
        print(f"\nSuccess! Customer {name} and vehicle {plate.upper()} have been registered.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")
    
    input("Press Enter to continue...")

def make_booking():
    clear_screen()
    print("\n--- MAKE A SERVICE BOOKING ---")
    
    # Cross-check facility bays before allowing a booking
    try:
        bay_file = open("bays.txt", "r")
        bay_lines = bay_file.readlines()
        bay_file.close()
        
        all_maintenance = True
        for line in bay_lines:
            data = line.strip().split("|")
            if len(data) == 2 and data[1].strip() != "Maintenance":
                all_maintenance = False
                break
                
        if all_maintenance and len(bay_lines) > 0:
            print("SYSTEM ALERT: All washing bays are currently under maintenance!")
            print("Cannot accept new bookings at this time. Please contact the Facility Assistant.")
            input("Press Enter to return...")
            return
    except FileNotFoundError:
        pass # If file missing, just proceed

    car_plate = input("Enter Car Plate to book: ").strip()
    
    if not car_plate:
        print("Error: Car Plate cannot be empty.")
        input("Press Enter to continue...")
        return

    # Validate plate against vehicles.txt
    vehicle_found = False
    customer_id = ""
    
    try:
        veh_file = open("vehicles.txt", "r")
        vehicles = veh_file.readlines()
        veh_file.close()
        
        for line in vehicles:
            record = line.strip().split("|")
            if len(record) >= 2 and record[1].upper() == car_plate.upper():
                vehicle_found = True
                customer_id = record[0].strip()
                break
    except FileNotFoundError:
        print("Error: No vehicles registered yet. Please register first.")
        input("Press Enter to continue...")
        return

    if not vehicle_found:
        print(f"Error: Car Plate '{car_plate.upper()}' is not registered! Please register the vehicle first.")
        input("Press Enter to continue...")
        return

    # Auto-fetch Customer Name
    customer_name = "Unknown Customer"
    try:
        cust_file = open("customers.txt", "r")
        customers = cust_file.readlines()
        cust_file.close()
        
        for line in customers:
            record = line.strip().split("|")
            if len(record) >= 2 and record[0].strip() == customer_id:
                customer_name = record[1].strip()
                break
    except FileNotFoundError:
        pass 
        
    print(f"Found Registered Customer: {customer_name}")

    print("\nAvailable Packages:")
    print("1. Washing")
    print("2. Polishing")
    print("3. Vacuuming")
    print("4. Detailing")
    
    package_choice = input("Select Package (1-4): ").strip()
    packages = {"1": "Washing", "2": "Polishing", "3": "Vacuuming", "4": "Detailing"}
    service_package = packages.get(package_choice, "Unknown")
    
    if service_package == "Unknown":
        print("Error: Invalid package selection.")
        input("Press Enter to continue...")
        return
        
    # --- UPGRADED DATE VALIDATION LOGIC ---
    date = input("Enter Booking Date (DD/MM/YYYY): ").strip()
    
    if not date:
        print("Error: Date cannot be empty.")
        input("Press Enter to continue...")
        return

    try:
        booking_date = datetime.strptime(date, "%d/%m/%Y").date()
        today = datetime.today().date()
        
        if booking_date <= today:
            print("Error: Bookings must be made for a future date.")
            input("Press Enter to continue...")
            return
    except ValueError:
        print("Error: Invalid date. Please use the exact DD/MM/YYYY format.")
        input("Press Enter to continue...")
        return

    # Auto-generate Booking ID
    booking_id = "B001"
    try:
        file = open("bookings.txt", "r")
        lines = file.readlines()
        file.close()
        
        if len(lines) > 0:
            last_line = lines[-1]
            last_id = last_line.split("|")[0].strip()
            if last_id.startswith("B") and last_id[1:].isdigit():
                new_num = int(last_id[1:]) + 1
                booking_id = f"B{new_num:03d}" 
    except FileNotFoundError:
        pass

    status = "Pending"
    record = f"{booking_id}|{customer_name}|{car_plate.upper()}|{service_package}|{status}|{date}\n"
    
    try:
        file = open("bookings.txt", "a")
        file.write(record)
        file.close()
        print(f"\nSuccess! Booking created. Your Booking ID is {booking_id}.")
    except Exception as e:
        print(f"Error saving booking: {e}")
        
    input("Press Enter to continue...")

def manage_booking():
    clear_screen()
    print("\n--- CANCEL OR RESCHEDULE BOOKING ---")
    booking_id = input("Enter Booking ID to manage (e.g., B001): ").strip().upper()
    
    try:
        file = open("bookings.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: No bookings found in the system.")
        input("Press Enter to continue...")
        return
        
    updated_lines = []
    found = False
    
    for line in lines:
        record = line.strip().split("|")
        
        if record[0].upper() == booking_id:
            found = True
            print(f"\nFound Booking: {record[1]} - {record[3]} on {record[5]}")
            
            # Prevent altering completed bookings
            if len(record) >= 5 and record[4] == "Completed":
                print("Error: This booking is already marked as 'Completed' and cannot be modified.")
                updated_lines.append(line)
                continue

            print("1. Reschedule (Change Date)")
            print("2. Cancel (Delete Booking)")
            
            choice = input("Select option (1-2): ").strip()
            
            if choice == "1":
                new_date = input("Enter new date (DD/MM/YYYY): ").strip()
                # Run the same date validation here
                try:
                    reschedule_date = datetime.strptime(new_date, "%d/%m/%Y").date()
                    today = datetime.today().date()
                    if reschedule_date <= today:
                        print("Error: You can only reschedule to a future date.")
                        updated_lines.append(line)
                    else:
                        if len(record) >= 6:
                            record[5] = new_date
                        new_line = "|".join(record) + "\n"
                        updated_lines.append(new_line)
                        print("\nSuccess: Booking rescheduled!")
                except ValueError:
                    print("Error: Invalid date format. Booking not changed.")
                    updated_lines.append(line)
                    
            elif choice == "2":
                print("\nSuccess: Booking has been cancelled and removed.")
            else:
                print("Invalid choice. Keeping original record.")
                updated_lines.append(line)
        else:
            updated_lines.append(line)
            
    if not found:
        print("Error: Booking ID not found.")
    else:
        try:
            file = open("bookings.txt", "w")
            file.writelines(updated_lines)
            file.close()
        except Exception as e:
            print(f"Error updating file: {e}")
            
    input("Press Enter to continue...")

def view_bookings():
    clear_screen()
    print("\n--- BOOKING SCHEDULE & HISTORY ---")
    try:
        file = open("bookings.txt", "r")
        lines = file.readlines()
        file.close()
        
        if len(lines) == 0:
            print("No bookings found in the system.")
        else:
            print(f"\n{'ID':<6} | {'Customer':<15} | {'Plate':<10} | {'Package':<12} | {'Status':<10} | {'Date':<12}")
            print("-" * 78)
            
            for line in lines:
                record = line.strip().split("|")
                if len(record) >= 6:
                    print(f"{record[0]:<6} | {record[1]:<15} | {record[2]:<10} | {record[3]:<12} | {record[4]:<10} | {record[5]:<12}")
                
    except FileNotFoundError:
        print("Error: The booking data file does not exist yet.")
        
    input("\nPress Enter to return to menu...")

# Only runs if testing this specific file
if __name__ == "__main__":
    booking_officer_menu()
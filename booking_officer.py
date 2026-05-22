def booking_officer_menu():
    is_running = True
    while is_running:
        print("\n==========================================")
        print("       SHINEPRO BOOKING OFFICER MENU      ")
        print("==========================================")
        print(" 1. Register New Customer & Vehicle")
        print(" 2. Make a Service Booking")
        print(" 3. Cancel / Reschedule Booking")
        print(" 4. View Booking Schedule & History")
        print(" 5. Return to Main Menu")
        print("==========================================")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            register_customer()
        elif choice == "2":
            make_booking()
        elif choice == "3":
            manage_booking()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            print("Exiting Booking Officer Menu...")
            is_running = False
        else:
            print("Invalid input! Please enter a number between 1 and 5.")


def register_customer():
    print("\n--- NEW CUSTOMER REGISTRATION ---")
    cust_id = input("Enter new Customer ID (e.g., C001): ").strip()
    name = input("Enter Customer Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    
    plate = input("Enter Car Plate (e.g., VDD1234): ").strip()
    make = input("Enter Car Make (e.g., Honda): ").strip()
    model = input("Enter Car Model (e.g., Civic): ").strip()
    
    if not cust_id or not name or not phone or not plate:
        print("Error: Customer ID, Name, Phone, and Car Plate cannot be empty!")
        return

    customer_record = f"{cust_id}|{name}|{phone}|{email}\n"
    vehicle_record = f"{cust_id}|{plate}|{make}|{model}\n"
    
    try:
        cust_file = open("customers.txt", "a")
        cust_file.write(customer_record)
        cust_file.close()
        
        veh_file = open("vehicles.txt", "a")
        veh_file.write(vehicle_record)
        veh_file.close()
        
        print(f"\nSuccess! Customer {name} and vehicle {plate} have been registered.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")


def make_booking():
    print("\n--- MAKE A SERVICE BOOKING ---")
    car_plate = input("Enter Car Plate to book: ").strip()
    
    if not car_plate:
        print("Error: Car Plate cannot be empty.")
        return

    # 1. VALIDATION: Check if the car plate exists in vehicles.txt
    vehicle_found = False
    customer_id = ""
    
    try:
        veh_file = open("vehicles.txt", "r")
        vehicles = veh_file.readlines()
        veh_file.close()
        
        for line in vehicles:
            record = line.strip().split("|")
            # record format: CustID|Plate|Make|Model
            if len(record) >= 2 and record[1] == car_plate:
                vehicle_found = True
                customer_id = record[0] # Grab the ID to find the name next
                break
    except FileNotFoundError:
        print("Error: No vehicles registered yet. Please use Option 1 first.")
        return

    if not vehicle_found:
        print(f"Error: Car Plate '{car_plate}' is not registered! Please register the vehicle first.")
        return

    # 2. DATA CONSISTENCY: Auto-fetch the Customer Name using the Customer ID
    customer_name = "Unknown Customer"
    try:
        cust_file = open("customers.txt", "r")
        customers = cust_file.readlines()
        cust_file.close()
        
        for line in customers:
            record = line.strip().split("|")
            # record format: CustID|Name|Phone|Email
            if len(record) >= 2 and record[0] == customer_id:
                customer_name = record[1]
                break
    except FileNotFoundError:
        pass # If file is missing, we just use "Unknown Customer"
        
    print(f"Found Registered Customer: {customer_name}")

    # 3. Proceed with the booking since the car is valid
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
        return
        
    date = input("Enter Booking Date (DD/MM/YYYY): ").strip()
    if not date:
        print("Error: Date cannot be empty.")
        return

    # 4. Auto-generate Booking ID
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
    record = f"{booking_id}|{customer_name}|{car_plate}|{service_package}|{status}|{date}\n"
    
    try:
        file = open("bookings.txt", "a")
        file.write(record)
        file.close()
        print(f"\nSuccess! Booking created. Your Booking ID is {booking_id}.")
    except Exception as e:
        print(f"Error saving booking: {e}")


def manage_booking():
    print("\n--- CANCEL OR RESCHEDULE BOOKING ---")
    booking_id = input("Enter Booking ID to manage (e.g., B001): ").strip()
    
    try:
        file = open("bookings.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: No bookings found in the system.")
        return
        
    updated_lines = []
    found = False
    
    for line in lines:
        record = line.strip().split("|")
        
        if record[0] == booking_id:
            found = True
            print(f"\nFound Booking: {record[1]} - {record[3]} on {record[5]}")
            print("1. Reschedule (Change Date)")
            print("2. Cancel (Delete Booking)")
            
            choice = input("Select option (1-2): ").strip()
            
            if choice == "1":
                new_date = input("Enter new date (DD/MM/YYYY): ").strip()
                if len(record) >= 6:
                    record[5] = new_date     
                new_line = "|".join(record) + "\n"
                updated_lines.append(new_line)
                print("\nSuccess: Booking rescheduled!")
            elif choice == "2":
                print("\nSuccess: Booking has been cancelled and removed.")
            else:
                print("Invalid choice. Keeping original record.")
                updated_lines.append(line)
        else:
            updated_lines.append(line)
            
    if not found:
        print("Error: Booking ID not found.")
        return
        
    try:
        file = open("bookings.txt", "w")
        file.writelines(updated_lines)
        file.close()
    except Exception as e:
        print(f"Error updating file: {e}")


def view_bookings():
    print("\n--- BOOKING SCHEDULE & HISTORY ---")
    try:
        file = open("bookings.txt", "r")
        lines = file.readlines()
        file.close()
        
        if len(lines) == 0:
            print("No bookings found in the system.")
            return
            
        print(f"\n{'ID':<6} | {'Customer':<15} | {'Plate':<10} | {'Package':<12} | {'Status':<10} | {'Date':<12}")
        print("-" * 78)
        
        for line in lines:
            record = line.strip().split("|")
            if len(record) >= 6:
                print(f"{record[0]:<6} | {record[1]:<15} | {record[2]:<10} | {record[3]:<12} | {record[4]:<10} | {record[5]:<12}")
                
    except FileNotFoundError:
        print("Error: The booking data file does not exist yet.")

if __name__ == "__main__":
    booking_officer_menu()
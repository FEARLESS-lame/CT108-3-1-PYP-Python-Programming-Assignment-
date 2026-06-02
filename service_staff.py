# SHINEPRO CAR CARE SERVICE STAFF MODULE
# This module provides functionalities for service staff to manage vehicle service statuses 
# this module also generate daily summary reports based on booking data stored in 'bookings.txt'.
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def service_staff_menu():
    clear_screen()
    is_running = True
    while is_running == True:
        print("\n==========================================")
        print("       SHINEPRO SERVICE STAFF MENU        ")
        print("==========================================")
        print(" 1. View & Update Vehicle Service Status")
        print(" 2. Generate Daily Service Summary Report")
        print(" 3. Return to Main Menu")
        print("==========================================")
        
        user_choice = input("Select an option (1-3): ")
        
        if user_choice == "1":
            update_vehicle_status()
        elif user_choice == "2":
            generate_service_report()
        elif user_choice == "3":
            print("Exiting Service Staff Menu... Returning to Main Menu.")
            is_running = False  # Terminates the loop
        else:
            print("Invalid input! Please enter 1, 2, or 3.")

def update_vehicle_status():
    clear_screen()
    data_file = "bookings.txt"
    
    # --- STEP 1: READ CURRENT FILE DATA (With Error Handling) ---
    try:
        file_reader = open(data_file, "r")
        all_bookings = file_reader.readlines()
        file_reader.close()
    except FileNotFoundError:
        print("Error: The booking data file was not found!")
        return

    # Check if the file is empty
    if len(all_bookings) == 0:
        print("No booking records currently exist in the system.")
        return

    print("\n--- Currently Active Vehicles in Workshop ---")
    active_vehicles_exist = False
    
    for line in all_bookings:
        # Delimiter used is '|'. Format: ID|Name|Plate|Package|Status|Date
        record = line.strip().split("|")
        booking_id = record[0]
        car_plate = record[2]
        current_status = record[4]
        
        # Only show jobs that are not yet finalized
        if current_status != "Completed":
            print("Booking ID: " + booking_id + " | Plate: " + car_plate + " | Status: " + current_status)
            active_vehicles_exist = True
            
    if active_vehicles_exist == False:
        print("All vehicles have been fully serviced and completed!")
        return

    target_id = input("\nEnter the Booking ID to update: ")
    
    updated_lines_list = []
    record_found = False

    for line in all_bookings:
        record = line.strip().split("|")
        
        # Check if this line matches the requested Booking ID
        if record[0] == target_id:
            record_found = True
            print("\nVehicle Found: " + record[2] + " (" + record[3] + ")")
            print("Select New Operational Status:")
            print(" 1. Washing")
            print(" 2. Polishing")
            print(" 3. Vacuuming")
            print(" 4. Detailing")
            print(" 5. Completed")
            
            status_input = input("Enter option number (1-5): ")
            
            # Simple conversion from menu numbers to strings
            if status_input == "1":
                assigned_status = "Washing"
            elif status_input == "2":
                assigned_status = "Polishing"
            elif status_input == "3":
                assigned_status = "Vacuuming"
            elif status_input == "4":
                assigned_status = "Detailing"
            elif status_input == "5":
                assigned_status = "Completed"
            else:
                print("Invalid choice. Status change aborted.")
                return
            
            # Reconstruct the text line manually with the updated status string
            modified_line = record[0] + "|" + record[1] + "|" + record[2] + "|" + record[3] + "|" + assigned_status + "|" + record[5] + "\n"
            updated_lines_list.append(modified_line)
            print("Success: Status successfully updated to '" + assigned_status + "'.")
        else:
            # If it's not the chosen vehicle, keep the original line intact
            updated_lines_list.append(line)

    if record_found == False:
        print("Error: Booking ID not found in the database.")
        return

    file_writer = open(data_file, "w")
    file_writer.writelines(updated_lines_list)
    file_writer.close()


def generate_service_report():
    clear_screen()
    data_file = "bookings.txt"
    
    try:
        file_reader = open(data_file, "r")
        all_bookings = file_reader.readlines()
        file_reader.close()
    except FileNotFoundError:
        print("Error: Cannot generate report because data file does not exist.")
        return

    # Initialize counter variables
    total_records = 0
    completed_jobs = 0
    washing_jobs = 0
    polishing_jobs = 0
    vacuuming_jobs = 0
    detailing_jobs = 0

    # Process files row by row to count metrics
    for line in all_bookings:
        record = line.strip().split("|")
        if len(record) >= 5:
            total_records = total_records + 1
            status_value = record[4]
            
            if status_value == "Completed":
                completed_jobs = completed_jobs + 1
            elif status_value == "Washing":
                washing_jobs = washing_jobs + 1
            elif status_value == "Polishing":
                polishing_jobs = polishing_jobs + 1
            elif status_value == "Vacuuming":
                vacuuming_jobs = vacuuming_jobs + 1
            elif status_value == "Detailing":
                detailing_jobs = detailing_jobs + 1

                
    print("\n==========================================")
    print("       DAILY SERVICE SUMMARY REPORT       ")
    print("==========================================")
    print(f"Total Bookings Processed : {total_records}")
    print(f"Total Jobs Completed     : {completed_jobs}")
    print("------------------------------------------")
    print("Breakdown by Service Type:")
    print(f" - Washing   : {washing_jobs}")
    print(f" - Polishing : {polishing_jobs}")
    print(f" - Vacuuming : {vacuuming_jobs}")
    print(f" - Detailing : {detailing_jobs}")
    print("==========================================\n")
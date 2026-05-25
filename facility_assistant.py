# ==========================================
# ROLE: FACILITY ASSISTANT
# SYSTEM: ShinePro Auto Care
# ==========================================

def display_menu():
    """Displays the main menu for the Facility Assistant."""
    print("\n" + "="*40)
    print("   SHINEPRO: FACILITY ASSISTANT MENU")
    print("="*40)
    print("1. Prepare Washing Bays & Equipment")
    print("2. Monitor Supply Usage & Condition")
    print("3. Report Issues to Administrator")
    print("4. Exit")
    print("="*40)

def prepare_bays():
    """Allows the assistant to view and update washing bay statuses."""
    print("\n--- Prepare Washing Bays ---")
    filename = "bays.txt"
    
    try:
        # Read current bays
        with open(filename, "r") as file:
            lines = file.readlines()
            
        if not lines:
            print("No bay data found.")
            return

        print(f"{'Bay ID':<10} | {'Current Status'}")
        print("-" * 30)
        bays = []
        for line in lines:
            data = line.strip().split(",")
            if len(data) == 2:
                bays.append(data)
                print(f"{data[0]:<10} | {data[1]}")

        # Update a bay
        update_choice = input("\nDo you want to update a bay status? (Y/N): ").strip().upper()
        if update_choice == 'Y':
            bay_id = input("Enter Bay ID to update (e.g., B01): ").strip().upper()
            found = False
            
            for i in range(len(bays)):
                if bays[i][0] == bay_id:
                    found = True
                    print("Select new status:")
                    print("1. Available")
                    print("2. Occupied")
                    print("3. Maintenance")
                    
                    status_choice = input("Enter choice (1-3): ").strip()
                    if status_choice == '1':
                        bays[i][1] = "Available"
                    elif status_choice == '2':
                        bays[i][1] = "Occupied"
                    elif status_choice == '3':
                        bays[i][1] = "Maintenance"
                    else:
                        print("Error: Invalid status choice.")
                        return
                    
                    print(f"Success: {bay_id} updated to {bays[i][1]}.")
                    break
            
            if not found:
                print("Error: Bay ID not found.")
            else:
                # Write back to file
                with open(filename, "w") as file:
                    for b in bays:
                        file.write(f"{b[0]},{b[1]}\n")
                        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please ensure it exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def monitor_supplies():
    """Allows the assistant to view and update supply quantities."""
    print("\n--- Monitor Supply Usage ---")
    filename = "supplies.txt"
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
        if not lines:
            print("No supplies data found.")
            return

        print(f"{'Item Name':<20} | {'Quantity':<10} | {'Condition/Status'}")
        print("-" * 55)
        supplies = []
        for line in lines:
            data = line.strip().split(",")
            if len(data) == 3:
                supplies.append(data)
                print(f"{data[0]:<20} | {data[1]:<10} | {data[2]}")

        update_choice = input("\nDo you want to update a supply quantity? (Y/N): ").strip().upper()
        if update_choice == 'Y':
            item_name = input("Enter Item Name to update (Case Sensitive): ").strip()
            found = False
            
            for i in range(len(supplies)):
                if supplies[i][0] == item_name:
                    found = True
                    try:
                        new_qty = int(input(f"Enter new quantity for {item_name}: ").strip())
                        if new_qty < 0:
                            print("Error: Quantity cannot be negative.")
                            return
                        
                        supplies[i][1] = str(new_qty)
                        
                        # Auto-update status based on quantity
                        if new_qty == 0:
                            supplies[i][2] = "Out of Stock"
                        elif new_qty < 5:
                            supplies[i][2] = "Low"
                        else:
                            supplies[i][2] = "Good"
                            
                        print(f"Success: {item_name} updated to {new_qty} ({supplies[i][2]}).")
                    except ValueError:
                        print("Error: Please enter a valid whole number for quantity.")
                        return
                    break
            
            if not found:
                print("Error: Item not found.")
            else:
                # Write back to file
                with open(filename, "w") as file:
                    for s in supplies:
                        file.write(f"{s[0]},{s[1]},{s[2]}\n")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def report_issues():
    """Allows the assistant to log issues for the administrator."""
    print("\n--- Report Issues ---")
    filename = "reports.txt"
    
    print("Types of issues you can report:")
    print("1. Delays")
    print("2. Equipment Issues")
    print("3. Fully Occupied Bays")
    print("4. Cancel")
    
    choice = input("Select an issue type (1-4): ").strip()
    
    issue_type = ""
    if choice == '1':
        issue_type = "Delay"
    elif choice == '2':
        issue_type = "Equipment Issue"
    elif choice == '3':
        issue_type = "Fully Occupied"
    elif choice == '4':
        print("Reporting cancelled.")
        return
    else:
        print("Error: Invalid choice.")
        return

    description = input("Enter a brief description of the issue: ").strip()
    date = input("Enter today's date (DD-MM-YYYY): ").strip()
    
    if not description or not date:
        print("Error: Description and date cannot be empty.")
        return
        
    try:
        # Append mode ("a") is used so we don't overwrite existing reports
        with open(filename, "a") as file:
            # Format: Date, IssueType, Description, Status
            file.write(f"{date},{issue_type},{description},Unresolved\n")
        print("\nSuccess: Issue successfully reported to the Administrator.")
    except Exception as e:
        print(f"Error saving report: {e}")

def facility_assistant_main():
    """Main loop for the Facility Assistant role."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            prepare_bays()
        elif choice == '2':
            monitor_supplies()
        elif choice == '3':
            report_issues()
        elif choice == '4':
            print("Logging out of Facility Assistant account...")
            break
        else:
            print("Error: Invalid input. Please enter a number between 1 and 4.")

# Automatically start the program if this script is run directly
if __name__ == "__main__":
    facility_assistant_main()
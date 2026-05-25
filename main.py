# main.py - SHINEPRO AUTO CARE CENTRAL SYSTEM

import booking_officer
import service_staff
import system_administrator
import facility_assistant
import Customer

def main_system_menu():
    while True:
        print("\n==========================================")
        print("    WELCOME TO SHINEPRO AUTO CARE SYSTEM  ")
        print("==========================================")
        print("Please select your role to login:")
        print(" 1. System Administrator")
        print(" 2. Booking Officer")
        print(" 3. Service Staff")
        print(" 4. Customer")
        print(" 5. Facility Assistant")
        print(" 6. Exit System")
        print("==========================================")
        
        role_choice = input("Enter your role (1-6): ").strip()
        
        # 2. Route the user to the correct file's menu function
        if role_choice == "1":
            system_administrator.system_admin_menu()
        elif role_choice == "2":
            booking_officer.booking_officer_menu() # This runs your part!
        elif role_choice == "3":
            service_staff.service_staff_menu() # This runs your friend's part!
        elif role_choice == "4":
            Customer.customer_menu()
        elif role_choice == "5":
            facility_assistant.facility_assistant_menu()
        elif role_choice == "6":
            print("Shutting down ShinePro Auto Care System. Goodbye!")
            break
        else:
            print("Invalid input. Please select a valid role.")

# Start the entire program
if __name__ == "__main__":
    main_system_menu()
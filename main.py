# ==========================================
# CENTRAL ROUTER
# SYSTEM: ShinePro Auto Care
# ==========================================
import os
import booking_officer
import service_staff
import system_administrator
import facility_assistant
import customer  # MUST BE LOWERCASE IN YOUR FOLDER TOO

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_system_menu():
    while True:
        clear_screen()
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
        
        if role_choice == "1":
            system_administrator.system_admin_menu()
        elif role_choice == "2":
            booking_officer.booking_officer_menu() 
        elif role_choice == "3":
            service_staff.service_staff_menu() 
        elif role_choice == "4":
            customer.customer_menu()
        elif role_choice == "5":
            facility_assistant.facility_assistant_menu()
        elif role_choice == "6":
            print("Shutting down ShinePro Auto Care System. Goodbye!")
            break
        else:
            print("Invalid input. Please select a valid role.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_system_menu()
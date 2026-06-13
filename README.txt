=========================================================
SHINEPRO AUTO CARE - SERVICE BOOKING MANAGEMENT SYSTEM
=========================================================

1. LIST OF ALL FILES INCLUDED & BRIEF DESCRIPTIONS
---------------------------------------------------------
Python Scripts:
* main.py                  : Central router and main login landing page for the system.
* system_administrator.py  : Module for managing service packages, time slots, and financial reports.
* booking_officer.py       : Module for handling customer registrations and detailing appointments.
* service_staff.py         : Module for logging daily work records and tracking live service progress.
* customer.py              : Module for customer interactions, booking, and service status checks.
* facility_assistant.py    : Module for tracking washing bays, inventory levels, and facility issues.

Database Files (Text Files):
* bays.txt                 : Flat-file database tracking the status of physical washing bays.
* supplies.txt             : Flat-file database tracking shop inventory and supply conditions.
* reports.txt              : Flat-file log where facility exceptions and issues are appended.
* customers.txt            : Flat-file database storing registered customer profiles.
* vehicles.txt             : Flat-file database storing customer vehicle details.
* booking.txt              : Flat-file database containing all active and past service appointments.
* payment.txt              : Flat-file database logging transaction and payment history.


2. INSTRUCTIONS ON HOW TO RUN THE PROGRAM
---------------------------------------------------------
1. Extract the entire contents of the ZIP file into a single folder on your computer.
2. Open your system's Terminal (Mac/Linux) or Command Prompt (Windows).
3. Use the `cd` command to navigate directly into the extracted folder.
4. Run the main application controller by typing the following command and pressing Enter:
   
   python main.py
   
   (Note: Depending on your system configuration, Mac users may need to type `python3 main.py`).
5. Once the system launches, use the numeric keys to navigate the main menu and select a role.


3. PYTHON VERSION USED
---------------------------------------------------------
Python 3.10 (Compatible with Python 3.x environments).


4. REQUIRED LIBRARIES
---------------------------------------------------------
None. 
It uses only native Python built-in modules (like `os` and `datetime`).


5. ADDITIONAL INSTRUCTIONS
---------------------------------------------------------
* File Placement Rule: For the program to execute without FileNotFoundError exceptions, ALL Python scripts (.py) and database files (.txt) MUST remain together in the exact same root directory. 
* Pre-populated Data: The text files contain pre-populated dummy data necessary for demonstrating the "View" and "Update" functionalities during the system execution. Do not delete the text files before running the program.
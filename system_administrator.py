# SHINEPRO CAR CARE - SYSTEM ADMINISTRATOR MODULE

SERVICES_FILE = "services.txt"
CUSTOMERS_FILE = "customers.txt"
VEHICLES_FILE = "vehicles.txt"
BOOKINGS_FILE = "bookings.txt"
PAYMENTS_FILE = "payments.txt"


def system_admin_menu():

    while True:
        print("\n================================")
        print("   SHINEPRO SYSTEM ADMINISTRATOR")
        print("================================")
        print("1. Add Service Package")
        print("2. Update Service Package")
        print("3. Remove Service Package")
        print("4. View All Data")
        print("5. Generate Report")
        print("0. Exit")

        choice = input("Enter choice: ")

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

        elif choice == "0":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")


def add_service_package():

    service_id = input("Enter service ID: ")
    service_name = input("Enter service name: ")
    price = input("Enter price: ")
    slot = input("Enter slot: ")

    file = open(SERVICES_FILE, "a")

    file.write(
        service_id + "," +
        service_name + "," +
        price + "," +
        slot + "\n"
    )

    file.close()

    print("Service package added successfully!")


def update_service_package():

    service_id = input("Enter Service ID to update: ")

    try:
        file = open(SERVICES_FILE, "r")
        services = file.readlines()
        file.close()

        found = False

        file = open(SERVICES_FILE, "w")

        for service in services:

            data = service.strip().split(",")

            if data[0] == service_id:

                found = True

                print("Service found!")

                new_name = input("Enter new service name: ")
                new_price = input("Enter new price: ")
                new_slot = input("Enter new slot: ")

                file.write(
                    service_id + "," +
                    new_name + "," +
                    new_price + "," +
                    new_slot + "\n"
                )

                print("Service updated successfully!")

            else:
                file.write(service)

        file.close()

        if found == False:
            print("Service ID not found.")

    except FileNotFoundError:
        print("services.txt not found!")


def remove_service_package():

    service_id = input("Enter Service ID to remove: ")

    try:
        file = open(SERVICES_FILE, "r")
        services = file.readlines()
        file.close()

        found = False

        file = open(SERVICES_FILE, "w")

        for service in services:

            data = service.strip().split(",")

            if data[0] == service_id:
                found = True
                print("Service removed successfully!")

            else:
                file.write(service)

        file.close()

        if found == False:
            print("Service ID not found.")

    except FileNotFoundError:
        print("services.txt not found!")


def view_all_data():

    files = [
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

            if data == "":
                print("No data found")
            else:
                print(data)

            file.close()

        except FileNotFoundError:
            print("File not found")


def generate_report():

    total_bookings = 0
    total_revenue = 0

    try:
        file = open(BOOKINGS_FILE, "r")

        bookings = file.readlines()

        total_bookings = len(bookings)

        file.close()

    except FileNotFoundError:
        print("Bookings file not found")

    try:
        file = open(PAYMENTS_FILE, "r")

        for line in file:

            data = line.strip().split(",")

            if len(data) > 1:
                total_revenue += float(data[1])

        file.close()

    except FileNotFoundError:
        print("Payments file not found")

    print("\n===== REPORT =====")
    print("Total bookings:", total_bookings)
    print("Total revenue: RM", total_revenue)


# RUN PROGRAM
system_admin_menu()

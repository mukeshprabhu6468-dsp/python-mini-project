# Bus Ticket Booking System with Login

# Predefined users (username: password)
users = {"admin": "1234",
         "user1": "pass1"}

buses = [
         {"bus_no": 101, "from": "Chennai", "to": "Bangalore", "seats": 5},
         {"bus_no": 102, "from": "Chennai", "to": "Hyderabad", "seats": 3},
         {"bus_no": 103, "from": "Bangalore", "to": "Mumbai", "seats": 4}]

#  Login Function
def login():
    print("\n--- Login System ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Username or Password!\n")
        return False

# Show buses
def show_buses():
    print("\nAvailable Buses:")
    for bus in buses:
        print(f"Bus No: {bus['bus_no']} | {bus['from']} -> {bus['to']} | Seats: {bus['seats']}")

# Book ticket
def book_ticket():
    bus_no = int(input("Enter Bus Number: "))
    
    for bus in buses:
        if bus["bus_no"] == bus_no:
            if bus["seats"] > 0:
                name = input("Enter your name: ")
                bus["seats"] -= 1
                
                print("\n Ticket Booked Successfully!")
                print("Name:", name)
                print("Bus No:", bus["bus_no"])
                print("Route:", bus["from"], "->", bus["to"])
                print("Seat Number:", bus["seats"] + 1)
                return
            else:
                print("No seats available!")
                return
    
    print("Invalid Bus Number!")

# Main program
def main():
    # Login loop
    while True:
        if login():
            break

    # After login
    while True:
        print("\n--- Bus Booking System ---")
        print("1. Show Buses")
        print("2. Book Ticket")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            show_buses()
        elif choice == "2":
            show_buses()
            book_ticket()
        elif choice == "3":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice!")

main()



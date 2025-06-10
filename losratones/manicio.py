MENU_ITEMS = {
    "Burger": 120.00,
    "Fries": 50.00,
    "Sushi": 200.00,
    "Pizza": 125.00,
    "Ice Cream": 25.00
}

LINE_SEPARATOR = "-" * 30
MIN_QUANTITY = 1
EXIT_OPTION = "0"

class Manicio:
    def __init__(self):
        self.customer_name = ""
        self.cart = {}
        self.menu_items = MENU_ITEMS

    def set_customer_name(self):
        while True:
            name = input("Enter customer name: ").strip()
            if not name:
                print("Customer name cannot be empty. Please try again.")
                continue
            self.customer_name = name
            print(f"Welcome, {self.customer_name}!")
            break

    def view_menu(self):
        print("\nAvailable Menu:")
        for item, price in self.menu_items.items():
            print(f"{item} - PHP {price}")

    def add_to_cart(self):
        self.view_menu()

        while True:
            item = input("\nEnter item to add (or 0 to stop): ").title()

            if item == EXIT_OPTION:
                print("Finished adding items to cart.")
                break

            if item not in self.menu_items:
                print("Item not in menu. Please try again.")
                continue

            try:
                quantity = int(input(f"Enter quantity for {item}: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue
            
            if quantity <= MIN_QUANTITY:
                    print("Quantity must be greater than zero.")
                    continue
            
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity

            print(f"Added {quantity} x {item} to cart.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return

        print("\nYour Cart:")
        print(LINE_SEPARATOR)

        total = 0

        for item, quantity in self.cart.items():
            price = self.menu_items[item]
            subtotal = price * quantity
            print(f"{item} x {quantity} @ PHP {price} = PHP {subtotal}")
            total += subtotal
            
        print(LINE_SEPARATOR)
        print(f"Total: PHP {total}")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Cannot proceed to checkout.")
            return
            
        if not self.customer_name:
            print("Please set customer name before checkout.")
            self.set_customer_name()

        print("\n===== RECEIPT =====")
        print(f"Customer: {self.customer_name}")
        print(LINE_SEPARATOR)

        total = 0

        for item, quantity in self.cart.items():
            price = self.menu_items[item]
            subtotal = price * quantity
            print(f"{item} x {quantity} @ PHP {price} = PHP {subtotal}")       
            total += subtotal

        print(LINE_SEPARATOR)
        print(f"TOTAL: PHP {total}")
        print(f"Thank you for ordering, {self.customer_name}!")
        print(LINE_SEPARATOR)

        self.cart.clear()

    def display_menu(self):
        """Display the order management options."""
        print("\n[Order Management]")
        print("1. Set Customer Name")
        print("2. View Menu")
        print("3. Add to Cart")
        print("4. View Cart") 
        print("5. Checkout")
        print("0. Back to Main Menu")

    def handle_menu_choice(self, choice):
        """Process the user's menu selection."""
        match choice:
            case "1":
                self.set_customer_name()
            case "2":
                self.view_menu()
            case "3":
                self.add_to_cart()
            case "4":
                self.view_cart()
            case "5":
                self.checkout()
            case _:
                print("Invalid option. Try again.")

    def menu(self):
        """Main menu loop."""
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            
            if choice == EXIT_OPTION:
                break
                
            self.handle_menu_choice(choice)


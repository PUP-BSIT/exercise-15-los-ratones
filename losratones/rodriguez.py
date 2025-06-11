MOVIE_LISTINGS = {
    "Inception": 350.00,
    "Avengers: Endgame": 400.00,
    "Parasite": 300.00,
    "The Godfather": 375.00,
    "Jurassic Park": 325.00
}

LINE_SEPARATOR = "-" * 40
EXIT_OPTION = "0"

class MovieTicketManager:
    """A class to manage movie ticket bookings and reservations."""
    
    def __init__(self):
        """Initialize the MovieTicketManager with default values."""
        self.customer_name = ""
        self.bookings = {}
        self.available_movies = MOVIE_LISTINGS
    
    def get_customer_name(self):
        """Get the customer's name."""
        return self.customer_name
    
    def booking_count(self):
        """Get the total number of movies booked."""
        return len(self.bookings)
    
    def total_tickets(self):
        """Get the total number of tickets across all bookings."""
        return sum(self.bookings.values())
    
    def set_customer_name(self):
        """Set or update the customer's name."""
        while True:
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")
                continue
            self.customer_name = name
            print(f"Welcome to MoviePlex, {self.customer_name}!")
            break
    
    def view_movies(self):
        """Display the list of available movies and their prices."""
        print("\nCurrently Showing Movies:")
        print(LINE_SEPARATOR)
        for movie, price in self.available_movies.items():
            print(f"{movie} - PHP {price:.2f}")
        print(LINE_SEPARATOR)
    
    def book_tickets(self):
        """Book tickets for one or more movies."""
        self.view_movies()

        while True:
            prompt = (f"\nEnter movie name to book "
                     f"(or {EXIT_OPTION} to finish): ")
            movie = input(prompt).strip()
            
            if movie == EXIT_OPTION:
                print("Finished booking tickets.")
                break
                
            if not self.is_valid_movie(movie):
                continue
                
            tickets = self.get_ticket_count(movie)
            if tickets <= 0:
                continue
                
            self.add_booking(movie, tickets)
    
    def is_valid_movie(self, movie):
        """Check if the movie exists in available movies."""
        exact_match = movie in self.available_movies
        
        if exact_match:
            return True
            
        for available_movie in self.available_movies:
            if movie.lower() in available_movie.lower():
                print(f"Found '{available_movie}' matching your search.")
                return True
                
        print("Movie not available. Please check the movie name.")
        return False
    
    def get_ticket_count(self, movie):
        """Get the number of tickets from user input."""
        try:
            tickets = int(input(f"How many tickets for '{movie}'? "))
            if tickets <= 0:
                print("Number of tickets must be greater than zero.")
                return 0
            return tickets
        except ValueError:
            print("Invalid input. Please enter a number.")
            return 0
    
    def add_booking(self, movie, tickets):
        """Add a booking for the specified movie and ticket count."""
        if movie in self.bookings:
            self.bookings[movie] += tickets
        else:
            self.bookings[movie] = tickets
            
        price = self.available_movies[movie]
        total = price * tickets
        print(f"Added {tickets} ticket(s) for '{movie}' - PHP {total:.2f}")
    
    def view_bookings(self):
        """View all current bookings and their total cost."""
        if not self.bookings:
            print("You haven't booked any tickets yet.")
            return
            
        print("\nYour Current Bookings:")
        print(LINE_SEPARATOR)
        self.print_booking_details()
    
    def generate_confirmation(self):
        """Generate a booking confirmation and clear the bookings."""
        if not self.bookings:
            print("You have no bookings to confirm.")
            return
            
        if not self.customer_name:
            self.set_customer_name()
            if not self.customer_name:
                return
    
        self.print_confirmation_header()
        self.print_booking_details()
        self.print_confirmation_footer()
        
        self.bookings.clear()
    
    def print_confirmation_header(self):
        """Print the confirmation header with customer information."""
        print("\n===== BOOKING CONFIRMATION =====")
        print(f"Customer: {self.customer_name}")
        print(f"Booking ID: JP{hash(self.customer_name) % 10000:04d}")
        print(LINE_SEPARATOR)
    
    def print_booking_details(self):
        """Print the details of each booking and calculate the total cost."""
        total_cost = 0
        for movie, tickets in self.bookings.items():
            price = self.available_movies[movie]
            subtotal = price * tickets
            print(f"{movie}: {tickets} ticket(s) @ PHP {price:.2f} = "
                  f"PHP {subtotal:.2f}")
            total_cost += subtotal
            
        print(LINE_SEPARATOR)
        print(f"TOTAL AMOUNT: PHP {total_cost:.2f}")
    
    def print_confirmation_footer(self):
        """Print the confirmation footer."""
        print("\nPlease present this confirmation at the counter.")
        print(f"Thank you for choosing MoviePlex, {self.customer_name}!")
        print("=============================")
    
    def menu(self):
        """Display the MovieTicketManager menu and handle user interactions."""
        while True:
            self.display_menu_header()
            choice = input("Select an option: ")
            
            if choice == EXIT_OPTION:
                break
                
            self.handle_menu_option(choice)
    
    def display_menu_header(self):
        """Display the menu header with customer information."""
        print("\n[MoviePlex Ticket Booking System]")
        if self.customer_name:
            print(f"Customer: {self.customer_name}")
        if self.bookings:
            print(f"Current Bookings: {self.booking_count()} movies, "
                  f"{self.total_tickets()} tickets")
            
        print("1. Set Customer Name")
        print("2. View Available Movies")
        print("3. Book Movie Tickets")
        print("4. View My Bookings")
        print("5. Generate Booking Confirmation")
        print(f"{EXIT_OPTION}. Back to Main Menu")
    
    def handle_menu_option(self, choice):
        """Handle the selected menu option."""
        match choice:
            case "1":
                self.set_customer_name()
            case "2":
                self.view_movies()
            case "3":
                self.book_tickets()
            case "4":
                self.view_bookings()
            case "5":
                self.generate_confirmation()
            case _:
                print("Invalid option. Please try again.")
MOVIE_LISTINGS = {
    "Inception": 350.00,
    "Avengers: Endgame": 400.00,
    "Parasite": 300.00,
    "The Godfather": 375.00,
    "Jurassic Park": 325.00
}

LINE_SEPARATOR = "-" * 40

class MovieTicketManager:
    """A class to manage movie ticket bookings and reservations."""
    
    def __init__(self):
        """Initialize the MovieTicketManager with default values."""
        self._customer_name = ""
        self._bookings = {}
        self._available_movies = MOVIE_LISTINGS
    
    @property
    def customer_name(self):
        """Get the customer's name."""
        return self._customer_name
    
    @property
    def booking_count(self):
        """Get the total number of movies booked."""
        return len(self._bookings)
    
    @property
    def total_tickets(self):
        """Get the total number of tickets across all bookings."""
        return sum(self._bookings.values())
    
    def set_customer_name(self):
        """Set or update the customer's name."""
        while True:
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")
                continue
            self._customer_name = name
            print(f"Welcome to MoviePlex, {self._customer_name}!")
            break
    
    def view_movies(self):
        """Display the list of available movies and their prices."""
        print("\nCurrently Showing Movies:")
        print(LINE_SEPARATOR)
        for movie, price in self._available_movies.items():
            print(f"{movie} - PHP {price:.2f}")
        print(LINE_SEPARATOR)
    
    def book_tickets(self):
        """Book tickets for one or more movies."""
        self.view_movies()

        while True:
            movie = input("\nEnter movie name to book (or 0 to finish): ").strip()
            
            if movie == "0":
                print("Finished booking tickets.")
                break
                
            if movie not in self._available_movies:
                print("Movie not available. Please check the movie name.")
                continue
                
            try:
                tickets = int(input(f"How many tickets for '{movie}'? "))
                if tickets <= 0:
                    print("Number of tickets must be greater than zero.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
                
            if movie in self._bookings:
                self._bookings[movie] += tickets
            else:
                self._bookings[movie] = tickets
                
            price = self._available_movies[movie]
            total = price * tickets
            print(f"Added {tickets} ticket(s) for '{movie}' - PHP {total:.2f}")
    
    def view_bookings(self):
        """View all current bookings and their total cost."""
        if not self._bookings:
            print("You haven't booked any tickets yet.")
            return
            
        print("\nYour Current Bookings:")
        print(LINE_SEPARATOR)
        
        total_cost = 0
        for movie, tickets in self._bookings.items():
            price = self._available_movies[movie]
            subtotal = price * tickets
            print(f"{movie}: {tickets} ticket(s) @ PHP {price:.2f} = PHP {subtotal:.2f}")
            total_cost += subtotal
            
        print(LINE_SEPARATOR)
        print(f"Total Cost: PHP {total_cost:.2f}")
    
    def generate_confirmation(self):
        """Generate a booking confirmation and clear the bookings."""
        if not self._bookings:
            print("You have no bookings to confirm.")
            return
            
        if not self._customer_name:
            print("Please set your name before confirming your booking.")
            self.set_customer_name()
            
            if not self._customer_name:
                return
        
        print("\n===== BOOKING CONFIRMATION =====")
        print(f"Customer: {self._customer_name}")
        print(f"Booking ID: JP{hash(self._customer_name) % 10000:04d}")
        print(LINE_SEPARATOR)
        
        total_cost = 0
        for movie, tickets in self._bookings.items():
            price = self._available_movies[movie]
            subtotal = price * tickets
            print(f"{movie}: {tickets} ticket(s) @ PHP {price:.2f} = PHP {subtotal:.2f}")
            total_cost += subtotal
            
        print(LINE_SEPARATOR)
        print(f"TOTAL AMOUNT: PHP {total_cost:.2f}")
        print("\nPlease present this confirmation at the counter.")
        print(f"Thank you for choosing MoviePlex, {self._customer_name}!")
        print("=============================")
        
        self._bookings.clear()
    
    def menu(self):
        """Display the MovieTicketManager menu and handle user interactions."""
        while True:
            print("\n[MoviePlex Ticket Booking System]")
            if self._customer_name:
                print(f"Customer: {self._customer_name}")
            if self._bookings:
                print(f"Current Bookings: {self.booking_count} movies, {self.total_tickets} tickets")
                
            print("1. Set Customer Name")
            print("2. View Available Movies")
            print("3. Book Movie Tickets")
            print("4. View My Bookings")
            print("5. Generate Booking Confirmation")
            print("0. Back to Main Menu")
            
            choice = input("Select an option: ")
            
            if choice == "0":
                break
                
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
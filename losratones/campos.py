import random

class DescribeMe:
    def __init__(self):
        print("Please enter the following details first:\n")
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.hometown = input("Enter your hometown: ")
        self.movie = input("Enter your favorite movie: ")
        self.dream = input("Enter your dream: ")

    def describe_name(self):
        response = random.choice([
            f"{self.name}, your name is wonderful!",
            f"{self.name}... it's alright.",
            f"{self.name}? are you serious? that's so unoriginal!"
            ])
        print(f"\n---\n{response}\n---\n")

    def describe_age(self):
        if self.age < 18:
            self.describe_young_age()
        else:
            self.describe_old_age()

    def describe_young_age(self):
        response_young = random.choice([
            f"{self.age} years old? You're just a kid!",
            f"Wow, {self.age} years old! enjoy your youth!",
            f"{self.age} years? Go help your parents with chores!"
        ])
        print(f"\n---\n{response_young}\n---\n")
        
    def describe_old_age(self):
        response_old = random.choice([
            f"{self.age} years old? Your white hairs are showing!",
            f"At {self.age}, you're getting wiser!",
            f"You're {self.age} already! Go get a job!"
        ])
        print(f"\n---\n{response_old}\n---\n")

    def describe_hometown(self):
        response = random.choice([
            f"{self.hometown} is a nice place, isn't it?",
            f"{self.hometown}... I've heard of it, but never been there.",
            f"{self.hometown}? Sounds like a place I'd avoid!"
        ])
        print(f"\n---\n{response}\n---\n")

    def describe_movie(self):
        response = random.choice([
            f"{self.movie} is a great movie! I love it!",
            f"{self.movie}? I've never seen it, but I'm sure it's okay.",
            f"{self.movie}... really? That's your favorite?"
        ])
        print(f"\n---\n{response}\n---\n")

    def describe_dream(self):
        response = random.choice([
            f"Your dream is to {self.dream}? That's inspiring!",
            f"{self.dream}... I hope you achieve it!",
            f"{self.dream}? Sounds like a fantasy!"
        ])
        print(f"\n---\n{response}\n---\n")
    
    def exit_program(self):
        print("Exiting program. Goodbye!")
        exit()

    def display_menu(self):
        input("\nPress Enter to continue...")
        print("\n--- Welcome to DescribeBot ---\n")
        print("1. Say something about your name")
        print("2. Say something about your age")
        print("3. Say something about your hometown")
        print("4. Say something about your favorite movie")
        print("5. Say something about your dream")
        print("6. Exit")

    def handle_choice(self, choice):
        options = {
            "1": self.describe_name,
            "2": self.describe_age,
            "3": self.describe_hometown,
            "4": self.describe_movie,
            "5": self.describe_dream,
            "6": self.exit_program
        }
        if choice in options:
            options[choice]()
        else:
            print("\nInvalid choice. Please try again.")

    def menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            self.handle_choice(choice)

if __name__ == "__main__":
    user = DescribeMe()
    user.menu()
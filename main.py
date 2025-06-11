from losratones.campos import DescribeMe
from losratones.manicio import Manicio
from losratones.reduta import BankingSystem
from losratones.rodriguez import MovieTicketManager

PAUSE_MESSAGE = "Press Enter to Continue..."

while True:
    print(
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
        "Welcome to Los Ratones Classes!",
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
        "1. Campos, Kenji Enishi",
        "2. Manicio, Dion Kylo",
        "3. Reduta, Paul Benidict",
        "4. Rodriguez, John Paul",
        "5. Exit", sep="\n"
        )
    
    user_choice = input("Please choose an option (1 - 5): ")
    
    try:
        user_choice = int(user_choice)
    except ValueError:
        print("Invalid input. Please choose between 1 to 5.")
        input(PAUSE_MESSAGE)
        continue

    match user_choice:
        case 1: 
            DescribeMe().menu()
            input(PAUSE_MESSAGE)
        case 2:
            Manicio().menu() 
            input(PAUSE_MESSAGE)
        case 3:
            BankingSystem().menu()
            input(PAUSE_MESSAGE)
        case 4:
            MovieTicketManager().menu()
            input(PAUSE_MESSAGE)
        case 5:
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please choose between 1 to 5.")
            input(PAUSE_MESSAGE)
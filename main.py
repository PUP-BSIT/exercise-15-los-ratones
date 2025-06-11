from losratones import campos
from losratones.manicio import Manicio
from losratones.reduta import BankingSystem

PAUSE_MESSAGE = "Press Enter to Continue..."

while True:
    print(
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
        "Welcome to Los Ratones Classes!",
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
        "1. Campos, Kenji Enish",
        "2. Manicio, Dion Kylo",
        "3. Reduta, Paul Benidict",
        "4. Rodriguez, John Paul",
        "5. Exit", sep="\n"
        )
    
    try:
        user_choice = int(input("Enter your choice (1 - 5): "))
    except ValueError:
        print("Invalid input. Please choose between 1 to 5.")
        input(PAUSE_MESSAGE)
        continue

    match user_choice:
        case 1: 
            campos.DescribeMe().menu()
            input(PAUSE_MESSAGE)
        case 2:
            manicio = Manicio()
            manicio.menu()
            input(PAUSE_MESSAGE)
        case 3:
            BankingSystem().menu()
            input(PAUSE_MESSAGE)
        case 4:
            #TODO(Rodriguez, John Paul): Implement your class here.
            pass
            input(PAUSE_MESSAGE)
        case 5:
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please choose between 1 to 5.")
            input(PAUSE_MESSAGE)
from losratones.manicio import Manicio

PAUSE_MESSAGE = "Press Enter to continue..."

while True:
    print(
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
        "Welcome to Los Ratones Classes!",
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
        "1. Campos, Kenji Enishi",
        "2. Gonot, Jedi Duncan",
        "3. Manicio, Dion Kylo",
        "4. Reduta, Paul Benidict",
        "5. Rodriguez, John Paul",
        "6. Exit", sep="\n"
        )
    
    try:
        user_choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input. Please choose between 1 to 6.")
        input(PAUSE_MESSAGE)
        continue

    match user_choice:
        case 1: 
            #TODO(Campos, Kenji Enishi): Implement your class here.
            pass
            input(PAUSE_MESSAGE)
        case 2:
            #TODO(Gonot, Jedi Duncan): Implement your class here.
            pass
            input(PAUSE_MESSAGE)
        case 3:
            manicio = Manicio()
            manicio.menu()
            input(PAUSE_MESSAGE)
        case 4:
            #TODO(Reduta, Paul Benidict): Implement your class here.
            pass
            input(PAUSE_MESSAGE)
        case 5:
            #TODO(Rodriguez, John Paul): Implement your class here.
            pass
            input(PAUSE_MESSAGE)
        case 6:
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please choose between 1 to 6.")
            input(PAUSE_MESSAGE)
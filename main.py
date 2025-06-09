PAUSE_MESSAGE = "Press Enter to continue..."

while True:
    print(
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
        "Welcome to Los Ratones Classes!",
        "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
        "1. Campos, Kenji Enishi",
        "2. Gonot, Jedi Duncan",
        "3. Manicio, Dion Kylo"
        "4. Reduta, Paul Benidict",
        "5. Rodriguez, John Paul",
        "6. Exit", sep="\n"
        )
    
    user_choice = int(input("Enter your choice (1-6): "))

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
            #TODO(Manicio, Dion Kylo): Implement your class here.
            pass
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
            print("Invalid choice. Please try again.")
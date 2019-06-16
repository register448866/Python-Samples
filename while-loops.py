help_text = """start - to start the car
stop - to stop the car
quit - to exit"""
command = ""
car_started = False

# WAITING FOR USER INPUT
while command != "quit":
    command = input("> ").lower()

    # USER ASKED FOR HELP
    if command == "help":
        print(help_text)

    # USER ASKED TO START THE CAR
    elif command == "start":
        if car_started: 
            print("Car already started") 
        else:
            car_started = True
            print("Car is started") 

    # USER ASKED TO STOP THE CAR
    elif command == "stop":
        if car_started:
            car_started = False
            print("Car is stopped")
        else:
            print("Car is already stopped")

    # USER ASKED TO QUIT THE GAME
    elif command == "quit":
        break

    # UNEXPECTED INPUT FROM USER
    else:
        print("I do not understand that...")
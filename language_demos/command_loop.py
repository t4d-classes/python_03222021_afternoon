

command = input("Please enter a command > ")


# the loop will loop so long as command is a non-zero length string
while command:

    if command == "cmd1":
        print("perform command 1")
        print("perform command 1")
    elif command == "cmd2":
        print("perform command 2")
    else:
        print("unknown command, please try again")

    command = input("Please enter a command > ")

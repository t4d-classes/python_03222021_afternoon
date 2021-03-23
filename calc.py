
result = 0

history = []


# def add_history_entry(history_list, p_history_entry_id, p_command, p_operand):
#     next_history_entry_id = history_entry_id + 1
#     # new_history_list = history_list.copy()
#     history_list.append((p_history_entry_id, p_command, p_operand))
#     return history_list, next_history_entry_id

def get_next_entry_id(history_list):
    return max([entry[0] for entry in history_list] or [0]) + 1


command = input("Please enter a command > ")


while command:

    if command == "add":
        operand = float(input("Please enter an operand > "))
        result = result + operand
        # history, history_entry_id = add_history_entry(
        #     history, history_entry_id, command, operand)
        history_entry_id = get_next_entry_id(history)
        history.append((history_entry_id, command, operand))
        print(f"Result: {result}")
    elif command == "subtract":
        operand = float(input("Please enter an operand > "))
        result = result - operand
        history_entry_id = get_next_entry_id(history)
        history.append((history_entry_id, command, operand))
        print(f"Result: {result}")
    elif command == "multiply":
        operand = float(input("Please enter an operand > "))
        result = result * operand
        history_entry_id = get_next_entry_id(history)
        history.append((history_entry_id, command, operand))
        print(f"Result: {result}")
    elif command == "divide":
        operand = float(input("Please enter an operand > "))
        result = result / operand
        history_entry_id = get_next_entry_id(history)
        history.append((history_entry_id, command, operand))
        print(f"Result: {result}")
    elif command == "remove":
        entry_id = int(input("Please enter a history entry id > "))
        for history_entry in history:
            if history_entry[0] == entry_id:
                history.remove(history_entry)
                break
    elif command == "clear":
        result = 0
        history = []
        print(f"Result: {result}")
    elif command == "history":
        print(" Id | Command   | Value ")
        print("------------------------")
        for history_entry in history:
            print(" | ".join([
                str(history_entry[0]).rjust(3),
                history_entry[1].ljust(9),
                str(history_entry[2]).ljust(6)
            ]))
    else:
        print("unknown command, please try again")

    command = input("Please enter a command > ")

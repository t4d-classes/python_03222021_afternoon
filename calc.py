from functools import reduce

calc_ops = [
    (1, "Add", "add", lambda x, y: x + y),
    (2, "Subtract", "subtract", lambda x, y: x - y),
    (3, "Multiply", "multiply", lambda x, y: x * y),
    (4, "Divide", "divide", lambda x, y: x / y),
    (5, "Exponent", "exponent", lambda x, y: x ** y),
]

history = []


def input_int(prompt):
    return int(input(prompt))


def input_float(prompt):
    return float(input(prompt))


def get_operand():
    return input_float("Please enter an operand: ")


def get_command():
    return input("Enter a command: ")


def get_history_entry_id():
    return input_int("Please enter a history entry id: ")


def next_entry_id(history_list):
    return max([entry[0] for entry in history_list] or [0]) + 1


def create_history_entry(entry_id, op_name, op_value):
    return (entry_id, op_name, op_value)


def append_history_entry(history_list, op_name, op_value):

    new_history_entry = create_history_entry(
        next_entry_id(history_list), op_name, op_value)

    history_list.append(new_history_entry)


def get_calc_op_by_cmd(calc_ops_list, cmd):
    for calc_op in calc_ops_list:
        if calc_op[2] == cmd:
            return calc_op


def perform_calc_op(result, entry):
    calc_op = get_calc_op_by_cmd(calc_ops, entry[1])
    calc_op_fn = calc_op[3]
    return calc_op_fn(result, entry[2])


def calc_result(history_list, calc_ops_list):
    return reduce(perform_calc_op, history_list, 0)

    # result = 0
    # for entry in history_list:
    #     calc_op = get_calc_op_by_cmd(calc_ops_list, entry[1])
    #     calc_op_fn = calc_op[3]
    #     result = calc_op_fn(result, entry[2])

    # return result

# def op_counts_str(accumulator, current):


def op_counts_str(op_counts_output, op_count):
    print(op_counts_output, op_count)
    return op_counts_output + " " + op_count[0] + ": " + str(op_count[1])


def display_operation_counts(history_list):

    op_counts = []

    for calc_op in calc_ops:
        op_counts.append(
            (calc_op[1], len([entry for entry in history_list
                              if entry[1] == calc_op[2]])))

    print("Op Counts")
    print("---------")
    # for oplabel, opcount in op_counts:
    #     print(f"{oplabel}: {opcount}")

    print(
        " ".join([f"{oplabel}: {opcount}" for oplabel, opcount in op_counts]))

    # print(reduce(op_counts_str, op_counts, ""))


def display_history(history_list):
    print(" Id | Op Name | Op Value ")
    print("-------------------------")
    for history_entry in history_list:
        print(" | ".join([
            str(history_entry[0]).rjust(3),
            history_entry[1].ljust(7),
            str(history_entry[2]).rjust(8)]))


def remove_history_entry(history_list, entry_id):
    for entry in history_list:
        if entry[0] == entry_id:
            history_list.remove(entry)
            break


command = "clear"

while command:

    if command == "history":
        display_history(history)
        display_operation_counts(history)
    elif command == "remove":
        history_entry_id = get_history_entry_id()
        remove_history_entry(history, history_entry_id)
    elif command == "clear":
        history = []
        print("Result: " + str(calc_result(history, calc_ops)))
    else:
        num = get_operand()
        append_history_entry(history, command, num)
        print("Result: " + str(calc_result(history, calc_ops)))

    command = get_command()

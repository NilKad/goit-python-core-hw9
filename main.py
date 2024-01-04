import sys
from types import NoneType


phonebook = [
    {"name": "Aleksandr", "phone": "+380671234567"},
    {"name": "Dima", "phone": "+380672345678"},
    {"name": "Nikita", "phone": "+380673456789"},
]


def one_params(func):
    # input - name
    # You didn't provide a name
    def wraper(*args):
        if len(args[0]) == 0:
            print("You didn't provide a name")
            return False

        # print(type(func))
        if isinstance(func, bool):
            return True

        return func(*args)

    return wraper


def input_error(func):
    # two params - name, phone
    # You didn't provide a phone number
    # You did not enter your name and phone number
    def wraper(*args):
        # print(f"TWO *args: {args[0]}")
        print(f'func name: {func.__name__}')
        res1 = one_params(False)
        res_1 = res1(*args)
        # if one_params not validate
        # if isinstance(res_1, NoneType):
        if not res_1:
            return

        if (len(args[0])) < 2:
            print("You didn't provide a phone number")
            return

        _, phone = args[0]

        if not phone.replace("+", "").isdigit():
            print(f"invalid phone number format - {args[0][1]}")
            return

        # print(f"TWO check before args: {args}")
        result = func(*args)
        # print(f"TWO check after args: {args}")

        return result

    return wraper


def hello(*args):
    print("How can I help you?")
    return


def find_name(name):
    for i in range(len(phonebook)):
        if phonebook[i]["name"] == name:
            return i
    return -1


@input_error
def handler_add(*args):
    name, phone = args[0]
    idx = find_name(name)
    if idx >= 0:
        print(f"name {name} already exists")
        return
    phonebook.append({"name": name, "phone": phone})
    print(f"Success added, name: {name}, phone: {phone}")
    # print(f"____phonebook: {phonebook}")
    return ""


@input_error
def handler_change(*args):
    name, phone = args[0]
    idx = find_name(name)
    if idx < 0:
        print(f"{name} there is no such.")
        return
    phonebook[idx]["phone"] = phone
    print(f"Success change, name: {name}, phone: {phone}")
    # print(phonebook)
    return ""


@one_params
def handler_phone(*args):
    name, *phone = args[0]
    idx = find_name(name)
    if idx < 0:
        print(f"{name} there is no such.")
        return
    print(phonebook[idx]["phone"])
    return


def handler_show_all(*args):
    for el in phonebook:
        print(f'{el['name']}: {el['phone']}')
    print()
    # print(phonebook)
    return []


def handler_end_program(*args):
    print("Good bye!")

    sys.exit()


command_list = {
    "hello": hello,
    "add": handler_add,
    "change": handler_change,
    "phone": handler_phone,
    "show all": handler_show_all,
    "good bye": handler_end_program,
    "close": handler_end_program,
    "exit": handler_end_program,
    "quit": handler_end_program,
}


def command_parse(string):
    string_lower = string.lower().strip()
    command_find = list(
        filter(lambda key: string_lower.startswith(key), command_list.keys())
    )
    # if find
    if len(command_find) == 0:
        print("command not found")
        return
    command_current = command_list[command_find[0]]
    command_parameters = string.replace(command_find[0], "").strip().split()
    # print(f"string: {string}")
    # print(f'len: {len(string.replace(command_find[0], "").strip())}')
    # print(f"command_find: {command_find}")
    # print(f"command_current: {command_current}")
    # print(f"command_parameters: {command_parameters}")
    command_current(command_parameters)
    return ""


while True:
    # command_input = input("Input command: ")
    # command_input = "hello sasha 124"
    command_input = "add sasha +124"
    # command_input = "add Aleksandr1 +124"
    # command_input = "add "
    # command_input = "add sasha"
    # command_input = "add 124"
    # command_input = "change Aleksandr +124"
    # command_input = "phone Aleksandr"
    # command_input = "show all"
    if command_input == "":
        continue
    func = command_parse(command_input)

    # end_program()
    break

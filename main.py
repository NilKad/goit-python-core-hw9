import sys
import traceback
from types import NoneType


phonebook = [
    {"name": "Aleksandr", "phone": "+380671234567"},
    {"name": "Dima", "phone": "+380672345678"},
    {"name": "Nikita", "phone": "+380673456789"},
]

def print_boolean(bool):
    if bool:
        print('True')
    else:
        print('False')

# def check_phone_number(phone):
#     return ''


# DECORATOR input_error
def input_error(func):
    # two params - name, phone
    # You didn't provide a phone number
    # You did not enter your name and phone number

    one_params = ['handler_phone']

    def wraper(*args):
        # print(f'func name: {func.__name__}') #print 
        
        # print (args[0])
        result = None
        try:
            is_need_one_params = func.__name__ in one_params
            len_args = len(args[0])
            
            if is_need_one_params and len_args < 1:
                raise ValueError('Give me name please')
            elif not is_need_one_params and len_args < 2: 
                raise ValueError('Give me name and phone please')

            result = func(*args)

        except ValueError as e:
            print(f'------- ValueError: {e}')

        except KeyError as e:
            print(f'------- keyerror: {e}')

        except IndexError as e:
            print(f'------- IndexError: {e}')

        except Exception as e:
            print('------ EXCEPTION - Exception {e}')
            # tb = sys.exc_info()

        return result

    return wraper


def find_name(name):
    for i in range(len(phonebook)):
        if phonebook[i]["name"] == name:
            return i
    return -1

def handler_hello(*args):
    print("How can I help you?")
    return

@input_error
def handler_add(*args):
    name, phone = args[0]
    idx = find_name(name)
    contact = {'name': name, 'phone': phone}
    if idx >= 0:
        raise ValueError(f"name {name} already exists")
    phonebook.append(contact)
    # print(f"Success added, name: {name}, phone: {phone}")
    # print(f"____phonebook: {phonebook}")
    return f'{name} {phone}'


@input_error
def handler_change(*args):
    name, phone = args[0]
    idx = find_name(name)
    contact = {'name': name, 'phone': phone}
    if idx < 0:
        raise ValueError(f"{name} there is no such.")
    phonebook[idx]["phone"] = phone
    # print(f"Success change, name: {name}, phone: {phone}")
    # print(phonebook)
    return f'{name} {phone}'



@input_error
def handler_phone(*args):
    name, *phone = args[0]
    idx = find_name(name)
    if idx < 0:
        raise ValueError(f"{name} there is no such.")
    # print(phonebook[idx]["phone"])
    return phonebook[idx]["phone"]

# @input_error
def handler_show_all(*args):
    res = ''
    for el in phonebook:
        res += f'{el['name']}: {el['phone']}\n'
    # print()
    # print(phonebook)
    return res


# @input_error
def handler_end_program(*args):
    print("Good bye!")
    sys.exit()


command_list = {
    "hello": handler_hello,
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
    res = command_current(command_parameters)
    return res


while True:
    command_input = input("Input command: ")
    # command_input = "hello sasha 124"
    # command_input = "add sasha +124"
    # command_input = "add Aleksandr1 +124"
    # command_input = "add Aleksandr +124"
    # command_input = "add "
    # command_input = "add sasha"
    # command_input = "add 124"
    # command_input = "change Aleksandr1 +124"
    # command_input = "change Aleksandr +124"
    # command_input = "change "
    # command_input = "change Aleksandr "
    # command_input = "phone Aleksandr"
    # command_input = "phone Aleksandr12"
    # command_input = "phone"
    # command_input = "show all"
    if command_input == "":
        continue
    res = command_parse(command_input)
    print(res) 
    # end_program()
    # break

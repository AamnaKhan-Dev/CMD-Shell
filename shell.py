builtin_cmd=["echo", "type", "exit 0"]
while True:
    user_input=input("$ ")
    cmd_list=user_input.split(" ")
    match cmd_list:
        case ["exit", "0"]:
             exit()
        case ["echo", *arg]:
             print(*arg)
        case ["type", *arg]:
            str=" ".join(arg)
            if str in builtin_cmd:
                print(f"{str} : is a shell builtin")
            else:
                print(f"{str} : is not a builtin shell")
        case _:
            print(f"{user_input}: command not found")
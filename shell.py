while True:
    user_input=input("$ ")
    if user_input == "exit 0":
        exit()
    elif user_input[0:5] == "echo ":
        print(user_input[5:])
    else:
        print(f"{user_input}: command not found")
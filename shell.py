import os
builtin_cmd=["echo", "type", "exit 0", "pwd", "cd"]
extensions=[".exe"]
def getPath(cmd):
    paths=os.getenv("PATH").split(os.pathsep)
    for path in paths:
        for ext in extensions:
            full_path=os.path.join(path, cmd+ext)
            if os.path.exists(full_path):
                return full_path
    return None
            
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
            full_path=getPath(str)
            if str in builtin_cmd:
                print(f"{str} : is a shell builtin")
            elif full_path:
                print(f"{str} : is {full_path}")
            else:
                print(f"{str} : is not a builtin shell")
        case ["pwd"]:
            print(os.getcwd())
        case ["cd", *arg]:
            cmd=" ".join(arg)
            os.chdir(cmd)
        case _:
            print(f"{user_input}: command not found")
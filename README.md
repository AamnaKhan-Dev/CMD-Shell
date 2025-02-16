# Command Shell Emulator Documentation

## Overview
This program is a simple command-line emulator written in Python. It continuously takes user input and processes specific commands while providing error messages for unrecognized inputs.

## Features
- Supports an `echo` command to print user-provided text.
- Recognizes the `exit 0` command to terminate execution.
- Handles unrecognized commands by displaying an error message.

## Code Explanation
```python
while True:
    user_input = input("$ ")  # Prompt user for input
    if user_input == "exit 0":  # Exit condition
        exit()
    elif user_input[0:5] == "echo ":  # Check for echo command
        print(user_input[5:])  # Print everything after "echo "
    else:
        print(f"{user_input}: command not found")  # Handle unrecognized commands
```

## Functionality
1. **User Input Handling**
   - The program continuously waits for user input using `input("$ ")`.
   - The loop ensures the program runs indefinitely unless explicitly terminated.

2. **Exit Command (`exit 0`)**
   - If the user types `exit 0`, the program calls `exit()`, terminating execution.

3. **Echo Command (`echo <message>`)**
   - If the input starts with `echo `, the program extracts and prints the text following it.

4. **Unknown Command Handling**
   - If the input does not match the above conditions, the program prints an error message: `<command>: command not found`.

## Example Usage
```
$ echo Hello, World!
Hello, World!

$ invalid_command
invalid_command: command not found

$ exit 0
```

## Limitations
- Does not handle leading or trailing spaces efficiently.
- Only recognizes `exit 0` as an exit command (e.g., `exit` alone will not work).
- Cannot process complex shell-like commands.

## Possible Improvements
- Implement support for additional shell commands.
- Enhance input parsing to handle extra spaces and variations.
- Add error handling for edge cases (e.g., empty input).
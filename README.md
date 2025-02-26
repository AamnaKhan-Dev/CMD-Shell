# Shell.py - A Simple Command Line Emulator

## Overview
`shell.py` is a basic command line emulator that supports a limited set of built-in commands. It mimics a Unix shell environment with basic functionalities like printing the current directory, changing directories, echoing text, and checking command types. The script makes use of the `os` module to interact with the operating system, including handling directory navigation and retrieving environment variables like `PATH`.

## Features
- Execute built-in commands:
  - `echo [args]`: Prints the provided arguments.
  - `type [command]`: Checks if a command is a built-in or external executable.
  - `pwd`: Prints the current working directory.
  - `cd [directory]`: Changes the current working directory.
  - `exit 0`: Exits the shell.
- Supports searching for executables in system `PATH` with `.exe` extensions (for Windows compatibility), leveraging environment variables.
- Handles unrecognized commands with an error message.

## Requirements
- Python 3.x
- OS: Windows, Linux, or macOS

## Installation
1. Clone or download this repository.
2. Ensure Python is installed on your system.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing `shell.py`.
3. Run the script:
   ```sh
   python shell.py
   ```
4. Use supported commands within the shell prompt (`$`).
5. To exit, type:
   ```sh
   exit 0
   ```

## Example Commands
```sh
$ echo Hello, world!
Hello, world!

$ pwd
/home/user

$ type pwd
pwd : is a shell builtin

$ cd Documents

$ pwd
/home/user/Documents

$ exit 0
```

## Limitations
- Only supports predefined built-in commands.
- Does not execute external commands apart from checking their paths.
- No support for piping or redirection.

## License
This project is open-source and free to use under the MIT License.

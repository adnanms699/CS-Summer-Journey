todo = []
completed = []
while True:
    for i in range (len(todo)):
        print(f"{i+1} {todo[i]}")
    print("****************")
    print("Enter a command. Type h for help.")
    command = input(" > ")
    if command == "q":
        break
    elif command.isnumeric():
        index = int(command) -1
        if index >= (len(todo)):
            print("Invalid index.")
        else:
            done = todo.pop(index)
            completed.append(done)
    else:
        todo.append(command)
if completed:
    print("You completed the following tasks:")
    for todo in completed:
        print(f"* {todo}")

# GET 2 EMPTY LISTS
# START A WHILE LOOP
# GIVE A FOR LOOP TO PRINT THE TODO LIST with sorting like 1...2..3...(use f string)
# PRINT A FEW STATEMENTS TO THE USER LIKE * OR ENTER A COMMAND
# ASK FOR A COMMAND
# GIVE SOME CONDIIONALS LIKE IF Q THEN BREAK AND IF H ITS GIVES INFO ABT THE STUFF
# IF ITS NUMBER THEN IT REMOVES THAT INDEX FROM THE TODO LIST AND ADDS IT IN A ANOTHER VARIABLE WHICH WE APPEND TO THE LAST COMPLETED LIST
# IF ITS NOT A NUMBER THEN IT APPENDS THE COMMAND TO THE TODO LIST
# AFTER THE WHILE LOOP ENDS, PRINT THE COMPLETED LIST IF IT HAS ANYTHING IN IT
# AND PRINT THE TODO LIST IF IT HAS ANYTHING IN IT
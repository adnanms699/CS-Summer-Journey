todo = []
completed =[]
while True:
    for i in range(len(todo)):
        print(f"{i+1}. {todo[i]}")
    print("***************")
    print("Enter a command: type h for help")
    command = input(" > ")
    if command == "q":
        break
    elif command.isnumeric():
       indx = int(command) -1
       if indx >= (len(todo)):
            print("Invalid task number.")
       else:
            done =todo.pop(indx)
            completed.append(done)
    elif command == "h":
        print("type h for help")
        print("type q to quit")
        print("type the specific task number to mark it as completed")
    else:
        todo.append(command)
if completed:
    print("You completed the following tasks:")
    for todo in completed:
        print(f"* {todo}")


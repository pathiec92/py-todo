import modules.functions as fun

prompt = "Enter todo\n"

options = "add/show/q\n"
todos = []



help(fun.save)
help(fun.get_todos)

while True:
    op = input(options)
    if "a!" in op:
        todo = op[3:] + "\n"
        todos = fun.get_todos()
        print(todos)
        todos.append(todo)
        fun.save(todos)

    elif "s!" in op:
        todos = fun.get_todos()
        new_todos = [item.strip("\n") for item in todos]
        for i, t in enumerate(new_todos):
            print(i, t)

    elif "e!" in op:
        try:
            todo = op[3:] + "\n"
            todos = fun.get_todos()
            print(todos)
            idx = int(todo)
            todo = input("Enter modified todo\n") + "\n"
            todos[idx] = todo
            fun.save(todos)
        except ValueError as ex:
            print(ex)
            print("Invalid input")
    elif "!" in op:
        print("Quit")
        break
    else:
        print("Invalid command")
    # match op:
    #     case "a":
    #         todo = input(prompt) + "\n"
    #         with open("todo.txt", "r") as file:
    #             todos = file.readlines()
    #             print(todos)
    #             todos.append(todo)
    #
    #         with open("todo.txt", "w") as file:
    #             file.writelines(todos)
    #             print(todos)
    #     case "s":
    #         with open("todo.txt", "r") as file:
    #             todos = file.readlines()
    #             new_todos = [item.strip("\n") for item in todos]
    #             for i, t in enumerate(new_todos):
    #                 print(i, t)
    #     case "q":
    #         print("Quit")
    #         break
    #     case _:
    #         print("Invalid command")
print("End")

# if op in "a":
# elif op in "s":
# elif op in "q":
# else: print("not a valid command")

# op[start:end:step]

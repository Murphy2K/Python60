#Seda kasuta kui ei ole palju funktsioone seal failis
#from functions import get_todos, write_todos

"""
Seda kasuta siis kui on seal failis palju funktsioone
Muidugi siis pead kasutama funktsioone nii:
Todos = functions.get_todos()
See on ka tegelikult parem varjant...
sest nüüd saad need lisa failid lisada teise kausta."todos.txt"
ntx on faili asukoht .../Documents/Python60/failid/functions.py
siis näeb rida välja selline:
from failid import functions
ja tulemus on sama.
"""
import functions
import time


now = time.strftime("%d %B %Y %H:%M") 
print("Praegu on: ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("show"):
        for index, item in enumerate(get_todos()):
            print(f"{index + 1}. {item.strip()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Andsid vale käsu...")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            todos = get_todos()
            todo_to_remove = todos.pop(number).strip()
            write_todos(todos)
            print(f"Todo {todo_to_remove} on lõpetatud.")
        except IndexError:
            print("Sellist ülesannet pole...")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Vale asja kirjutasid...")

print("Bye!")

class TodoList:
    def __init__(self):
        self.tasks = []

    def addt(self, task):
        self.tasks.append(task)

    def rmvt(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed")
        else:
            print("Invalid task index. try again.")

    def dply_tsk(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
        else:
            print(" To-Do List is empty")

    def updt_t(self, index, new_t):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_t
            print("Task updated")
        else:
            print("Invalid task index. Please try again.")

def main():
    todo_list = TodoList()

    while True:
        print("\n...To-Do List Menu...")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.addt(task)
        elif choice == '2':
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.rmvt(index)
        elif choice == '3':
            index = int(input("Enter task index to update: ")) - 1
            new_task = input("Enter new task: ")
            todo_list.updt_t(index, new_t)
        elif choice == '4':
            todo_list.dply_tsk()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
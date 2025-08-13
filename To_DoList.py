import os

class TodoList:
  def __init__(self, filename='tasks.txt'):
    self.filename = filename
    self.tasks = self.load_tasks()

  def load_tasks(self):
    if not os.path.exists(self.filename):
      return []
    with open(self.filename, 'r') as file:
      return [line.strip() for line in file.readlines()]

  def save_tasks(self):
    with open (self.filename, 'w') as file:
      for task in self.tasks:
        file.write(task + '\n')

  def add_task(self, task):
    self.tasks.append(task)
    self.save_tasks()
    print(f'Task "{task}" added.')

  def view_tasks(self):
    if not self.tasks:
      print("No tasks available.")
      return 
    print("Your tasks:")
    for index, task in enumerate(self.tasks, start=1):
      print(f"{index}. {task}")

  def update_task(self, index, new_task):
    if 0 <= index < len(self.tasks):
      old_task = self.tasks[index]
      self.tasks[index] = new_task
      self.save_tasks() 
      print(f'Task "{old_task}" updated to "{new_task}".')
    else:
      print("Invalid task number")

  def delete_task(self, index):
    if 0 <= index < len(self.tasks):
      removed_task = self.tasks.pop(index)
      self.save_tasks()
      print(f'Task "{removed_task}" deleted.')
    else:
      print("Invalid task number")

def main():
  todo_list = TodoList()

  while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ") 

    if choice == '1': 
      task = input("Enter the task: ")
      todo_list.add_task(task)
    elif choice == '2': 
      todo_list.view_tasks()
    elif choice == '3':
      todo_list.view_tasks()
      index  = int(input("Enter the task number to update: ")) - 1
      new_task = input("Enter the new task: ")
      todo_list.update_task(index, new_task)
    elif choice == '4':
      todo_list.new_tasks()
      index = int(input("Enter the task number to delete: ")) - 1 
      todo_list.delete_task(index)
    elif choice == '5':
      print("Exiting the To-Do List App.")
      break
    else: 
      print("Invalid choice. Please try again.") 

if __name__=="__main__":
  main()        

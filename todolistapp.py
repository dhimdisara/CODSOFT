""""""
"""CODSOFT INTERN"""
"""PYTHON PROGRAMMING INTERNSHIP , 25 MARCH 2024"""
"""TASK 1 """
"""TO DO LIST APP"""
def add_task(tasks,task_description,due_date=None, priority = None):
        """
        This function adds a new task to the provided to-do list.

        Args:
            tasks (list): The list to store tasks.
            task_description (str): The description of the task.
            due_date (str, optional): The due date of the task (optional). Defaults to None.
            priority (int, optional): The priority level of the task (optional). Defaults to None.

        Returns:
            str: A message indicating success or error.
        """

        # Error handling for empty task description
        if not task_description :
                return "Error: Enter a task description"

        # Validate priority (optional)
        if priority is not None:
                try:
                        priority=int(priority)
                        if priority < 1:
                            return "Error: Priority must be  a positive integer."

                except ValueError:
                  return "Error: Priority must be a number"

        # Create a task dictionary
        task={"Task Description:": task_description , "Due Date:" : due_date , "Priority:": priority}

        # Add task to the list
        tasks.append(task)
        return "Task added successfully."

# Example usage
tasks=[]

while True:
        task_description=input("Enter a task description or enter q to quit.")
        if task_description.lower() == "q":
                        break
        # Implement validation for priority data type (optional)
        due_date=str(input("enter a due date, str (optional)"))

        # Handle potential errors in due date format (implementation left as an exercise)
        priority=int(input("enter a priority (optional), integer"))


        message=add_task(tasks,task_description, due_date, priority)
        print(message)

# Improve task display logic based on your storage method (in-memory or persistent)
print("your tasks:")
for task in tasks:
        print(f"-{task['Task Description:']}")







works = []


def add_work(work):
    works.append(work)
    print("Work added successfully!")


def view_work():
    print("Your To-Do List:")
    if works:
        for index, work in enumerate(works, start=1):
            print(f"{index}. {work}")
    else:
        print("No tasks available!")


def edit_work():
    view_work()
    if works:
        try:
            task_num = int(input("Enter the number of the work you want to edit: "))
            if 1 <= task_num <= len(works):
                new_work = input("Enter the new work: ")
                works[task_num - 1] = new_work
                print("Task updated successfully!")
            else:
                print("Invalid work number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("There are no work to edit.")


while True:
    print("\nMenu:")
    print("1. Add Work")
    print("2. View Work")
    print("3. Edit Work")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        work = input("Enter the work: ")
        add_work(work)
    elif choice == "2":
        view_work()
    elif choice == "3":
        edit_work()
    elif choice == "4":
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid choice. Please try again.")

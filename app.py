def task():
    tasks=[]
    print("---Welcome to the task Management App---")

    total_task=int(input("Enter how many tasks you want to add="))
    for i in range(1,total_task+1):
        task_name=input(f"enter task {i}=")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")
    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        
        if operation == 1 :
            Add=input("enter your task you want to add=")
            tasks.append(Add)
            print("your task {add} has sucessfully added....")

        elif operation == 2:
            updated_val=input("enter the task you want to update=")
            if updated_val in tasks:
                up=input("enter your task=")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print("task is updated{up}")

        elif operation == 3:
            del_val=input("enter your task you want to del=")
            if del_val in tasks:  
                ind=tasks.index(del_val)
                del tasks[ind]
                print("task {del_val} has been deleted...")

        elif operation == 4:
            print(f"Total tasks = {tasks}")      

        elif operation == 5:
            print("closing the program...")
            break
        else:
            print("invalid input")
task()  




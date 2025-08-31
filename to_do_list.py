# to do list

task = []

task.append("excersize should be done")
task.append("book reading")
task.append("some excersize of python")

for tasks in task:
    print("-", tasks)
task.pop(2)
for tasks in task:
    print(tasks)
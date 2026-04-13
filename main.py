import json

def create_task(name_tasks, *tasks):
    user_task = {
        name_tasks : [*tasks],
    }

    with open("tasks/test.json", 'w', encoding='utf-8') as file:
        data = json.dump(user_task, file, indent=4)
    return data

def append_task(name_tasks, *tasks):
    # user_task = {
    #     name_tasks : [*tasks]
    # }
    with open('tasks/test.json', 'r', encoding='utf-8') as file:
        dicts = json.load(file)

    dicts[name_tasks] = [*tasks]

    with open('tasks/test.json', 'w', encoding='utf-8') as file:
        data = json.dump(dicts, file, indent=4)
    return data

def read_task(name_tasks):
    '''Выводить все задачи, которые есть''' 
    with open("tasks/test.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return '\n'.join(data[name_tasks])

def clear_task():
    '''Очищает json-файл с задачами'''
    with open("tasks/test.json", 'w', encoding='utf-8') as file:
        pass

create_task('tasks', 'приготовить', 'подрочить')
append_task('task1', 'приготовить', 'подрочить')
append_task('task2', 'подрочить')
clear_task()


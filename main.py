import json

def create_task(name_tasks, task):
    user_task = {
        name_tasks : [task],
    }
    with open("tasks/test.json", 'w', encoding='utf-8') as file:
        json.dump(user_task, file, indent=4)
    print('Файл с задачами успешно создан')


def append_task(operation):
    with open('tasks/test.json', 'r', encoding='utf-8') as file:
        dicts = json.load(file)

    if operation.lower() == 'файл':
        try:
            name_tasks = input('Имя файла: ')
            dicts[name_tasks] = []
            with open('tasks/test.json', 'w', encoding='utf-8') as file:
                data = json.dump(dicts, file, indent=4)
            print('Файл успешно создан')
        except:
            print('Произошла ошибка')
        
    elif operation.lower() == 'задача':
        try:
            task = [x for x in input('Введите свои задачи через пробел: ').split()]
            name_file = input('Введите имя файла куда хотите сохранить задачи: ')
            dicts[name_file] = task

            with open('tasks/test.json', 'w', encoding='utf-8') as file:
                data = json.dump(dicts, file, indent=4)
            print('Задача успешна добавлена:)')
        except:
            print('Произошла ошибка')

def read_task(name_tasks):
    '''Выводить все задачи, которые есть''' 
    with open("tasks/test.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return '\n'.join(data[name_tasks])

def clear_task():
    '''Очищает json-файл с задачами'''
    with open("tasks/test.json", 'w', encoding='utf-8') as file:
        pass

def delete_task(name_tasks, task):
    with open("tasks/test.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    data[name_tasks].remove(task)

    with open('tasks/test.json', 'w', encoding='utf-8') as file:
        data = json.dump(data, file, indent=4)

def compl_tasks(name_task):
    completed_tasks = []
    completed_tasks.append(name_task)
    return completed_tasks

complited_vocab = {}

while True:

    command = int(input('''
1 - Создать первый файл с задачами
2 - Создать задачу или файл
3 - Просмотреть все задачи
4 - Удалить все файлы
5 - Отметить задачу выполненной 
6 - Просмотреть выполненные задачи
\n'''))

    match command:
        case 1:
            name_task_file = input('Введите файл для задач: ')
            first_task = input('Напишите свою первую задачу: ')
            create_task(name_task_file, first_task)

            read_first_task = input(f"Желаете посмотреть задача в файле {name_task_file}?(Да/Нет):")
            print('\nЗадачи:')
            print(read_task(name_task_file)) if read_first_task == 'Да' else None

        case 2:
            operation = input('Что вы хотите создать(Файл/Задача): ')
            append_task(operation)

        case 3:
            name_file = input('Введите имя файла для просмотра задач: ')
            print(read_task(name_file))

        case 4:
            clear_task()
            print('Все файлы с задачами удалены удалены')

        case 5:
            name_file = input('Введите имя файла, где хранится задача: ')
            print(read_task(name_file) + '\n')
            name_task = input('Введите задачу которую хотите пометить выполненной: ')
            delete_task(name_file, name_task)
            complited_vocab[name_file] = [name_task]
        case 6:
            name_task_file = input('Введите название файла для просмотра выполненных задач: ')
            print(' '.join(complited_vocab[name_task_file]))

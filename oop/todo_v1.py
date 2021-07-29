from datetime import datetime

class Task:
    def __init__(self, desc):
        self.desc = desc
        self.done = False
        self.creation = datetime.now()

    def complete(self):
        self.done = True

    def __str__(self):
        return self.desc + (' (Complete)' if self.done else '')


def main():
    home = []
    home.append(Task('Iron clothes'))
    home.append(Task('Wash dishes'))

    [task.complete() for task in home if task.desc == 'Wash dishes']
    for task in home:
        print(f'- {task}')


if __name__ == '__main__':
    main()

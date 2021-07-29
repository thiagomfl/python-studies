from datetime import date, datetime, timedelta

class TaskNotFound(Exception):
    pass


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    # Operator overload +=
    def __iadd__(self, task):
        task.owner = self
        self._add_task(task)

        return self

    def _add_task(self, task, **kwargs):
        self.tasks.append(task)

    def _add_new_task(self, desc, **kwargs):
        self.tasks.append(Task(desc, kwargs.get('deadline', None)))

    def add(self, task, deadline=None, **kwargs):
        # self.tasks.append(Task(desc, deadline)
        choosen_fn = self._add_task if isinstance(task, Task) else self._add_new_task
        kwargs['deadline'] = deadline
        choosen_fn(task, **kwargs)

    def pending(self):
        return [task for task in self.tasks if not task.done]

    def searching(self, desc):
        try:
            return [task for task in self.tasks if task.desc == desc][0]
        except IndexError as e:
            raise TaskNotFound(str(e))

    def __str__(self):
        return f'{self.name} ({len(self.pending())} pending task(s))'


class Task:
    def __init__(self, desc, deadline=None):
        self.desc = desc
        self.done = False
        self.deadline = deadline
        self.creation = datetime.now()

    def complete(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append('(Completed)')
        elif self.deadline:
            if datetime.now() > self.deadline:
                status.append('(Due date)')
            else:
                expiresIn = (self.deadline - datetime.now()).days
                status.append(f'(Expires in {expiresIn} days)')

        return f'{self.desc} ' + ' '.join(status)


class RecurringTask(Task):
    def __init__(self, desc, deadline, days=7):
        super().__init__(desc, deadline)
        self.days = days
        self.owner = None

    def complete(self):
        super().complete()
        new_deadline = datetime.now() + timedelta(days=self.days)
        new_task = RecurringTask(self.desc, new_deadline, self.days)

        if self.owner:
            self.owner += new_task

        return new_task


def main():
    timedate = datetime.now() + timedelta(days=3, minutes=12)

    home = Project('Homework')
    home.add('Iron clothes')
    home.add('Wash dishes', timedate)
    home.add('Sweep the room')
    home.add('Take out the trash')
    home.add(home.searching('Make the bed').complete())
    home += RecurringTask('Change sheets', datetime.now(), 7)
    print(home)

    try:
        home.searching('Wash dishes - Erro').complete()
    except TaskNotFound as e:
        print(f'The caus was "{str(e)}"!')

    home.searching('Wash dishes').complete()

    for task in home:
        print(f'- {task}')
    
    print(home)

    market = Project('Shopping in the market')
    market.add('Dry fruits')
    market.add('Meat', timedate)
    market.add('Tomato')
    print(market)

    buy_meat = market.searching('Meat')
    buy_meat.complete()

    for task in market:
        print(f'- {task}')


if __name__ == '__main__':
    main()

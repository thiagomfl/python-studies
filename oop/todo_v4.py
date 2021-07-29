from datetime import date, datetime, timedelta

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def add(self, desc, deadline=None):
        self.tasks.append(Task(desc, deadline))

    def pending(self):
        return [task for task in self.tasks if not task.done]

    def searching(self, desc):
        # Possible IndexError
        return [task for task in self.tasks if task.desc == desc][0]

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


def main():
    home = Project('Homework')
    home.add('Iron clothes', datetime.now())
    timedate = datetime.now() + timedelta(days=3, minutes=12)
    home.add('Wash dishes', timedate)
    home.add('Sweep the room')
    home.add('Take out the trash')
    home.add('Make the bed')
    print(home)

    home.searching('Wash dishes').complete()

    for task in home:
        print(f'- {task}')
    
    print(home)

    market = Project('Shopping in the market')
    market.add('Dry fruits')
    market.add('Meat')
    market.add('Tomato')
    print(market)

    buy_meat = market.searching('Meat')
    buy_meat.complete()

    for task in market:
        print(f'- {task}')


if __name__ == '__main__':
    main()

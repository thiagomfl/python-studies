class Animal:
    @property
    def capacities(self):
        return ('sleep', 'eat', 'drink')


class Man(Animal):
    @property
    def capacities(self):
        return super().capacities + ('love', 'speak', 'study')


class Spider(Animal):
    @property
    def capacities(self):
        return super().capacities + ('do web', 'walk the walls')


class SpiderMan(Spider, Man):
    @property
    def capacities(self):
        return super().capacities + ('hit bandits', 'shoot webs between buildings')

    
if __name__ == '__main__':
    john = Man()
    print(f'John: {john.capacities}')

    spider = Spider()
    print(f'Spider: {spider.capacities}')

    peter = SpiderMan()
    print(f'Peter: {peter.capacities}')


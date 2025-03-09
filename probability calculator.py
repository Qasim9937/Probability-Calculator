from random import randrange
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key in kwargs.keys() for _ in range(kwargs[key]) ]

    def draw(self, num_to_draw):
        if num_to_draw <= len(self.contents):
            drawn = [self.contents.pop(randrange(0,len(self.contents))) for i in range(num_to_draw) ]
            return drawn   
        elif num_to_draw > len(self.contents): 
            drawn = [self.contents.pop(0) for i in range(len(self.contents))]
            return drawn       

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    x = []
    test = copy.deepcopy(hat)
    
    for i in range(num_experiments):
        drawn = test.draw(num_balls_drawn)
        x.append(drawn)
        test = copy.deepcopy(hat)

    
    y = []
    for item in x:
        check = 1
        for key,value in expected_balls.items():
            if item.count(key) < value:
                check = 0 
        y.append(check)

    probability = y.count(1) / num_experiments

    return probability
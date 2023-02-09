import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        contents = []
        for kwarg in kwargs:
            for _i in range(0, kwargs[kwarg]):
                contents.append(kwarg)
        self.contents = contents

    def draw(self, tries:int):
        l = []
        tries = min(tries, len(self.contents))
        for _i in range(0, tries):
            pos = random.randrange(len(self.contents))
            l.append(self.contents.pop(pos))
        return l


def experiment(hat:Hat, expected_balls, num_balls_drawn, num_experiments):
    matchedDrawn = 0
    expectedBallsCount = 0
    for type in expected_balls:
        expectedBallsCount += expected_balls[type]

    for _i in range(0, num_experiments):
        newHat = copy.deepcopy(hat)
        drawn = newHat.draw(num_balls_drawn)
        expectedDraw = 0
        for type in expected_balls:
            for _j in range(0, expected_balls[type]):
                try:
                    drawn.remove(type)
                except ValueError:                        
                    continue
                expectedDraw += 1
        if (expectedDraw == expectedBallsCount):
            matchedDrawn += 1 
        
    return matchedDrawn / num_experiments

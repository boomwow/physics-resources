# Sample Ball class
import numpy as np
import matplotlib.pyplot as plt

class Ball:
    # State variable is in the form [x, y, vx, vy]
    def __init__(self, mass=1, state=np.array([0, 0, 0, 0], dtype=float), bounce=1):
        self.mass = mass
        self.state = state
        self.bounce = bounce

    def update(self, dt):
        self.state[3] += -9.8 * dt
        self.state[1] += self.state[3] * dt
        print(self.state)


def test():

    jim = Ball()
    jim.state[1] = 1
    
    print(jim.state)
    for i in range(20):
        jim.update(.1)

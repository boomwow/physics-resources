# Sample Ball class
import numpy as np

class Ball:
    # State var in the form [x, y, vx, vy]
    def __init__(self, mass=1, state=np.array([0, 0, 0, 0], dtype=float), bounce=1):
        self.mass = mass
        self.state = state 
        self.bounce = bounce

    def update(self, dt):
        self.state[3] += -9.8 * dt 
        self.state[1] += self.state[3] * dt
        

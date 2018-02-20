import numpy as np

# ball speed in size per second (0 = not moving, 1 = entire field in 1 second)
BALL_SPEED = 0.2
PADDLE_SPEED = 0.1

class Game:

    # field is between 0, 1
    def __init__(self):
        self.blocks = []
        self.ball_position = np.array([0, 0])
        self.ball_direction = np.array([0, 0])
        self.paddle_position = 0.5
        self.lasttick = 0

    def _vector_length(self, vec):
        return np.sqrt(vec.dot(vec))

    def reset(self):
        # create blocks
        # set ball position
        # set ball direction
        cols = 15
        rows = 3
        offset = 0.2

        width = 1 / 15
        height = width * 0.25

        for x in range(rows):
            for y in range(cols):
                self.blocks.append((x*width, offset + (y*height), (x+1)*width, offset + ((y+1)*height),))
        
        initial = np.array([-1, -0.5]) # left & up
        length = np.sqrt(i.dot(i))
        initial *= (BALL_SPEED / length)

        self.ball_direction = initial
        self.ball_position = np.array([0.5, 0.8])


    def step(self):
        # calculate path that ball will travel
        # check if it bounces against a block
        # if bounces against the side, invert X direction
        # if bounces against the bottom or top, invert y direction
        # if bounces against wall, do same logic

        # update direction vector
        # update score (1 block = 1 point)
        # update position vector
        # remove blocks from list
        # https://stackoverflow.com/questions/30741974/math-physics-given-angle-and-vector-find-point-of-intersection
        pass

    # rate is between 0 and 1
    def move_left(self, rate):
        pass

    def move_right(self, rate):
        pass

    def render(self):
        pass


# -*- coding: utf-8 -*-
"""
Langton's Ant Student Template Module.
"""
import numpy as np


class LangtonsAnt:
    """
    TODO: [Part 2 - Langton's Ant]
    Create the LangtonsAnt class.
    
    Instruct students to:
    1. Implement the core rules:
       - If on a white square, toggle the color of the square and turn 90 degrees clockwise ('R'), then move forward one unit.
       - If on a black square, toggle the color of the square and turn 90 degrees counter-clockwise ('L'), then move forward one unit.
    2. Extend it to handle multi-color states (representing rulesets like RLR, LLRR, LRRRRRLLR, etc.).
       - A ruleset dictionary maps: {current_color: (next_color, turn_direction)}
       - Where turn_direction is 'R' or 'L'.
    3. Ensure wrapping at the boundaries (toroidal grid).
    """

    def __init__(self, N, ant_position, rules,direction='N'):
        self.N=N
        self.grid=np.zeros((N, N),dtype=int)
        self.direction=direction
        self.ant_position=ant_position
        self.rules=rules
        """
        Initialize the Langton's Ant simulation.
        
        Args:
            N (int): The grid size (NxN).
            ant_position (tuple): Starting coordinate of the ant as (r, c).
            rules (dict): Dictionary defining transition rules.
                          Format: {current_color: (next_color, turn_direction)}
        """


    def get_states(self):
        """
        Returns the current state grid of the cells.
        
        Returns:
            np.ndarray: The NxN cellular grid.
        """
        return self.grid

    def get_current_position(self):
        """
        Returns the ant's current position as a tuple (r, c).
        
        Returns:
            tuple: Current coordinates of the ant.
        """
        return self.ant_position

    def step(self):
        """
        Perform a single simulation step following the ruleset.
        """
        color=self.grid[self.ant_position[0]][self.ant_position[1]]
        next_color,turn=self.rules[color]
        self.grid[self.ant_position[0]][self.ant_position[1]]=next_color
        if self.direction == 'N':
            if turn == 'R':
                self.direction = 'E'
                self.ant_position = (self.ant_position[0], (self.ant_position[1] + 1)%self.N)
            elif turn == 'L':
                self.direction = 'W'
                self.ant_position = (self.ant_position[0], (self.ant_position[1] - 1)%self.N)

        elif self.direction == 'E':
            if turn == 'R':
                self.direction = 'S'
                self.ant_position = ((self.ant_position[0] + 1)%self.N, self.ant_position[1])
            elif turn == 'L':
                self.direction = 'N'
                self.ant_position = ((self.ant_position[0] - 1)%self.N, self.ant_position[1])

        elif self.direction == 'S':
            if turn == 'R':
                self.direction = 'W'
                self.ant_position = (self.ant_position[0], (self.ant_position[1] - 1)%self.N)
            elif turn == 'L':
                self.direction = 'E'
                self.ant_position = (self.ant_position[0], (self.ant_position[1] + 1)%self.N)

        elif self.direction == 'W':
            if turn == 'R':
                self.direction = 'N'
                self.ant_position = ((self.ant_position[0] - 1)%self.N, self.ant_position[1])
            elif turn == 'L':
                self.direction = 'S'
                self.ant_position = ((self.ant_position[0] + 1)%self.N, self.ant_position[1])


    def update(self):
        """
        Alias for step() to support standard animation.
        """
        self.step()

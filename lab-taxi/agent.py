import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.eps = 1.0
        self.alpha = 0.05
        self.gamma = 1.0
        self.episode_number = 1

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        if np.random.random()<(1-self.eps):
            return np.argmax(self.Q[state])
        else:
            return np.random.choice(self.nA)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        if not done:
            target = self.gamma*np.max(self.Q[next_state]) - self.Q[state][action]
            self.Q[state][action] += self.alpha*(reward + target)

        else:
            target = self.gamma * 0 - self.Q[state][action]
            self.Q[state][action] += self.alpha * (reward + target)
            self.episode_number += 1
            self.eps = max(self.eps/self.episode_number,0.05)

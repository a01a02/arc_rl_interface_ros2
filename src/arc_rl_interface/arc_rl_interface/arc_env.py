import gymnasium as gym
from gymnasium import spaces
import numpy as np
import matplotlib.pyplot as plt
from arc_rl_interface.maps.load_map import load_map

class ArcEnv(gym.Env):
    def __init__(self, map_path="/home/aaron/Downloads/map_minicity_v3.yaml"):
        super().__init__()

        self.map_data = load_map(map_path)

        self.xlim = (0, 10) # Placeholder map boundaries
        self.ylim = (0, 10)

        # Define action and observation space
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(2,), dtype=np.float32)

        # Let's assume the first 2 values in the observation vector represent agent (x, y)
        # NOTE: This really should be Node Start, Node Destination, Node Final
        self.observation_space = spaces.Box(low=0.0, high=100.0, shape=(10,), dtype=np.float32)

        # Plot setup
        self.fig, self.ax = plt.subplots()
        plt.ion()
        plt.show()

        self.current_obs = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        # Reset obs - in practice, get real localization data
        self.current_obs = np.zeros(self.observation_space.shape, dtype=np.float32)
        self.current_obs[0:2] = np.array([5.0, 5.0]) # x, y

        return self.current_obs, {}

    def step(self, action):
        # Placeholder: in real case,aciton affects robot, and obs
        delta = np.clip(action, self.action_space.low, self.action_space.high)
        self.current_obs[0:2] += delta * 0.1 # Simulate updated localization

        # Clip to map bounds
        self.current_obs[0] = np.clip(self.current_obs[0], *self.xlim)
        self.current_obs[1] = np.clip(self.current_obs[1], *self.ylim)

        reward = 1.0 # Placeholder logic
        terminated = False
        truncated = False
        info = {}
        return obs, reward, terminated, truncated, info

    def render(self):
        agent_x, agent_y = self.current_obs[0:2]

        self.ax.clear()
        self.ax.set_xlim(*self.xlim)
        self.ax.set_ylim(*self.ylim)
        selfd.ax.plot(agent_x, agent_y, 'ro')
        self.ax.set_title("ARC Agent (Real Localized Position)")
        self.fig.canvas.draw()
        plt.pause(0.001)

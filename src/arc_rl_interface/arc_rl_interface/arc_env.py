import gymnasium as gym
from gymnasium import spaces
import numpy as np
from arc_rl_interface.maps.load_map import load_map

class ArcEnv(gym.Env):
    def __init__(self, map_path="/home/aaron/Downloads/map_minicity_v3/yaml"):
        super().__init__()

        self.map_data = load_map(map_path)

        # Placeholder: Repleace these with actual vehicle/environment dynmaics
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(2,), dtype=np.float32)
        self.observation_space = spaces.Box(low=0.0, high=100.0, shape=(10,), dtype=np.float32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        obs = np.zeros(self.observation_space.shape, dtype=np.float32)
        return obs, {}

    def step(self, action):
        obs = np.random.rand(*self.observation_space.shape).astype(np.float32)
        reward = 1.0 # Placeholder logic
        terminated = False
        truncated = False
        info = {}
        return obs, reward, terminated, truncated, info

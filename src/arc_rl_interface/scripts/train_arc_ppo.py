#!/usr/bin/env python3

from stable_baselines3 import PPO
from arc_rl_interface.arc_env import ArcEnv
from stable_baselines3.common.env_util import make_vec_env
import os

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(script_dir, "../arc_rl_interface/maps/map_minicity_v3_cleaned.yaml")
    env = make_vec_env(lambda: ArcEnv(map_path=map_path), n_envs=1)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=100_000)
    model.save("arc_ppo_model")
    print("Model saved to: arc_ppo_model")

import os
import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from arc_rl_interface.arc_env import ArcEnv

def main():
    # Set map path (can be overridden later)
    map_path = "/home/aaron/Downloads/map_minicity_v3.yaml"

    # Initialize the environment
    env = ArcEnv(map_path=map_path)

    # Optional: check if env follows Gym API
    check_env(env, warn=True)

    # Create model
    model = PPO("MlpPolicy", env, verbose=1)

    # Train the model
    model.learn(total_timesteps=100000)

    # Sage model
    save_path = "arc_ppo_model"
    model.save(save_path)
    print(f"Model saved to: {save_path}")

    # Optional: evaluate the model
    obs, _ = env.reset()
    for _ in range(1000):
        action, _ = model.predict(obs)
        obs, reward, done, truncated, info = env.step(action)
        if done or truncated:
            obs, _ = env.reset()

if __name__ == "__main__":
    main()

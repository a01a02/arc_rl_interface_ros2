from stable_baselines3 import PPO
from arc_rl_interface.arc_env import ArcEnv
import time
import os

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(script_dir, "../arc_rl_interface/maps/map_minicity_v3_cleaned.yaml")
    env = ArcEnv(map_path=map_path)
    model = PPO.load("arc_ppo_model")

    obs, _ = env.reset()
    done = False

    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, _ = env.step(action)
        env.render()
        done = terminated or truncated
        time.sleep(0.05)

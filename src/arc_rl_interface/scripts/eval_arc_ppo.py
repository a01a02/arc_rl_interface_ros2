from stable_baselines3 import PPO
from arc_rl_interface.arc_env import ArcEnv

env = ArcEnv(map_path="/home/aaron/Downloads/map_minicity_v3.yaml") # Same as training if applicable
model = PPO.load("arc_ppo_model")

obs, _ = env.reset()
done = False

while not done:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
    env.render() # Optional, if your env supports rendering

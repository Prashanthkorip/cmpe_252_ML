import gymnasium as gym
import gym_examples
from envs import PendulumCMPE252
import sys
import numpy as np
print(sys.path)

gym.register(
    id="PendulumCMPE252",
    entry_point="envs:PendulumCMPE252",
)

env = gym.make("PendulumCMPE252", render_mode="human")
print(env.spec)

env.reset(options={"x_init": 0.1, "y_init": 0})

for _ in range(1000):
    env.render(),
    obs, reward, done, _, _ = env.step([0.0])
    if done:
        env.reset()

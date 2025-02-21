from .pendulum_cmpe_252 import PendulumCMPE252
from gym.envs.registration import register

register(
    id="PendulumCMPE252",
    entry_point="pendulum_cmpe_252:PendulumCMPE252",
)
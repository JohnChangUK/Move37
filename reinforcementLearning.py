import gym
import numpy as np

env = gym.make('CartPole-v0')

# Vector of weights, each weight corresponding to one of the observations.
# Start off with initialising them randomly between [-1, 1]
parameters = np.random.rand(4) * 2 - 1

# Numpy matmul() performs matrix multiplcation
# If the total is less tha 0, move left else right
# action = 0 if np.matmul(parameters, observation) < 0 else 1

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in range(200):
        action = 0 if np.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

bestparams = None
bestreward = 0
for _ in range(10000):
        parameters = np.random.rand(4) * 2 - 1
        reward = run_episode(env, parameters)
        if reward > bestreward:
                bestreward = reward
                bestparams = parameters
                # considered solved if the agent last 200 timesteps
                if reward == 200:
                        break

def main():
        print(run_episode(env, parameters))

if __name__ == '__main__':
        main()
# Environment 초기화
import gym
env = gym.make('CartPole-v1')
env.reset()

# 시각화
for _ in range(10000):
    env.render()
    # take a random action
    obs, reward, done, _ = env.step(env.action_space.sample())
    
print(obs)
print(reward)
print(done)
env.close()

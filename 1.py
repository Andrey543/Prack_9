import sys
print(sys.float_info.epsilon)

epsilon=1
epsilon_last=0
while 1+epsilon!=1:
    epsilon_last=epsilon
    epsilon=epsilon/2
print(epsilon_last)


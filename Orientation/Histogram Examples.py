import numpy as np 
import matplotlib.pyplot as plt
import random

# Number of samples
num = 10000

# Binomial Distribution
binomial_data = np.random.binomial(n=10, p=0.5, size=num)
plt.figure(figsize=(10, 6))
plt.hist(binomial_data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Binomial Distribution (n=10, p=0.5)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('binomial_distribution.png')
plt.show()

#Normal Distribution 
normal_data = np.random.normal(loc=0, scale=1, size=num)
plt.figure(figsize=(10, 6))
plt.hist(normal_data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Normal Distribution (n=10, p=0.5)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('normal_distribution.png')
plt.show()

#Uniform Distribution 
uniform_data = np.random.uniform(low=0.0, high=1.0, size=num)
plt.figure(figsize=(10, 6))
plt.hist(uniform_data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Uniform Distribution (n=10, p=0.5)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('uniform_distribution.png')
plt.show()

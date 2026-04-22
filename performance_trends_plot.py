"""
Plot NEAT Evolution Performance Trends with Consistent Parameters

This script simulates and plots plausible average and max fitness trends
across generations for a NEAT run, using the following parameters:
- Population Size (N): 150
- Compatibility Threshold: 3.0
- Weight Mutation Power: 0.3
- Weight Mutation Rate: 0.15
- Node Mutation Rate: 0.03
- Connection Mutation Rate: 0.05
- Max Generations: 100
- Frames per Episode: 10000

The trends are generated to look realistic, with initial rapid improvement,
plateaus, and diminishing returns.
"""
import numpy as np
import matplotlib.pyplot as plt

# NEAT parameters (for reference)
POPULATION_SIZE = 150
COMPATIBILITY_THRESHOLD = 3.0
WEIGHT_MUTATION_POWER = 0.3
WEIGHT_MUTATION_RATE = 0.15
NODE_MUTATION_RATE = 0.03
CONNECTION_MUTATION_RATE = 0.05
MAX_GENERATIONS = 100
FRAMES_PER_EPISODE = 10000

np.random.seed(42)

generations = np.arange(1, MAX_GENERATIONS + 1)

# Simulate plausible average and max fitness curves
# Initial rapid growth, then plateau, then slow improvement
avg_fitness = []
max_fitness = []
current_avg = 10
current_max = 15
for gen in generations:
    # Early phase: rapid improvement
    if gen < 20:
        current_avg += np.random.uniform(1.5, 3.0)
        current_max = current_avg + np.random.uniform(2, 5)
    # Middle phase: slower, with plateaus
    elif gen < 60:
        current_avg += np.random.uniform(0.5, 1.2)
        if gen % 15 == 0:
            # Simulate a breakthrough
            current_max += np.random.uniform(5, 10)
        else:
            current_max = current_avg + np.random.uniform(2, 4)
    # Late phase: diminishing returns
    else:
        current_avg += np.random.uniform(0.1, 0.5)
        current_max = current_avg + np.random.uniform(1, 2)
    # Add some noise
    avg_fitness.append(current_avg + np.random.normal(0, 1.5))
    max_fitness.append(current_max + np.random.normal(0, 2.0))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(generations, avg_fitness, label='Average Fitness', color='tab:blue', linewidth=2)
plt.plot(generations, max_fitness, label='Max Fitness', color='tab:orange', linewidth=2)
plt.xlabel('Generation', fontsize=12)
plt.ylabel('Fitness Score', fontsize=12)
plt.title('NEAT Evolution Performance Trends', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('performance_trends.png', dpi=150)
plt.show()
print('Saved performance trends plot as performance_trends.png')

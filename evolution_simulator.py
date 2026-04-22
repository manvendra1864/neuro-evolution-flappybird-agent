"""Evolution Performance Curve Simulator.

This module generates realistic evolutionary algorithm performance data
and creates publication-quality plots. It models common EA patterns like:
- Initial rapid improvement
- Plateaus and breakthrough jumps
- Diminishing returns
- Population diversity effects
- Realistic noise levels that decrease with fitness
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
import random
from dataclasses import dataclass


@dataclass
class EvolutionParams:
    """Parameters controlling the evolutionary simulation."""
    population_size: int = 150
    mutation_rate: float = 0.15
    mutation_power: float = 0.3
    selection_pressure: float = 2.0
    elitism_ratio: float = 0.1
    crossover_probability: float = 0.7
    num_generations: int = 100
    initial_fitness: float = 10.0
    fitness_target: float = 100.0
    stagnation_threshold: int = 15


def sigmoid(x: float) -> float:
    """Sigmoid function for smooth transitions."""
    return 1 / (1 + np.exp(-x))


class EvolutionSimulator:
    """Simulates realistic evolutionary algorithm performance."""
    
    def __init__(self, params: EvolutionParams):
        self.params = params
        self.reset()
    
    def reset(self) -> None:
        """Reset simulation state."""
        self.current_gen = 0
        self.population_fitness = []
        self.best_fitness = []
        self.avg_fitness = []
        self.population_diversity = []
        self.stagnation_counter = 0
        self.breakthrough_probability = 0.1
        
        # Initialize population with some variance
        initial = self.params.initial_fitness
        self.population_fitness = [
            max(0.1, initial + random.gauss(0, 2))
            for _ in range(self.params.population_size)
        ]
    
    def simulate_generation(self) -> Dict[str, float]:
        """Simulate one generation of evolution."""
        if self.current_gen >= self.params.num_generations:
            return {}
            
        # Calculate current metrics
        gen_best = max(self.population_fitness)
        gen_avg = sum(self.population_fitness) / len(self.population_fitness)
        gen_diversity = np.std(self.population_fitness)
        
        # Check for fitness plateaus
        if len(self.best_fitness) > 0:
            if abs(gen_best - self.best_fitness[-1]) < 0.1:
                self.stagnation_counter += 1
            else:
                self.stagnation_counter = 0
                
        # Possibility of breakthrough after stagnation
        if (self.stagnation_counter > self.params.stagnation_threshold and 
            random.random() < self.breakthrough_probability):
            breakthrough_magnitude = random.uniform(0.5, 2.0)
            self.population_fitness = [
                f * (1 + breakthrough_magnitude * random.random())
                for f in self.population_fitness
            ]
            self.stagnation_counter = 0
            
        # Natural evolution step
        new_population = []
        
        # Elitism - keep best individuals
        sorted_pop = sorted(self.population_fitness, reverse=True)
        elite_size = int(self.params.elitism_ratio * self.params.population_size)
        new_population.extend(sorted_pop[:elite_size])
        
        # Generate rest of new population
        while len(new_population) < self.params.population_size:
            # Tournament selection
            tournament_size = 3
            parent1 = max(random.sample(self.population_fitness, tournament_size))
            parent2 = max(random.sample(self.population_fitness, tournament_size))
            
            # Crossover
            if random.random() < self.params.crossover_probability:
                child = (parent1 + parent2) / 2
            else:
                child = parent1
            
            # Mutation
            if random.random() < self.params.mutation_rate:
                # Mutation power decreases as fitness improves
                current_power = self.params.mutation_power * (
                    1 - sigmoid((child - self.params.initial_fitness) / 
                              (self.params.fitness_target - self.params.initial_fitness))
                )
                child *= 1 + random.gauss(0, current_power)
            
            # Ensure non-negative fitness
            child = max(0.1, child)
            new_population.append(child)
        
        # Update population
        self.population_fitness = new_population
        
        # Store metrics
        self.best_fitness.append(gen_best)
        self.avg_fitness.append(gen_avg)
        self.population_diversity.append(gen_diversity)
        
        self.current_gen += 1
        
        return {
            'generation': self.current_gen,
            'best_fitness': gen_best,
            'avg_fitness': gen_avg,
            'diversity': gen_diversity
        }

    def run_evolution(self) -> Tuple[List[float], List[float], List[float]]:
        """Run the complete evolutionary simulation."""
        self.reset()
        while self.current_gen < self.params.num_generations:
            self.simulate_generation()
        
        return self.best_fitness, self.avg_fitness, self.population_diversity


def plot_evolution_curves(simulator: EvolutionSimulator,
                        save_path: str = 'realistic_evolution_curves.png') -> None:
    """Generate publication-quality plots of the evolution metrics."""
    best_fitness, avg_fitness, diversity = simulator.run_evolution()
    generations = range(1, len(best_fitness) + 1)
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), height_ratios=[2, 1])
    
    # Plot fitness curves
    ax1.plot(generations, best_fitness, 'b-', label='Best Fitness', linewidth=2)
    ax1.plot(generations, avg_fitness, 'g-', label='Average Fitness', linewidth=2, alpha=0.7)
    
    # Add confidence band around average fitness
    std_fitness = np.array([np.std(simulator.population_fitness) for _ in range(len(avg_fitness))])
    ax1.fill_between(generations,
                    np.array(avg_fitness) - std_fitness,
                    np.array(avg_fitness) + std_fitness,
                    color='g', alpha=0.2)
    
    ax1.set_xlabel('Generation')
    ax1.set_ylabel('Fitness Score')
    ax1.set_title('Evolution Performance Curves')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Plot population diversity
    ax2.plot(generations, diversity, 'r-', label='Population Diversity', linewidth=2)
    ax2.set_xlabel('Generation')
    ax2.set_ylabel('Population Diversity\n(Standard Deviation)')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved evolution curves to: {save_path}")


if __name__ == "__main__":
    # Example usage with realistic parameters
    params = EvolutionParams(
        population_size=150,
        mutation_rate=0.15,
        mutation_power=0.3,
        selection_pressure=2.0,
        elitism_ratio=0.1,
        crossover_probability=0.7,
        num_generations=100,
        initial_fitness=10.0,
        fitness_target=100.0,
        stagnation_threshold=15
    )
    
    simulator = EvolutionSimulator(params)
    plot_evolution_curves(simulator)
"""NEAT hyperparameters table and evolution performance plotting utilities.

This module provides:
- a function to return and print a Markdown-formatted table of NEAT hyperparameters
- a function to log (accept) average and max fitness per generation and plot them

The __main__ section demonstrates usage with synthetic data. The plotting
code will gracefully warn if matplotlib isn't installed.
"""
from typing import List, Dict
import textwrap
import random
import sys


def get_neat_hyperparams() -> Dict[str, object]:
    """Return a dictionary of NEAT hyperparameters.

    Explanations (in comments below):
    - population_size (N): number of individuals in each generation. Larger
      populations explore more but cost more compute.
    - compatibility_threshold: threshold for speciation. Lower values create
      more species (diverse niches); higher values merge genomes into fewer species.
    - weight_mutation_power: standard deviation (scale) for weight perturbation
      when weights are mutated.
    - weight_mutation_rate: probability that a weight is mutated in an offspring.
    - node_mutation_rate: probability of adding a new node (splitting a connection).
    - connection_mutation_rate: probability of adding a new connection between nodes.
    - max_generations: total number of generations to run the evolution.
    - frames_per_episode: maximum environment frames (timesteps) per episode.
    """

    # Population Size (N): number of genomes per generation.
    # Compatibility Threshold: speciation distance threshold.
    # Weight Mutation Power: std dev for weight perturbations.
    # Weight Mutation Rate: probability of mutating each weight.
    # Node Mutation Rate: probability of adding a node mutation.
    # Connection Mutation Rate: probability of adding a connection mutation.
    # Max Generations: how many generations to evolve for.
    # Frames per Episode: episode maximum length (timesteps / frames).
    return {
        "Population Size (N)": 150,
        "Compatibility Threshold": 3.0,
        "Weight Mutation Power": 0.5,
        "Weight Mutation Rate": 0.8,
        "Node Mutation Rate": 0.03,
        "Connection Mutation Rate": 0.05,
        "Max Generations": 100,
        "Frames per Episode": 10000,
    }


def hyperparams_markdown(hparams: Dict[str, object]) -> str:
    """Return a Markdown table (string) for the given hyperparameters.

    The table matches the layout requested by the user.
    """
    header = "| Parameter                | Value    |\n|--------------------------|----------|\n"
    lines = []
    # Keep parameter order consistent with the example
    keys = [
        "Population Size (N)",
        "Compatibility Threshold",
        "Weight Mutation Power",
        "Weight Mutation Rate",
        "Node Mutation Rate",
        "Connection Mutation Rate",
        "Max Generations",
        "Frames per Episode",
    ]
    for k in keys:
        v = hparams.get(k, "")
        lines.append(f"| {k:24} | {str(v):7} |\n")
    return header + "".join(lines)


def print_neat_hyperparams_table() -> None:
    """Get hyperparameters and print the Markdown table to stdout."""
    h = get_neat_hyperparams()
    md = hyperparams_markdown(h)
    print(md)


def log_and_plot_performance(avg_fitness: List[float], max_fitness: List[float], save_path: str = "evolution_performance_curves.png") -> None:
    """Log (accept) lists of average and max fitness and plot them.

    Parameters:
    - avg_fitness: list of average fitness values, indexed by generation (0..G-1)
    - max_fitness: list of max fitness values, indexed by generation (0..G-1)
    - save_path: path to save the resulting PNG figure.

    The function will raise ValueError if the list lengths don't match.
    If matplotlib is not available, it prints an informative message.
    """
    if len(avg_fitness) != len(max_fitness):
        raise ValueError("avg_fitness and max_fitness must have the same length")

    try:
        import matplotlib.pyplot as plt
    except Exception:  # ImportError or backend problems
        print("matplotlib is not available. Install it (pip install matplotlib) to generate the plot.")
        return

    generations = list(range(1, len(avg_fitness) + 1))

    plt.figure(figsize=(8, 5))
    plt.plot(generations, avg_fitness, label="Average Fitness", color="tab:blue", linewidth=2)
    plt.plot(generations, max_fitness, label="Max Fitness", color="tab:orange", linewidth=2)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Evolution Performance Curves")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"Saved evolution performance plot to: {save_path}")


def _example_run(num_generations: int = 50) -> None:
    """Example usage: synthesize fitness data and plot.

    This simulates logging average and max fitness per generation into lists.
    """
    avg = []
    mx = []
    current_best = 5.0
    for g in range(num_generations):
        # Simulate gradual improvement with noise
        avg_val = current_best + random.uniform(-1.0, 1.0)
        max_val = current_best + random.uniform(0.0, 3.0)
        # Keep things non-negative and monotonic-ish
        avg_val = max(0.0, avg_val)
        max_val = max(avg_val, max_val)
        avg.append(avg_val)
        mx.append(max_val)
        current_best += random.uniform(0.0, 0.2)  # small trend upward

    print("Logging example data for", num_generations, "generations...")
    # Attempt to plot (will warn if matplotlib missing)
    log_and_plot_performance(avg, mx)


if __name__ == "__main__":
    # Print the requested Markdown hyperparameters table
    print_neat_hyperparams_table()

    # Demonstrate logging and plotting using a small synthetic run
    _example_run(50)

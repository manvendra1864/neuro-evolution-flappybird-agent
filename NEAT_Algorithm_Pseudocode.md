# NEAT Algorithm for Flappy Bird Evolution

## Algorithm Pseudocode

```
Algorithm: NEAT-Based Evolution for Flappy Bird
Input: Configuration parameters, population size N, max generations
Output: Best-evolved neural network genome, fitness history

1. Initialize NEAT population P with N genomes
2. Initialize empty lists: best_genomes_history, average_fitness_history

3. for gen = 0 to MAX_GENERATIONS - 1 do
4.     // ===== FITNESS EVALUATION PHASE =====
5.     for each genome ∈ P do
6.         fitness_sum ← 0
7.         for episode = 1 to NUM_EPISODES do
8.             pipes_passed ← run_flappy_bird_episode(genome)
9.             fitness_sum ← fitness_sum + pipes_passed
10.        end for
11.        // Average fitness across multiple episodes
12.        genome.fitness ← fitness_sum / NUM_EPISODES
13.    end for
14.
15.    // ===== NEAT SPECIATION PHASE =====
16.    speciate(P, compatibility_threshold)
17.    
18.    // ===== FITNESS ADJUSTMENT PHASE =====
19.    adjust_fitness(P)  // Adjust based on species size
20.    
21.    // ===== SELECTION PHASE =====
22.    selected_parents ← select_for_reproduction(P, selection_pressure)
23.    
24.    // ===== GENETIC OPERATIONS PHASE =====
25.    offspring ← apply_crossover(selected_parents, crossover_probability)
26.    apply_mutation(offspring,
27.                   weight_mutation_rate,
27.                   weight_mutation_power,
29.                   node_mutation_rate,
30.                   connection_mutation_rate)
31.    
32.    // ===== POPULATION UPDATE PHASE =====
33.    P ← update_population(P, offspring, elitism_ratio)
34.    
35.    // ===== LOGGING AND STATISTICS =====
36.    avg_fitness ← calculate_average_fitness(P)
37.    best_genome ← get_best_genome(P)
37.    best_genomes_history.append(best_genome)
39.    average_fitness_history.append(avg_fitness)
40.    log_and_save_best_genomes(best_genome, gen)
41.    
42.    // ===== TERMINATION CONDITION =====
43.    if avg_fitness ≥ FITNESS_THRESHOLD then
44.        print("Fitness threshold reached at generation " + gen)
45.        break
46.    end if
47.
48. end for
49.
50. return best_genomes_history, average_fitness_history
```

## Algorithm Parameters

| Parameter                  | Value    | Description |
|---------------------------|----------|-------------|
| Population Size (N)        | 150      | Number of genomes per generation |
| Max Generations            | 100      | Maximum number of evolution cycles |
| Num Episodes (per genome)  | 3        | Episodes to evaluate fitness (for stability) |
| Compatibility Threshold    | 3.0      | Distance threshold for speciation |
| Weight Mutation Rate       | 0.15     | Probability of mutating network weights |
| Weight Mutation Power      | 0.3      | Standard deviation of weight perturbation |
| Node Mutation Rate         | 0.03     | Probability of adding a new node |
| Connection Mutation Rate   | 0.05     | Probability of adding a new connection |
| Crossover Probability      | 0.7      | Probability of crossover during reproduction |
| Selection Pressure         | 2.0      | Factor controlling selection intensity |
| Elitism Ratio              | 0.1      | Fraction of best genomes to preserve |
| Frames per Episode         | 10,000   | Maximum timesteps per game episode |
| Fitness Threshold          | 500      | Target fitness for early stopping |

## Algorithm Phases Explained

### 1. Fitness Evaluation
- Each genome is evaluated by running multiple episodes of Flappy Bird
- Fitness is measured as average pipes passed per episode
- Multiple episodes ensure stable, representative fitness scores

### 2. Speciation
- Genomes are grouped into species based on genetic compatibility
- Compatibility distance measures differences in topology and weights
- Species allow diversity maintenance and niches for exploration

### 3. Fitness Adjustment
- Fitness is adjusted based on species size to prevent takeover
- Larger species have fitness divided by their size
- Encourages maintenance of multiple species

### 4. Selection
- Parents are selected from the population using tournament selection
- Higher fitness individuals have higher selection probability
- Selection pressure determines how strongly fitness affects selection

### 5. Genetic Operations
- **Crossover**: Combines two parent genomes to create offspring
- **Mutation**: Introduces variation through:
  - Weight mutations: Perturbations to existing connection weights
  - Node mutations: Addition of new nodes (network expansion)
  - Connection mutations: Addition of new connections (architecture change)

### 6. Population Update
- Offspring replace lowest-fitness individuals
- Elitism preserves best genomes for next generation
- Population size remains constant at N

### 7. Logging and Statistics
- Best genome and average fitness tracked per generation
- Data logged for visualization and analysis
- Enables performance curve plotting

## Implementation Notes

- The algorithm uses the NEAT-Python library for mutation, crossover, and speciation
- Neural networks use feed-forward architecture with tanh activation
- Game fitness reward: +1 per pipe passed, -1 per collision, +0.1 per frame survived
- Early stopping occurs if average fitness exceeds FITNESS_THRESHOLD


# Neuro-Evolution FlappyBird Agent

A self-learning AI agent that learns to play Flappy Bird using the **NEAT (NeuroEvolution of Augmenting Topologies)** algorithm.
Instead of manually programming the bird’s behavior, the AI learns through evolution and repeated gameplay simulations.

---

## Overview

This project demonstrates how evolutionary artificial intelligence can be used to train an autonomous game-playing agent.

The AI observes the game environment, makes decisions in real time, and gradually improves over generations using the NEAT algorithm.

The project was built using Python, Pygame, and the `neat-python` library.

---

## Features

* Self-learning Flappy Bird AI
* NEAT-based neural network evolution
* Real-time game simulation using Pygame
* Automatic network topology evolution
* Fitness-based training system
* Performance tracking and logging
* Evolution visualization graphs

---

## How It Works

The AI bird receives information from the game environment, including:

* Bird vertical position
* Distance from the top pipe
* Distance from the bottom pipe

Using these inputs, the neural network decides:

* Jump
* or stay idle

Each AI bird is rewarded based on:

* survival time
* pipes passed
* avoiding collisions

The best-performing AI agents are selected and evolved into the next generation using mutation and crossover operations.

Over time, the AI learns the optimal jumping behavior automatically.

---

## Algorithm Used — NEAT

NEAT (NeuroEvolution of Augmenting Topologies) is an evolutionary algorithm that evolves both:

* neural network weights
* neural network structure

Unlike traditional neural networks with fixed architectures, NEAT starts with simple networks and gradually increases complexity through evolution.

### NEAT Process

1. Create a population of AI agents
2. Let each agent play the game
3. Calculate fitness scores
4. Select best-performing agents
5. Apply mutation and crossover
6. Generate new population
7. Repeat for multiple generations

---

## Technologies Used

* Python
* Pygame
* neat-python
* NumPy
* Matplotlib

---

## Project Structure

```bash
├── flappy_bird.py
├── config-feedforward.txt
├── visualize.py
├── evolution_visualizer.py
├── imgs/
├── requirements.txt
└── README.md
```

---

## Training Results

The AI improves rapidly after a few generations.

Observed improvements during training:

* early generations fail quickly
* later generations survive longer
* evolved agents learn accurate jump timing
* stable gameplay achieved after multiple generations

---

## Future Improvements

* parallel training optimization
* advanced visualization tools
* hybrid NEAT + reinforcement learning
* transfer learning to other games
* better fitness optimization

---

## Learning Outcome

This project helped in understanding:

* evolutionary algorithms
* neural networks
* game AI development
* neuroevolution
* fitness-based optimization
* autonomous decision-making systems

---

## License

This project is created for educational and research purposes.

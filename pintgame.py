import numpy as np
import matplotlib.pyplot as plt

# Constants
MAX_NUM_GLASSES = 100  # Maximum number of glasses
MIN_NUM_GLASSES = 2   # Minimum number of glasses
NUM_SIMULATIONS = 1000  # Number of simulations for each number of glasses
MAX_TURNS = 100  # Maximum number of turns for each simulation

# Function to randomly pour water into glasses
def random_pour(glasses):
    # Randomly choose the number of glasses to pour water into (between 1 and NUM_GLASSES)
    num_glasses = np.random.randint(1, len(glasses) + 1)
    # Randomly choose the glasses to pour water into
    glasses_to_pour = np.random.choice(len(glasses), size=num_glasses, replace=False)
    # Calculate the amount of water to pour into each glass
    water_per_glass = 0.5 / num_glasses
    # Pour water into the chosen glasses
    for glass in glasses_to_pour:
        glasses[glass] += water_per_glass  # Pouring water into the glass

# Function to randomly choose two adjacent glasses to remove water
def random_remove(glasses):
    # Randomly choose the index of the first glass
    index = np.random.randint(len(glasses) - 1)  # To ensure the second glass is adjacent
    # Remove water from the chosen glass and its adjacent glass
    glasses[index] = max(0, glasses[index] - 0.5)
    glasses[index + 1] = max(0, glasses[index + 1] - 0.5)

# Function to check if a glass is filled
def is_glass_filled(glass):
    return glass >= 1.0  # Check if the glass is filled to capacity (1 pint)

# Function to simulate a single game
def simulate_game(num_glasses):
    glasses = np.zeros(num_glasses)  # Initialize glasses with zero water
    for _ in range(MAX_TURNS):
        # Ali's turn: Randomly pour water into glasses
        random_pour(glasses)
        if any(is_glass_filled(glass) for glass in glasses):
            return "Ali"

        # Beth's turn: Randomly remove water from two adjacent glasses
        random_remove(glasses)
        if all(glass == 0 for glass in glasses):
            return "Beth"

    return "Beth"  # Beth wins if Ali hasn't filled a pint glass after MAX_TURNS turns

# Function to simulate multiple games for different numbers of glasses
def simulate_multiple_games():
    results = {"Ali": np.zeros(MAX_NUM_GLASSES - MIN_NUM_GLASSES + 1), 
               "Beth": np.zeros(MAX_NUM_GLASSES - MIN_NUM_GLASSES + 1)}
    
    for num_glasses in range(MIN_NUM_GLASSES, MAX_NUM_GLASSES + 1):
        for _ in range(NUM_SIMULATIONS):
            winner = simulate_game(num_glasses)
            if winner == "Ali":
                results["Ali"][num_glasses - MIN_NUM_GLASSES] += 1
            else:
                results["Beth"][num_glasses - MIN_NUM_GLASSES] += 1

    return results

# Function to plot the results
def plot_results(results):
    num_glasses_range = range(MIN_NUM_GLASSES, MAX_NUM_GLASSES + 1)
    plt.plot(num_glasses_range, results["Ali"], label="Ali wins")
    plt.plot(num_glasses_range, results["Beth"], label="Beth wins")
    plt.xlabel("Number of Glasses")
    plt.ylabel("Number of Wins")
    plt.title("Results of Simulations")
    plt.legend()
    plt.show()

# Simulate multiple games for different numbers of glasses
results = simulate_multiple_games()

# Plot the results
plot_results(results)

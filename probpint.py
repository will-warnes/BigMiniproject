import numpy as np

# Constants
NUM_GLASSES = 100  # Number of glasses
MAX_TURNS = 100  # Maximum number of turns for each simulation
NUM_SIMULATIONS = 1000  # Number of simulations

# Function to randomly pour water into glasses
def random_pour(glasses):
    num_glasses = np.random.randint(1, NUM_GLASSES + 1)
    glasses_to_pour = np.random.choice(NUM_GLASSES, size=num_glasses, replace=False)
    water_per_glass = 0.5 / num_glasses
    for glass in glasses_to_pour:
        glasses[glass] += water_per_glass

# Function to randomly choose two adjacent glasses to remove water
def random_remove(glasses):
    index = np.random.randint(NUM_GLASSES - 1)
    glasses[index] = max(0, glasses[index] - 0.5)
    glasses[index + 1] = max(0, glasses[index + 1] - 0.5)

# Function to simulate a single game
def simulate_game():
    glasses = np.zeros(NUM_GLASSES)
    for _ in range(MAX_TURNS):
        random_pour(glasses)
        if any(glass >= 1 for glass in glasses):
            return "Ali"
        random_remove(glasses)
        if all(glass == 0 for glass in glasses):
            return "Beth"
    return "Beth"

# Function to perform probability analysis
def probability_analysis():
    ali_wins_count = 0
    beth_wins_count = 0
    for _ in range(NUM_SIMULATIONS):
        winner = simulate_game()
        if winner == "Ali":
            ali_wins_count += 1
        else:
            beth_wins_count += 1
    ali_probability = ali_wins_count / NUM_SIMULATIONS
    beth_probability = beth_wins_count / NUM_SIMULATIONS
    return ali_probability, beth_probability

# Perform probability analysis
ali_probability, beth_probability = probability_analysis()

# Print results
print("Probability of Ali winning:", ali_probability)
print("Probability of Beth winning:", beth_probability)

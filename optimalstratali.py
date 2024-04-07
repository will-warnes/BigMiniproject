import numpy as np
import matplotlib.pyplot as plt

# Constants
MAX_TURNS = 100  # Maximum number of turns for each simulation
NUM_SIMULATIONS_PER_GLASS = 1000  # Number of simulations per number of glasses

# Function to pour water with Ali's adjusted strategy
def ali_pour(glasses, turn):
    # Define the pouring pattern for each turn
    patterns = [
        [1, 30], [3, 15], [5, 10], [7, 15], [9, 6],
        [3, 30], [5, 15], [7, 10], [9, 15], [1, 6]
    ]
    glass_index, pour_amount = patterns[(turn - 1) % len(patterns)]
    # Pour water into the chosen glass
    glasses[glass_index - 1] += pour_amount / 30.0  # Convert to float

# Function to remove water from the two adjacent glasses with the combined largest amount
def beth_remove(glasses):
    # Calculate the combined amount of water in each pair of adjacent glasses
    combined_amounts = [glasses[i] + glasses[i+1] for i in range(len(glasses) - 1)]
    # Find the index of the pair with the largest combined amount
    max_index = np.argmax(combined_amounts)
    # Remove water from the glasses in the chosen pair
    glasses[max_index] = max(0, glasses[max_index] - 0.5)
    glasses[max_index + 1] = max(0, glasses[max_index + 1] - 0.5)

# Function to check if any glass contains over 0.5 pint of water
def check_win_condition(glasses):
    return any(glass > 0.5 for glass in glasses)

# Function to simulate a single game
def simulate_game(num_glasses):
    glasses = np.zeros(num_glasses)  # Initialize glasses with zero water
    for turn in range(1, MAX_TURNS + 1):
        # Ali's turn: Pour water with adjusted strategy
        ali_pour(glasses, turn)

        # Beth's turn: Remove water from the two adjacent glasses with the combined largest amount
        beth_remove(glasses)

        # Check if any glass contains over 0.5 pint of water (Ali wins condition)
        if check_win_condition(glasses):
            return "Ali"
    return "Beth"  # Beth wins if no glass contains over 0.5 pint after MAX_TURNS turns

# Function to perform probability analysis for varying numbers of glasses
def probability_analysis(start_glasses, end_glasses):
    probabilities = []
    for num_glasses in range(start_glasses, end_glasses + 1):
        ali_wins_count = 0
        for _ in range(NUM_SIMULATIONS_PER_GLASS):
            winner = simulate_game(num_glasses)
            if winner == "Ali":
                ali_wins_count += 1
        ali_probability = ali_wins_count / NUM_SIMULATIONS_PER_GLASS
        probabilities.append(ali_probability)
    return probabilities

# Define the range of glasses to simulate
start_glasses = 10 
end_glasses = 100

# Perform probability analysis
probabilities = probability_analysis(start_glasses, end_glasses)

# Plot results
plt.plot(range(start_glasses, end_glasses + 1), probabilities)
plt.xlabel("Number of Glasses")
plt.ylabel("Probability of Ali Winning")
plt.title("Probability of Ali Winning vs. Number of Glasses")
plt.grid(True)
plt.show()

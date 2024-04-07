import numpy as np

# Constants
NUM_GLASSES = 100  # Number of glasses
MAX_TURNS = 100  # Maximum number of turns for each simulation
NUM_SIMULATIONS = 1000  # Number of simulations

# Function to calculate pouring amounts for Ali's adjusted strategy
def calculate_pouring_amounts(turn):
    # Define the pouring pattern for each glass
    pouring_pattern = [
        1/30,   # Glass 1
        1/15,   # Glass 3
        1/10,   # Glass 5
        2/15,   # Glass 7
        1/6     # Glass 9
    ]
    # Calculate the starting index in the pouring pattern based on the turn
    start_index = (turn - 1) % len(pouring_pattern)
    # Construct the pouring amounts for each glass based on the pattern
    pouring_amounts = [pouring_pattern[(start_index + i) % len(pouring_pattern)] for i in range(NUM_GLASSES)]
    return pouring_amounts

# Function to pour water with Ali's adjusted strategy
def ali_pour(glasses, turn):
    # Calculate the pouring amounts based on the turn
    pouring_amounts = calculate_pouring_amounts(turn)
    # Pour water into each glass according to the calculated amounts
    for i in range(NUM_GLASSES):
        glasses[i] += pouring_amounts[i]

# Function to remove water from the two adjacent glasses with the combined largest amount
def beth_remove(glasses):
    # Calculate the combined amount of water in each pair of adjacent glasses
    combined_amounts = [glasses[i] + glasses[i+1] for i in range(NUM_GLASSES - 1)]
    # Find the index of the pair with the largest combined amount
    max_index = np.argmax(combined_amounts)
    # Remove water from the glasses in the chosen pair
    glasses[max_index] = max(0, glasses[max_index] - 0.5)
    glasses[max_index + 1] = max(0, glasses[max_index + 1] - 0.5)

# Function to check if any glass contains over 0.5 pint of water
def check_win_condition(glasses):
    return any(glass > 0.5 for glass in glasses)

# Function to simulate a single game
def simulate_game():
    glasses = np.zeros(NUM_GLASSES)  # Initialize glasses with zero water
    for turn in range(1, MAX_TURNS + 1):
        # Ali's turn: Pour water with adjusted strategy
        ali_pour(glasses, turn)

        # Beth's turn: Remove water from the two adjacent glasses with the combined largest amount
        beth_remove(glasses)

        # Check if any glass contains over 0.5 pint of water (Ali wins condition)
        if check_win_condition(glasses):
            return "Ali"
    return "Beth"  # Beth wins if no glass contains over 0.5 pint after MAX_TURNS turns

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

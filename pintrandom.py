import numpy as np

# Constants
NUM_GLASSES = 5  # Number of glasses
NUM_TURNS = 100  # Number of turns for each simulation

# Function to randomly pour water between glasses
def random_pour(glasses):
    # Randomly choose the amount of water to pour (0.5 pint)
    water = 0.5
    # Randomly choose the source and destination glasses
    source_glass = np.random.randint(NUM_GLASSES)
    destination_glass = np.random.randint(NUM_GLASSES)
    while destination_glass == source_glass:  # Ensure different glasses for source and destination
        destination_glass = np.random.randint(NUM_GLASSES)
    # Pour water from source to destination
    glasses[source_glass] -= water
    glasses[destination_glass] += water

# Function to randomly choose two adjacent glasses to remove water
def random_remove(glasses):
    # Randomly choose the index of the first glass
    index = np.random.randint(NUM_GLASSES - 1)  # To ensure the second glass is adjacent
    # Remove water from the chosen glass and its adjacent glass
    glasses[index] = max(0, glasses[index] - 0.5)
    glasses[index + 1] = max(0, glasses[index + 1] - 0.5)

# Function to check if a glass is filled
def is_glass_filled(glass):
    return glass == 1.0

# Simulate the game for multiple runs
num_runs = 1000
ali_wins = 0
beth_wins = 0

for _ in range(num_runs):
    glasses = np.zeros(NUM_GLASSES)
    for _ in range(NUM_TURNS):
        # Ali's turn
        random_pour(glasses)
        # Check if Ali has won
        if any(is_glass_filled(glass) for glass in glasses):
            ali_wins += 1
            break
        # Beth's turn
        random_remove(glasses)
    else:
        # Beth wins if Ali hasn't filled a pint glass after 100 turns
        beth_wins += 1

# Calculate the win rates
ali_win_rate = ali_wins / num_runs
beth_win_rate = beth_wins / num_runs

# Print the results
print(f"Ali wins: {ali_win_rate * 100:.2f}%")
print(f"Beth wins: {beth_win_rate * 100:.2f}%")

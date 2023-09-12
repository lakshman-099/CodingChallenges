import random

def simulate_dice_rolls(numRolls, numDices, numSides):
    for roll_num in range(numRolls):
        print(f"Roll #{roll_num + 1}")
        
        # Simulate rolling multiple dice and calculate the total
        total_rolled = sum([random.randint(1, numSides) for _ in range(numDices)])
        print(f"The total rolled: {total_rolled}")
        
        # Check for special cases based on the total rolled
        if total_rolled == 7:
            print("Lucky 7")
        if total_rolled == 2 and numDices == 2:
            print("Snake Eyes")
        if total_rolled % 2 == 0:
            print("Even")
        if total_rolled % 2 ==1:
            print("Odd")

# Simulate 2 rolls of 3 six-sided dice
simulate_dice_rolls(2, 3, 6)

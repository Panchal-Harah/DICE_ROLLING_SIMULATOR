import random

def roll_dice(sides, rolls):
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results

def main():
    # Prompt the user for the number of sides on the dice
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            if sides <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Prompt the user for the number of rolls
    while True:
        try:
            rolls = int(input("Enter the number of rolls: "))
            if rolls <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Roll the dice and get the results
    results = roll_dice(sides, rolls)

    # Display the results
    print(f"\nRolling a {sides}-sided dice {rolls} times...")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")

    print("\nSummary of results:")
    print(f"Total Rolls: {rolls}")
    print(f"Results: {results}")
    print(f"Average Roll: {sum(results) / rolls:.2f}")

if __name__ == "__main__":
    main()

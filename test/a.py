def max_ingredients(N, skewers):
    # Sort the skewers
    skewers.sort()

    # Create pairs and calculate the total
    total_ingredients = sum(skewers[i] for i in range(0, 2*N, 2))

    return total_ingredients

# Get inputs
N = int(input().strip())
skewers = list(map(int, input().strip().split()))

# Calculate and print the maximum number of ingredients
print(max_ingredients(N, skewers))

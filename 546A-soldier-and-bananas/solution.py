k, n, w = map(int, input().split())

# k = cost of the first banana
# n = amount of money the soldier has
# w = number of bananas the soldier wants to buy

for i in range(1, w + 1):
    # Calculate the price of the i-th banana
    price = k * i

    # Subtract the price from the remaining money
    n -= price

# If n is negative, -n is the amount we need to borrow.
# Otherwise, we need to borrow nothing.
print(max(0, -n))

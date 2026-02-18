print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Initialize with the first element (no max()/min())
highest = temperatures[0]
lowest = temperatures[0]

# Use a for loop to check each temperature
for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

# Use a for loop and continue to skip non-hot days (<= 30°C)
for temp in temperatures:
    if temp <= 30:
        continue
    hot_days += 1

print(f"Hot Days (>30°C): {hot_days}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days_before_alert = 0
day = 0  # day counter

# Use a for loop with a day counter
for temp in temperatures:
    day += 1

    # Stop immediately if temperature reaches 40°C or higher
    if temp >= 40:
        print(f"Hot Days before alert: {hot_days_before_alert}")
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day}")
        break

    # Count only hot days (>30°C) before the alert
    if temp <= 30:
        continue
    hot_days_before_alert += 1
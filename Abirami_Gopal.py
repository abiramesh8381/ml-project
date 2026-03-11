import numpy as np

# Sensor Temperature Analysis Assignment
# Author: Abirami Gopal

# Data: 4 stations, 5 readings each
data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])

# -------------------------------
# Task 1: Shape and Mean per Station
# -------------------------------
print("Task 1")
print("Shape of data:", data.shape)

mean_per_station = data.mean(axis=1)
print("Mean temperature per station:", mean_per_station)
print()

# -------------------------------
# Task 2: Extract readings above 28.0°C
# -------------------------------
print("Task 2")
mask = data > 28.0
above_28 = data[mask]
print("Temperatures above 28.0°C:", above_28)
print()

# -------------------------------
# Task 3: Normalize data to [0, 1]
# -------------------------------
print("Task 3")
normalized = (data - data.min()) / (data.max() - data.min())
print("Normalized data:\n", np.round(normalized, 2))

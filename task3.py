# task3_analysis.py
# TrendPulse: What's Actually Trending Right Now
# Marks: 20
# Author: <Your Name>
# Note: This script uses Pandas & NumPy to analyse Task 2 output (trends_clean.csv).
# Comments explain the logic for clarity and marks.

import pandas as pd
import numpy as np

# -------------------------------
# 1 — Load and Explore (4 marks)
# -------------------------------

# Load the cleaned CSV from Task 2
df = pd.read_csv("data/trends_clean.csv")

# Print shape of DataFrame
print("Loaded data:", df.shape)

# Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Compute averages using Pandas
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score   :", round(avg_score, 2))
print("Average comments:", round(avg_comments, 2))

# -------------------------------
# 2 — Basic Analysis with NumPy (8 marks)
# -------------------------------

# Convert columns to NumPy arrays for numerical analysis
scores = df["score"].to_numpy()
comments = df["num_comments"].to_numpy()

print("\n--- NumPy Stats ---")
print("Mean score   :", np.mean(scores))
print("Median score :", np.median(scores))
print("Std deviation:", np.std(scores))
print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))

# Category with most stories
most_category = df["category"].value_counts().idxmax()
most_category_count = df["category"].value_counts().max()
print(f"\nMost stories in: {most_category} ({most_category_count} stories)")

# Story with most comments
most_commented = df.loc[df["num_comments"].idxmax()]
print(f"\nMost commented story: \"{most_commented['title']}\" — {most_commented['num_comments']} comments")

# -------------------------------
# 3 — Add New Columns (5 marks)
# -------------------------------

# Engagement = num_comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = True if score > average score
df["is_popular"] = df["score"] > avg_score

# -------------------------------
# 4 — Save the Result (3 marks)
# -------------------------------

# Save updated DataFrame to new CSV for Task 4
df.to_csv("data/trends_analysed.csv", index=False)
print("\nSaved to data/trends_analysed.csv")

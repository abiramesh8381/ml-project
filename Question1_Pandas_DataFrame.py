# Question1_Pandas_DataFrame.py
# Task: Create, Save, Reload, and Explore a Student DataFrame using Pandas

import pandas as pd

# Step 1: Create the DataFrame
data = {
    'StudentID': [101,102,103,104,105,106,107,108,109,110],
    'Name': ['Alice','Bob','Charlie','Diana','Ethan','Fiona','George','Hannah','Ivan','Julia'],
    'Age': [20,21,19,22,20,21,23,19,22,20],
    'Marks': [88,75,92,65,78,85,70,95,60,80],
    'Grade': ['A','B','A','C','B','A','B','A','C','B']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Step 2: Save DataFrame as CSV
df.to_csv('students.csv', index=False)
print("\nDataFrame saved as students.csv")

# Step 3: Reload the CSV into a new DataFrame
df_new = pd.read_csv('students.csv')
print("\nReloaded DataFrame:\n", df_new)

# Step 4: Display the first 3 rows
print("\nFirst 3 rows:\n", df_new.head(3))

# Step 5: Display statistical summary
print("\nStatistical Summary:\n", df_new.describe())

# Step 6: Explore DataFrame properties
print("\nShape of DataFrame:", df_new.shape)
print("\nData Types:\n", df_new.dtypes)
print("\nInfo:")
df_new.info()

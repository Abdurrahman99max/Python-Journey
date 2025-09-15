# ---------------------------------------
# 📌 Assignment: Analyzing Data with Pandas & Visualizing with Matplotlib
# Dataset: Iris dataset
# ---------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

try:
    # Load iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # converts to Pandas DataFrame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # add species column

    print("✅ Dataset loaded successfully!")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display first rows
print("\nFirst 5 rows of dataset:")
print(df.head())

# Explore structure
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# (No missing values in Iris, but if they existed:)
df = df.dropna()

# --------------------------
# Task 2: Basic Data Analysis
# --------------------------

print("\nDescriptive Statistics:")
print(df.describe())

# Grouping: average petal length per species
avg_petal = df.groupby("species")["petal length (cm)"].mean()
print("\nAverage Petal Length per Species:")
print(avg_petal)

# --------------------------
# Task 3: Data Visualization
# --------------------------

# 1. Line Chart (using index as x since no time column in Iris)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Line Chart of Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart - Average Petal Length per Species
plt.figure(figsize=(6,4))
avg_petal.plot(kind="bar", color=["red","green","blue"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram of Sepal Length
plt.figure(figsize=(6,4))
plt.hist(df["sepal length (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()
import pandas as pd
# Created table from a dictionary
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)
print(df)

# Filter rows where Age is greater than 30
Adults = df[df['Age'] > 30]
print(Adults)

# Calculate the average age
average_age = df['Age'].mean()
print("Average Age:", average_age)

# Add a new column 'Salary'
df['Salary'] = [50000, 60000, 55000, 65000]
print(df)
# Save the DataFrame to a CSV file
df.to_csv('people.csv', index=False)
print("DataFrame saved to 'people.csv'")
# Read the CSV file back into a DataFrame
df_from_csv = pd.read_csv('people.csv')
print(df_from_csv)
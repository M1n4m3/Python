import pandas as pd

# 1. Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# 2. Display the DataFrame
print("DataFrame:")
print(df)

# 3. Accessing columns
print("\nNames:")
print(df['Name'])

# 4. Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# 5. Filtering data
print("\nPeople older than 25:")
print(df[df['Age'] > 25])

# 6. Adding a new column
df['Salary'] = [50000, 60000, 45000, 70000]
print("\nDataFrame with Salary column:")
print(df)

# 7. Saving to a CSV file
df.to_csv('people.csv', index=False)
print("\nDataFrame saved to 'people.csv'")

# 8. Reading from a CSV file
df_loaded = pd.read_csv('people.csv')
print("\nData loaded from CSV:")
print(df_loaded)

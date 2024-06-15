import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Age': [24, 27, 22, 32, 29, 24, 30, 22],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago', 'New York', 'Chicago'],
    'Salary': [70000, 80000, 60000, 90000, 75000, 72000, 68000, 66000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)


filtered_city_df = df[df['City'] == 'New York']
print("\nFiltered DataFrame (City is New York):")
print(filtered_city_df)

sorted_df = df.sort_values(by='Age')
print("\nSorted DataFrame by Age (ascending):")
print(sorted_df)

sorted_salary_df = df.sort_values(by='Salary', ascending=False)
print("\nSorted DataFrame by Salary (descending):")
print(sorted_salary_df)


grouped_df = df.groupby('City').mean()
print("\nGrouped DataFrame by City (mean Age and Salary):")
print(grouped_df)


count_df = df.groupby('City').size().reset_index(name='Count')
print("\nGrouped DataFrame by City (count of people):")
print(count_df)
grouped_multiple_df = df.groupby(['City', 'Age'])['Salary'].sum().reset_index()
print("\nGrouped DataFrame by City and Age (sum of Salary):")
print(grouped_multiple_df)

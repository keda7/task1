import pandas as pd


df = pd.read_csv('data.csv')

print("Original DataFrame:")
print(df.head())


df_cleaned = df.dropna()


df_cleaned = df_cleaned.drop_duplicates()


print("Cleaned DataFrame:")
print(df_cleaned.head())

df_cleaned.to_csv('cleaned_data.csv', index=False)

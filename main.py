import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
df = pd.read_csv('C:/Users/User/Documents/GitHub/Pandas/dz.csv')

# Вывод первых 5 строк данных
print(df.head())

# Вывод информации о данных
print(df.info())

# Вывод статистического описания данных
print(df.describe())

# Загрузка данных из файла dz.csv
dz_df = pd.read_csv('dz.csv')

# Определение средней зарплаты по городам
average_salary_by_city = dz_df.groupby('City')['Salary'].mean()

# Вывод средней зарплаты по городам
print(average_salary_by_city)


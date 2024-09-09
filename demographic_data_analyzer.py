import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\arman\OneDrive\Desktop\Coding\table.csv')

# Number of people of each race
race_counts = df['race'].value_counts()
print("Number of people of each race:\n", race_counts)

# Average age of men
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print("Average age of men:", round(average_age_men, 1))

# Percentage of people with a Bachelor's degree
bachelor_percentage = (df['education'] == 'Bachelors').mean() * 100
print("Percentage of people with a Bachelor's degree:", round(bachelor_percentage, 1))

# Percentage of people with advanced education earning >50K
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
if not df[advanced_education].empty:
    percentage_advanced_high_income = (df[advanced_education]['salary'] == '>50K').mean() * 100
else:
    percentage_advanced_high_income = 0
print("Percentage of people with advanced education earning >50K:", round(percentage_advanced_high_income, 1))

# Percentage of people without advanced education earning >50K
non_advanced_education = ~advanced_education
if not df[non_advanced_education].empty:
    percentage_non_advanced_high_income = (df[non_advanced_education]['salary'] == '>50K').mean() * 100
else:
    percentage_non_advanced_high_income = 0
print("Percentage of people without advanced education earning >50K:", round(percentage_non_advanced_high_income, 1))

# Minimum number of hours per week
min_hours_per_week = df['hours-per-week'].min()
print("Minimum number of hours per week:", min_hours_per_week)

# Percentage of people working the minimum number of hours with salary >50K
if not df[df['hours-per-week'] == min_hours_per_week].empty:
    min_hours_high_income_percentage = (df[df['hours-per-week'] == min_hours_per_week]['salary'] == '>50K').mean() * 100
else:
    min_hours_high_income_percentage = 0
print("Percentage of people working minimum hours with salary >50K:", round(min_hours_high_income_percentage, 1))

# Country with highest percentage of people earning >50K
country_percentage_high_income = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size() * 100
if not country_percentage_high_income.empty:
    highest_percentage_country = country_percentage_high_income.idxmax()
    highest_percentage = country_percentage_high_income.max()
else:
    highest_percentage_country = 'N/A'
    highest_percentage = 0
print("Country with highest percentage of people earning >50K:", highest_percentage_country, round(highest_percentage, 1))

# Most popular occupation for high-income earners in India
india_high_income_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
if not india_high_income_df.empty:
    india_high_income_occupation = india_high_income_df['occupation'].mode()
    if not india_high_income_occupation.empty:
        india_high_income_occupation = india_high_income_occupation.iloc[0]  # Use iloc for safe indexing
    else:
        india_high_income_occupation = 'N/A'
else:
    india_high_income_occupation = 'N/A'
print("Most popular occupation for high-income earners in India:", india_high_income_occupation)

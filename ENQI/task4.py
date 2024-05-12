import pandas as pd
import matplotlib.pyplot as pp
import numpy as np

# Load the data
data = pd.read_excel('C:/Users/elim6/OneDrive/Documents/personal/ENQI/Population in Malaysia.xlsx')

# Filter the data for age and gender analysis, excluding overall totals
age_gender_data = data[(data['sex'] != 'overall_sex') & (data['age'] != 'overall_age')]

# Filter the data for ethnicity analysis, excluding overall totals
ethnicity_data = data[data['ethnicity'] != 'overall_ethnicity']

# Filter the data for specific ethnic groups among females
female_ethnic_data = data[(data['sex'] == 'female') & 
                          (data['ethnicity'].isin(['bumi_malay', 'other_bumiputera', 'chinese', 'indian']))]

# Calculate mean and standard deviation for female ethnic groups
mean_std = female_ethnic_data.groupby('ethnicity')['population'].agg(['mean', 'std'])

# Create a bar plot for population by age and gender
fig, ax = pp.subplots(figsize=(14, 7))
ages = age_gender_data['age'].unique()
genders = age_gender_data['sex'].unique()
colors = {'male': 'blue', 'female': 'red'}
width = 0.35  # Bar width

# Aggregate data
age_gender_grouped = age_gender_data.groupby(['age', 'sex']).agg({'population': 'sum'}).reset_index()

for i, gender in enumerate(genders):
    # Filter data by gender
    gender_data = age_gender_grouped[age_gender_grouped['sex'] == gender]
    # Create bar positions
    bar_positions = np.arange(len(ages)) + i * width
    # Plot
    ax.bar(bar_positions, gender_data['population'], width, label=gender, color=colors[gender])

ax.set_xticks(np.arange(len(ages)) + width / 2)
ax.set_xticklabels(ages, rotation=45)
ax.set_title('Population by Age Range for Each Gender in Malaysia')
ax.set_xlabel('Age Range')
ax.set_ylabel('Population')
ax.legend(title='Gender')
pp.show()

# Create a bar plot for population by ethnicity
fig, ax = pp.subplots(figsize=(14, 7))
ethnicity_grouped = ethnicity_data.groupby('ethnicity').agg({'population': 'sum'}).reset_index()

ax.bar(ethnicity_grouped['ethnicity'], ethnicity_grouped['population'])
ax.set_title('Population by Ethnicity in Malaysia')
ax.set_xlabel('Ethnicity')
ax.set_ylabel('Population')
ax.set_xticklabels(ethnicity_grouped['ethnicity'], rotation=45)
pp.show()

# Create a bar plot for female population by ethnicity
fig, ax = pp.subplots(figsize=(14, 7))
female_ethnic_grouped = female_ethnic_data.groupby('ethnicity').agg({'population': 'mean'}).reset_index()

ax.bar(female_ethnic_grouped['ethnicity'], female_ethnic_grouped['population'])
ax.set_title('Female Population by Ethnicity in Malaysia')
ax.set_xlabel('Ethnicity')
ax.set_ylabel('Population')
ax.set_xticklabels(female_ethnic_grouped['ethnicity'], rotation=45)
pp.show()

# Print mean and standard deviation
print(mean_std)

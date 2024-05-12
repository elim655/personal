import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_excel('C:/Users/elim6/OneDrive/Documents/personal/ENQI/Population in Malaysia.xlsx')

# Filter the data for age and gender analysis, excluding overall totals
age_gender_data = data[(data['sex'] != 'overall_sex') & (data['age'] != 'overall_age')]

# Create a bar plot for population by age and gender
plt.figure(figsize=(14, 7))
sns.barplot(data=age_gender_data, x='age', y='population', hue='sex', ci=None)
plt.title('Population by Age Range for Each Gender in Malaysia')
plt.xlabel('Age Range')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.show()


# Filter the data for ethnicity analysis, excluding overall totals
ethnicity_data = data[data['ethnicity'] != 'overall_ethnicity']

# Create a bar plot for population by ethnicity
plt.figure(figsize=(14, 7))
sns.barplot(data=ethnicity_data, x='ethnicity', y='population', ci=None)
plt.title('Population by Ethnicity in Malaysia')
plt.xlabel('Ethnicity')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.show()


# Filter the data for specific ethnic groups among females
female_ethnic_data = data[(data['sex'] == 'female') & 
                          (data['ethnicity'].isin(['bumi_malay', 'other_bumiputera', 'chinese', 'indian']))]

# Calculate mean and standard deviation
mean_std = female_ethnic_data.groupby('ethnicity')['population'].agg(['mean', 'std'])

# Create a bar plot for female population by ethnicity
plt.figure(figsize=(14, 7))
sns.barplot(data=female_ethnic_data, x='ethnicity', y='population', ci=None)
plt.title('Female Population by Ethnicity in Malaysia')
plt.xlabel('Ethnicity')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.show()

# Display mean and standard deviation
print(mean_std)

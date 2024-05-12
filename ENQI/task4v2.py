import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_excel('C:/Users/elim6/OneDrive/Documents/personal/ENQI/Population in Malaysia.xlsx')

# Filter the data for age and gender analysis, excluding overall totals
age_gender_data = data[(data['sex'] != 'overall_sex') & (data['age'] != 'overall_age')]

# Filter the data for ethnicity analysis, excluding overall totals
ethnicity_data = data[data['ethnicity'] != 'overall_ethnicity']

# Filter the data for specific ethnic groups among females
female_ethnic_data = data[(data['sex'] == 'female') & 
                          (data['ethnicity'].isin(['bumi_malay', 'other_bumiputera', 'chinese', 'indian']))]

# Calculate mean and standard deviation
mean_std = female_ethnic_data.groupby('ethnicity')['population'].agg(['mean', 'std'])

# Set up the figure and axes for the subplots
fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(14, 21))  # Adjust size as needed

# First plot: Population by Age and Gender
sns.barplot(data=age_gender_data, x='age', y='population', hue='sex', ci=None, ax=axs[0])
axs[0].set_title('Population by Age Range for Each Gender in Malaysia')
axs[0].set_xlabel('Age Range')
axs[0].set_ylabel('Population')
axs[0].tick_params(axis='x', rotation=45)
axs[0].legend(title='Gender')

# Second plot: Population by Ethnicity
sns.barplot(data=ethnicity_data, x='ethnicity', y='population', ci=None, ax=axs[1])
axs[1].set_title('Population by Ethnicity in Malaysia')
axs[1].set_xlabel('Ethnicity')
axs[1].set_ylabel('Population')
axs[1].tick_params(axis='x', rotation=45)

# Third plot: Female Population by Ethnicity
sns.barplot(data=female_ethnic_data, x='ethnicity', y='population', ci=None, ax=axs[2])
axs[2].set_title('Female Population by Ethnicity in Malaysia')
axs[2].set_xlabel('Ethnicity')
axs[2].set_ylabel('Population')
axs[2].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()

# Display mean and standard deviation
print(mean_std)

import pandas as pd
import plotly.express as px
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Jujin\Desktop\stats-project-dataset\data\heart_failure_clinical_records_dataset.csv')

# print the mean, mode, median, variance, and outliers of ages
# for visualizations, there can be one column for mean/median age at death
# and ages of those who didnt die to compare, highest disease to death correlation, etc.

# prevent truncation of columns to view all data
pd.set_option('display.max_columns', None)

# block 1 - simple stats
mean1 = df['age'].mean()
mode1 = df['age'].mode()
median1 = df['age'].median()
std1 = df['age'].std()
var1 = df['age'].var()
min1 = df['age'].min()
max1 = df['age'].max()
outliers = df[df['age'] > mean1 + 3 * std1]

print(df.describe())

# block 2 - group by
groupby_diabetes = df.groupby(['diabetes']).mean()
groupby_death = df.groupby(['DEATH_EVENT']).mean()

# print block 1
print('Mean age: ' + str(mean1))
print('Mode age: ' + str(mode1))
print('Median age: ' + str(median1))
print('Std of age: ' + str(std1))
print('Var of age: ' + str(var1))
print('Min of age: ' + str(min1))
print('Max of age: ' + str(max1))
print('Outliers of age: ' + str(outliers))

# print block 2
print('Mean of values, grouped by whether they have diabetes: \n' + str(groupby_diabetes))
print('Mean of values, grouped by whether they have died: \n' + str(groupby_death))

# Histogram
# numbers = pd.Series(df.columns)
# df[numbers].hist(figsize = (14, 14))
# plt.show()

# Box plot
# df.plot(kind='box', subplots=True, layout=(4, 4), sharex=False, sharey=False, figsize=(12, 12))
# plt.show()

# densityPlot
# df.plot(kind='density', subplots= True, layout=(4, 4), sharex=False, figsize=(12, 12))
# plt.show()

# Correlation Heatmap
# corr = df.corr()
# f, ax = plt.subplots(figsize=(20, 9))
# sns.heatmap(corr, vmax=8, annot=True)
# plt.show()

# sns.pairplot(df, hue="DEATH_EVENT")
# plt.show()

# sns.pairplot(df [["age", "sex", "high_blood_pressure", "smoking", "diabetes"]], diag_kind="kde")
# plt.show()



import pandas as pd
import plotly.express as px
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data\heart_failure_clinical_records_dataset.csv')

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

mean2 = df['anaemia'].mean()
median2 = df['anaemia'].median()
std2 = df['anaemia'].std()
var2 = df['anaemia'].var()
outliers = df[df['anaemia'] > mean2 + 3 * std2]

mean3 = df['creatinine_phosphokinase'].mean()
median3 = df['creatinine_phosphokinase'].median()
std3 = df['creatinine_phosphokinase'].std()
var3 = df['creatinine_phosphokinase'].var()
outliers2 = df[df['creatinine_phosphokinase'] > mean3 + 3 * std3]

mean4 = df['diabetes'].mean()
median4 = df['diabetes'].median()
std4 = df['diabetes'].std()
var4 = df['diabetes'].var()
outliers3 = df[df['diabetes'] > mean4 + 3 * std4]

mean5 = df['ejection_fraction'].mean()
median5 = df['ejection_fraction'].median()
std5 = df['ejection_fraction'].std()
var5 = df['ejection_fraction'].var()
outliers4 = df[df['ejection_fraction'] > mean5 + 3 * std5]

mean6 = df['high_blood_pressure'].mean()
median6 = df['high_blood_pressure'].median()
std6 = df['high_blood_pressure'].std()
var6 = df['high_blood_pressure'].var()
outliers5 = df[df['high_blood_pressure'] > mean6 + 3 * std6]

mean7 = df['platelets'].mean()
median7 = df['platelets'].median()
std7 = df['platelets'].std()
var7 = df['platelets'].var()
outliers6 = df[df['platelets'] > mean7 + 3 * std7]

mean8 = df['serum_creatinine'].mean()
median8 = df['serum_creatinine'].median()
std8 = df['serum_creatinine'].std()
var8 = df['serum_creatinine'].var()
outliers7 = df[df['serum_creatinine'] > mean8 + 3 * std8]

mean9 = df['serum_sodium'].mean()
median9 = df['serum_sodium'].median()
std9 = df['serum_sodium'].std()
var9 = df['serum_sodium'].var()
outliers8 = df[df['serum_sodium'] > mean9 + 3 * std9]

mean10 = df['sex'].mean()
median10 = df['sex'].median()
std10 = df['sex'].std()
var10 = df['sex'].var()

mean11 = df['smoking'].mean()
median11 = df['smoking'].median()
std11 = df['smoking'].std()
var11 = df['smoking'].var()
outliers9 = df[df['smoking'] > mean11 + 3 * std11]

mean12 = df['DEATH_EVENT'].mean()
median12 = df['DEATH_EVENT'].median()
std12 = df['DEATH_EVENT'].std()
var12 = df['DEATH_EVENT'].var()
outliers10 = df[df['DEATH_EVENT'] > mean12 + 3 * std12]

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

print('Mean anaemia: ' + str(mean2))
print('Median anaemia: ' + str(median2))
print('Std of anaemia: ' + str(std2))
print('Var of anaemia: ' + str(var2))
print('Outliers of anaemia: ' + str(outliers))

print('Mean creatinine_phosphokinase: ' + str(mean3))
print('Median creatinine_phosphokinase: ' + str(median3))
print('Std of creatinine_phosphokinase: ' + str(std3))
print('Var of creatinine_phosphokinase: ' + str(var3))
print('Outliers of creatinine_phosphokinase: ' + str(outliers2))

print('Mean diabetes: ' + str(mean4))
print('Median diabetes: ' + str(median4))
print('Std of diabetes: ' + str(std4))
print('Var of diabetes: ' + str(var4))
print('Outliers of diabetes: ' + str(outliers3))

print('Mean ejection_fraction: ' + str(mean5))
print('Median ejection_fraction: ' + str(median5))
print('Std of ejection_fraction: ' + str(std5))
print('Var of ejection_fraction: ' + str(var5))
print('Outliers of ejection_fraction: ' + str(outliers4))

print('Mean high_blood_pressure: ' + str(mean6))
print('Median high_blood_pressure: ' + str(median6))
print('Std of high_blood_pressure: ' + str(std6))
print('Var of high_blood_pressure: ' + str(var6))
print('Outliers of high_blood_pressure: ' + str(outliers5))

print('Mean platelets: ' + str(mean7))
print('Median platelets: ' + str(median7))
print('Std of platelets: ' + str(std7))
print('Var of platelets: ' + str(var7))
print('Outliers of platelets: ' + str(outliers6))

print('Mean serum_creatinine: ' + str(mean8))
print('Median serum_creatinine: ' + str(median8))
print('Std of serum_creatinine: ' + str(std8))
print('Var of serum_creatinine: ' + str(var8))
print('Outliers of serum_creatinine: ' + str(outliers7))

print('Mean serum_sodium: ' + str(mean9))
print('Median serum_sodium: ' + str(median9))
print('Std of serum_sodium: ' + str(std9))
print('Var of serum_sodium: ' + str(var9))
print('Outliers of serum_sodium: ' + str(outliers8))

print('Mean sex: ' + str(mean10))
print('Median sex: ' + str(median10))
print('Std of sex: ' + str(std10))
print('Var of sex: ' + str(var10))

print('Mean smoking: ' + str(mean11))
print('Median smoking: ' + str(median11))
print('Std of smoking: ' + str(std11))
print('Var of smoking: ' + str(var11))
print('Outliers of smoking: ' + str(outliers9))

print('Mean DEATH_EVENT: ' + str(mean12))
print('Median DEATH_EVENT: ' + str(median12))
print('Std of DEATH_EVENT: ' + str(std12))
print('Var of DEATH_EVENT: ' + str(var12))
print('Outliers of DEATH_EVENT: ' + str(outliers10))

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


# P(a | b) = pd.crosstab(df.a, df.b, normalize='columns')
# P(b | a) = pd.crosstab(df.a, df.b, normalize='index')
cp_anaemia = pd.crosstab(df.anaemia, df.DEATH_EVENT, normalize='index')
print(cp_anaemia)

cp_diabetes = pd.crosstab(df.diabetes, df.DEATH_EVENT, normalize='index')
print(cp_diabetes)

cp_blood_pressure = pd.crosstab(df.high_blood_pressure, df.DEATH_EVENT, normalize='index')
print(cp_blood_pressure)

cp_over_60 = pd.crosstab(df.over_60, df.DEATH_EVENT, normalize='index')
print(cp_over_60)

cp_sex = pd.crosstab(df.sex, df.DEATH_EVENT, normalize='index')
print(cp_sex)

cp_smoke = pd.crosstab(df.smoking, df.DEATH_EVENT, normalize='index')
print(cp_smoke)

cp_abnorm_ck = pd.crosstab(df.abnorm_ck, df.DEATH_EVENT, normalize='index')
print(cp_abnorm_ck)

cp_abnorm_eject_fract = pd.crosstab(df.abnorm_eject_fract, df.DEATH_EVENT, normalize='index')
print(cp_abnorm_eject_fract)

cp_abnorm_platelets = pd.crosstab(df.abnorm_platelets, df.DEATH_EVENT, normalize='index')
print(cp_abnorm_platelets)

cp_abnorm_creatinine = pd.crosstab(df.abnorm_creatinine, df.DEATH_EVENT, normalize='index')
print(cp_abnorm_creatinine)

cp_abnorm_sodium = pd.crosstab(df.abnorm_sodium, df.DEATH_EVENT, normalize='index')
print(cp_abnorm_sodium)
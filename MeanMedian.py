import pandas as pd
df = pd.read_csv (r'C:\Users\Jujin\Desktop\stats-project-dataset\data\heart_failure_clinical_records_dataset.csv')

# block 1 - simple stats
mean1 = df['age'].mean()
median1 = df['age'].median()
std1 = df['age'].std()
var1 = df['age'].var()

# block 2 - group by
groupby_diabetes = df.groupby(['diabetes']).mean()

# print block 1
print ('Mean age: ' + str(mean1))
print ('Median age: ' + str(median1))
print ('Std of age: ' + str(std1))
print ('Var of age: ' + str(var1))
#
# # print block 2
print ('Mean of values, grouped by whether they have diabetes: \n' + str(groupby_diabetes))

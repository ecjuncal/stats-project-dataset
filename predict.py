import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, plot_confusion_matrix

df = pd.read_csv(r'C:\Users\Jujin\Desktop\stats-project-dataset\data\heart_failure_clinical_records_dataset.csv')

x = df[['ejection_fraction', 'serum_creatinine', 'serum_sodium', 'age', 'diabetes', 'high_blood_pressure', 'anaemia', 'sex', 'smoking']]
y = df['DEATH_EVENT']

#Spliting data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.2)

scorelist = []
knn = None
for i in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(x_train, y_train)
    predict = knn.predict(x_test)
    score = accuracy_score(y_test, predict)
    scorelist.append(round(100 * score, 2))
print("K Nearest Neighbors Top 5 Success Rates: ")
print(sorted(scorelist, reverse=True)[:5])
plot_confusion_matrix(knn, x_test, y_test)
plt.show()

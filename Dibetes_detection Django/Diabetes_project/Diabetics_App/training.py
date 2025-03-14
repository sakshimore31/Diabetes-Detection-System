import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

df=pd.read_csv(r'C:\Users\HP\.spyder-py3\Dibetes_detection\Diabetes_project\Diabetics_App\diabetes.csv')

print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df.duplicated().sum())

#analysis
print(df.isna().sum())
print(df.nunique().sort_values())
print(df.isna().sum())
sns.countplot(x='Outcome',data=df)

#feature selection manual
x=df.drop(['Pregnancies','Outcome'],axis=1)
#data=data.dropna()
print(type(x))

y=df['Outcome']
print(type(y))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.20,random_state=1234)

from sklearn.svm import SVC
#from sklearn.ensemble import RandomForestClassifier // svm-support vector machine

svcclassifier = SVC()
svcclassifier.fit(x_train,y_train)
y_pred = svcclassifier.predict(x_test)
print(y_pred)

print("=" * 40)
print("==========")
print("Classification Report: ",(classification_report(y_test,y_pred)))
print("Accuracy: ",accuracy_score(y_test,y_pred)*100)
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
#ACC =(accuracy_score(y_test,y_pred)+100)
#repo =(classification_report(y_test,y_pred))

#confusion matrix
conf_matrix= confusion_matrix(y_test,y_pred)
print("====================")
print("Confusion Matrix :\n",conf_matrix)

#plot the confusion matrix

plt.figure(figsize=(10,7))
sns.heatmap(conf_matrix,annot=True, fmt='d',cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

from joblib import dump
dump(svcclassifier, "model.joblib")
print("Model saved as model.joblib")

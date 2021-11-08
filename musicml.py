# -*- coding: utf-8 -*-
"""MusicML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gEKKBTJvFFTY0CyL6STTSyhGyqUuk-LC
"""

import pandas as pd

from google.colab import drive

drive.mount('/content/gdrive')

df = pd.read_csv('/content/gdrive/My Drive/music.csv')

df

#Assumption => #1 - male, 0 denotes female

#Men => 20-25 Hiphop, 26-30 Jazz, 30+ Classical

#women => 20-25 Dance, 26-30 Acoustics, 30+ Classical

df.describe()

#PREPARING THE DATA => CLEAN THE DATA, split the dataset to input set and output set

#Output set => genre is the prediction to be made, The input set is gender and age

x = df.drop(columns=['genre'])      #split dataset to input set, excluding the output or data to be predicted
x

#output dataset
y = df['genre']
y

from sklearn.tree import DecisionTreeClassifier

model  = DecisionTreeClassifier()                                                                             #create instance of the class
model.fit(x,y)                                                                                        #train the model, takes two parameters, the input and the output set

predict = model.predict([[21,1]])
predict[0]

#ACCURACY

from sklearn.model_selection import train_test_split                                    #splits datasets into two sets

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)                  #print values in tuples, 0.2 specifies 20% for testing date and 80% for training

trainmodel = DecisionTreeClassifier()
trainmodel.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
pred = trainmodel.predict(x_test)

score = accuracy_score(y_test, pred)                                                    #accuracy score between 0-1, compare between actual value and predicted value
score

age = int(input("Enter Age : "))
gender = input("Enter Gender : ")
gender = gender.lower()

if gender == 'male':
  g = 1
else:
  g = 0

prediction = model.predict([[age,g]])
prediction[0]

from sklearn.externals import joblib
joblib.dump(model,'music-recommend')


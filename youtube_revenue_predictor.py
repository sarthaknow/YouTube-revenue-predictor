# -*- coding: utf-8 -*-
"""YouTube revenue predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WyJcAVCju_3tpjRQ90noysjNaFo4S8Ou
"""

from google.colab import drive
drive.mount('/content/drive')

"""# Importing primary Libraries"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

"""# **Loading YouTube channel dataset**"""

os.chdir("/content/drive/MyDrive/Youtube revenue predict")  # Accessing YT revenue folder in Drive

df = pd.read_excel("The_Concept_Guy_YT.xlsx")  # 365 days data of my YT Channel (The Concept Guy)
df.head()

######################################################### Time to only SECONDS

def view_dur_sec(t):      # Changing Hours:Minutes:Seconds to Seconds
  for i in range(0,len(t)):
    h,m,s = t[i].split(':')
    tot_sec = int(h) * 3600 + int(m) * 60 + int(s)
    t[i] = tot_sec


dfnum = df["Av­er­age view dur­a­tion"].astype(str)
view_dur_sec(dfnum) 
dfnum  # Converted to seconds
df["Av­er­age view dur­a­tion"] = dfnum

data_df = df.iloc[1:, 3:df.shape[1]]   # Removing unnecessary data
data_df.head()

data_df.info()

data_df.describe() # Obtaining various statistics

data_df.isnull().values.any()  # Checking NaN values if any

data_df.head()

"""# Initialising X and Y"""

X= data_df.drop("Your es­tim­ated rev­en­ue (INR)",axis=1)

X.head()

Y = data_df["Your es­tim­ated rev­en­ue (INR)"]

Y.head()

"""# **Train Test Split**"""

from sklearn.model_selection import train_test_split as tts

X_train, X_test , y_train, y_test = tts(X,Y,test_size=0.3, random_state=1)

X_train.head()

y_train

"""# **Developing ML model**"""

from sklearn.linear_model import LinearRegression as linreg

model = linreg()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error as mse 

rmse = np.sqrt(mse(y_test,y_pred))
print(rmse)

plotx = np.arange(1,len(y_test)+1)

plt.scatter(plotx ,y_test)
plt.scatter(plotx ,y_pred)

max(y_test)

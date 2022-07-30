import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import r2_score
from datetime import date, timedelta,datetime
import math


data= pd.read_csv("Covid19_India11.csv")


def confirmed_cases(day):
    label = []
    value = []
    real_x= data.iloc[:,1].values
    real_y= data.iloc[:,2].values
    real_x= real_x.reshape(-1,1)
    real_y= real_y.reshape(-1,1)
    training_x,testing_x,training_y,testing_y = train_test_split(real_x,real_y,test_size=0.3,random_state=0)
    Lin= LinearRegression()
    Lin.fit(training_x,training_y)

   # pred_y= Lin.predict(testing_x)

    for i in range(1,15):
        end_date= ((datetime.now()+timedelta(day)) + timedelta(days=i) ).strftime('%Y-%m-%d')
        C_cases=Lin.predict([[40+day+i]])
        conf_cases=math.trunc(C_cases[0][0])
        label.append(end_date)
        value.append(conf_cases)

    return  value,label


# this will show recovery cases
def Recovered_cases(day):
    label_rec = []
    value_rec = []
    real_x= data.iloc[:,1].values
    real_y= data.iloc[:,3].values
    real_x= real_x.reshape(-1,1)
    real_y= real_y.reshape(-1,1)
    training_x,testing_x,training_y,testing_y = train_test_split(real_x,real_y,test_size=0.3,random_state=0)
    Lin= LinearRegression()
    Lin.fit(training_x,training_y)
    pred_y= Lin.predict(testing_x)
    for i in range(1, 15):
        end_date = ((datetime.now()+timedelta(day)) + timedelta(days=i)).strftime('%Y-%m-%d')
        recovered_cases = Lin.predict([[40 + day + i]])
        rec_cases = math.trunc(recovered_cases[0][0])
        label_rec.append(end_date)
        value_rec.append(rec_cases)

    return value_rec,label_rec
#

# this will predict graph for recovered cases (training set)



#accur=r2_score(testing_y,pred_y)*100
#print("accuracy recovered cases using trainig set =%.2f"%accur)

#this will predict death rate
def death_cases(day):
    label_det=[]
    value_det=[]
    real_x= data.iloc[:,1].values
    real_y= data.iloc[:,4].values
    real_x= real_x.reshape(-1,1)
    real_y= real_y.reshape(-1,1)
    training_x,testing_x,training_y,testing_y = train_test_split(real_x,real_y,test_size=0.3,random_state=0)
    Lin= LinearRegression()
    Lin.fit(training_x,training_y)

    pred_y= Lin.predict(testing_x)
    for i in range(1, 15):
        end_date = ((datetime.now()+timedelta(day)) + timedelta(days=i)).strftime('%Y-%m-%d')
        death_predict = Lin.predict([[40 + day + i]])
        death_pred = math.trunc(death_predict[0][0])
        label_det.append(end_date)
        value_det.append(death_pred)
    return value_det, label_det

#ac=r2_score(testing_y,pred_y)*100
#print("accuracy death cases using training set =%.2f"%ac)


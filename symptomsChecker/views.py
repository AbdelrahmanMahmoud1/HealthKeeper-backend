from django.shortcuts import render
import pandas as pd
import numpy as np
import joblib as joblib
from pathlib import Path
# Create your views here.
def check (arr):
    file_path = Path(__file__).resolve().parent / './random_forest.joblib'
    loaded_rf = joblib.load(file_path)
    arry = list(map(int, arr))
    try:
        return predd(loaded_rf,arry[0],arry[1],arry[2],arry[3],arry[4],arry[5],arry[6],arry[7],arry[8],
            arry[9],arry[10],arry[11],arry[12],arry[13],arry[14],arry[15],arry[16])
    except:
        return  "Sorry I cant Detect that Disease"


def predd(x,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17):
    file_path1 = Path(__file__).resolve().parent / './Symptom-severity.csv'
    file_path2 = Path(__file__).resolve().parent / './symptom_Description.csv'
    file_path3 = Path(__file__).resolve().parent / './symptom_precaution.csv'

    print(S1)
    df1 = pd.read_csv(file_path1)
    df1['Symptom'] = df1['Symptom'].str.replace('_',' ')
    discrp = pd.read_csv(file_path2)
    ektra7at = pd.read_csv(file_path3)

    psymptoms = [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17]
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j]==a[k]:
                psymptoms[j]=b[k]
    psy = [psymptoms]
    pred2 = x.predict(psy)
    disp= discrp[discrp['Disease']==pred2[0]]
    print(disp)
    disp = disp.values[0][1]
    recomnd = ektra7at[ektra7at['Disease']==pred2[0]]
    c=np.where(ektra7at['Disease']==pred2[0])[0][0]
    precuation_list=[]
    x=""
    for i in range(1,len(ektra7at.iloc[c])):
          precuation_list.append(ektra7at.iloc[c,i])

    x= x +"The Disease Name: "+pred2[0]+"\n"

    x= x +"The Disease Discription: "+disp+"\n"

    x= x +"Recommended Things to do at home: " + "\n"

    for i in precuation_list:
  
        x= x + i + "\n"
    
    print(x)
    return x

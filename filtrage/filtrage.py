# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:52:49 2021

@author: youss
"""
import pandas as pd
import numpy as np

def filter(fileName, listParam):
    df = pd.read_csv(fileName)
    
    data = np.array([df[listParam[0]]])

    i = 1
    for param in listParam[1:len(listParam)]:
        data = np.r_[ data, [df[param]] ]
        i = i+1
        
    print(data)
    print(data.shape[0])
    fdata = np.array([listParam])
    print(fdata)
    
    f = open('outputfile.csv', 'w')
    f.write(listParam[0]+'\n')
    for i in range(data.shape[1]-1):
        f.write(data[0][i]+'\n')
    f.write(data[0][i+1])
    f.close()
   
    # Add a list as column
    for i in range(1 , data.shape[0]):
        df = pd.read_csv("outputfile.csv")
        df[listParam[i]] = ""
        df.to_csv("outputfile.csv", index=False)
        #df = pd.read_csv("out.csv")
        df[listParam[i]] = data[i]
        df.to_csv("outputfile.csv", index=False)
    
    
    
    
#La liste des colonnes à réserver
listParam = ['Div','HomeTeam','AwayTeam','FTHG','FTAG']
filter('SP1.csv',listParam)

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:31:24 2016

@author: pedro.a.morales
"""

import pandas as pd

#This method will suppport only csv at the moment
def loadData(filePath):
    
    if filePath.endswith('.csv'):
        data = open(filePath)
    else:
        return None
    
    df = pd.DataFrame.from_csv(data,index_col=None)

    return df.head(20)
    

def main():
    loadData('ds1.csv')    
    
    
if __name__ == '__main__':
    main()